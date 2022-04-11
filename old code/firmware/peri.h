#define UP_PRESSED() ((PINC & (1<<PC2)) == 0)
#define DOWN_PRESSED() ((PINC & (1<<PC1)) == 0)
#define RIGHT_PRESSED() ((PINC & (1<<PC3)) == 0)
#define LEFT_PRESSED() ((PINC & (1<<PC0)) == 0)

void init_peri();
uint16_t read_adc(uint8_t channel);
