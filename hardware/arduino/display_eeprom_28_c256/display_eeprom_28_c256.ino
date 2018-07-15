#define SHIFT_DATA 2
#define SHIFT_CLK 4
#define SHIFT_LATCH 3

#define EEPROM_D0 5
#define EEPROM_D7 12

#define WRITE_EN 13
#define OUT_EN A0


void pulse(int pin, int width) {
  digitalWrite(pin, LOW);
  delayMicroseconds(width);
  digitalWrite(pin, HIGH);
  delayMicroseconds(width);
  digitalWrite(pin, LOW);
}

void setAddress(int address, bool output_enable) {
  shiftOut(SHIFT_DATA, SHIFT_CLK, MSBFIRST, address >> 8);
  shiftOut(SHIFT_DATA, SHIFT_CLK, MSBFIRST, address);
  digitalWrite(OUT_EN, output_enable ? LOW : HIGH);
  pulse(SHIFT_LATCH, 0);
}

byte readEEPROM(int address) {
  for(int i = 0; i < 8; i++) pinMode(EEPROM_D0 + i, INPUT);
  setAddress(address, true);
  
  byte data = 0;
  for(int pin = EEPROM_D7; pin >= EEPROM_D0; pin--) {
    data = (data << 1) + digitalRead(pin);
  }
  return data;
}

void writeEEPROM(int address, byte data) {
  for(int i = 0; i < 8; i++) pinMode(EEPROM_D0 + i, OUTPUT);
 
  setAddress(address, true);
  for(int pin = EEPROM_D0; pin <= EEPROM_D7; pin += 1) {
    digitalWrite(pin, data & 1);
    data >>= 1;
  }
  
  digitalWrite(WRITE_EN, LOW);
  delayMicroseconds(1);
  digitalWrite(WRITE_EN, HIGH);
  delay(10);
}

void clearEEPROM() {
  for(long i = 0; i < 32768; i++) {
    setAddress(i, false);
    writeEEPROM(i, 0xff);
  }
  Serial.println("Erased EEPROM");
}

void printEEPROM() {
  
    Serial.println("Reading EEPROM");
    for(long i = 0; i <= 512; i += 1) {
      char buf[200];
      sprintf(buf, "%03x ", i*64);
      for(int j = 0; j < 64; j++) {
        sprintf(buf+strlen(buf), "%02x ", readEEPROM(i*64+j));
      }
      Serial.println(buf);
    }
    
}

void disable_write_protection() {
  writeEEPROM(0x5555, 0xaa);
  writeEEPROM(0x2aaa, 0x55);
  writeEEPROM(0x5555, 0x80);
  writeEEPROM(0x5555, 0xaa);
  writeEEPROM(0x2aaa, 0x55);
  writeEEPROM(0x5555, 0x20);
}

void setup() {
  pinMode(SHIFT_DATA, OUTPUT);
  pinMode(SHIFT_CLK, OUTPUT);
  pinMode(SHIFT_LATCH, OUTPUT);
  pinMode(WRITE_EN, OUTPUT);
  pinMode(OUT_EN, OUTPUT);
  digitalWrite(WRITE_EN, HIGH);
  
  Serial.begin(115200);

  for (int i = 0; i < 16; i++)
    Serial.println(readEEPROM(0x01));
  //setAddress(0x00, false);
  //Serial.println(readEEPROM(0x7fff));
}


void loop() {

}
