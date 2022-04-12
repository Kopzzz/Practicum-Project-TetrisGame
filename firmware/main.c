#include <avr/io.h>
#include <avr/interrupt.h>  /* for sei() */
#include <util/delay.h>     /* for _delay_ms() */
#include <avr/pgmspace.h>   /* required by usbdrv.h */

#include "peri.h"
#include "usbdrv.h"

#define RQ_GET_CHECK_UP      0
#define RQ_GET_CHECK_DOWN    1
#define RQ_GET_CHECK_RIGHT   2
#define RQ_GET_CHECK_LEFT    3
#define RQ_GET_LIGHT         4
#define RQ_GET_TEMP          5

/* ------------------------------------------------------------------------- */
/* ----------------------------- USB interface ----------------------------- */
/* ------------------------------------------------------------------------- */
usbMsgLen_t usbFunctionSetup(uint8_t data[8])
{
    usbRequest_t *rq = (void *)data;

    /* declared as static so they stay valid when usbFunctionSetup returns */
    static uint8_t up_state;
    static uint8_t down_state;
    static uint8_t right_state;
    static uint8_t left_state;

    static uint16_t light_value;
    //static uint16_t temp_value;

    if (rq->bRequest == RQ_GET_CHECK_UP)
    {
        up_state = UP_PRESSED();

        /* point usbMsgPtr to the data to be returned to host */
        usbMsgPtr = &up_state;

        /* return the number of bytes of data to be returned to host */
        return 1;
    }

    else if (rq->bRequest == RQ_GET_CHECK_DOWN)
    {
        down_state = DOWN_PRESSED();

        /* point usbMsgPtr to the data to be returned to host */
        usbMsgPtr = &down_state;

        /* return the number of bytes of data to be returned to host */
        return 1;
    }

    else if (rq->bRequest == RQ_GET_CHECK_RIGHT)
    {
        right_state = RIGHT_PRESSED();

        /* point usbMsgPtr to the data to be returned to host */
        usbMsgPtr = &right_state;

        /* return the number of bytes of data to be returned to host */
        return 1;
    }

    else if (rq->bRequest == RQ_GET_CHECK_LEFT)
    {
        left_state = LEFT_PRESSED();

        /* point usbMsgPtr to the data to be returned to host */
        usbMsgPtr = &left_state;

        /* return the number of bytes of data to be returned to host */
        return 1;
    }

    else if (rq->bRequest == RQ_GET_LIGHT)
    {
        light_value = read_adc(PC4);
        usbMsgPtr = (uchar*) &light_value;
        return sizeof(light_value);
    }

    /*else if (rq->bRequest == RQ_GET_TEMP)
    {
        temp_value = read_adc(PC0);
        usbMsgPtr = (uchar*) &temp_value;
        return sizeof(temp_value);
    }*/

    /* default for not implemented requests: return no data back to host */
    return 0;
}

/* ------------------------------------------------------------------------- */
int main(void)
{
    init_peri();
    usbInit();

    /* enforce re-enumeration, do this while interrupts are disabled! */
    usbDeviceDisconnect();
    _delay_ms(300);
    usbDeviceConnect();

    /* enable global interrupts */
    sei();

    /* main event loop */
    for(;;)
    {
        usbPoll();
    }

    return 0;
}

/* ------------------------------------------------------------------------- */
