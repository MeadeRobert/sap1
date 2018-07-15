#define SHIFT_DATA 2
#define SHIFT_CLK 4
#define SHIFT_LATCH 3

#define EEPROM_D0 5
#define EEPROM_D7 12

#define WRITE_EN 13


void pulse(int pin, int width) {
  digitalWrite(pin, LOW);
  delayMicroseconds(width);
  digitalWrite(pin, HIGH);
  delayMicroseconds(width);
  digitalWrite(pin, LOW);
}

void setAddress(int address, bool output_enable) {
  // shift in 7 most significant address bits and output enable in bit 12 for 28c16
  shiftOut(SHIFT_DATA, SHIFT_CLK, MSBFIRST, (address >> 8) | (output_enable ? 0x00 : 0x80));
  // shift in remaining 4 address bits for 28c16
  shiftOut(SHIFT_DATA, SHIFT_CLK, MSBFIRST, address);
  pulse(SHIFT_LATCH, 500);
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
 
  setAddress(address, false);
  for(int pin = EEPROM_D0; pin <= EEPROM_D7; pin += 1) {
    digitalWrite(pin, data & 1);
    data >>= 1;
  }
  digitalWrite(WRITE_EN, LOW);
  digitalWrite(WRITE_EN, HIGH);
  delay(10);
}

void clearEEPROM() {
  for(int i = 0; i <= pow(2, 12); i++) {
    setAddress(i, false);
    writeEEPROM(i, 0xff);
  }
  Serial.println("Erased EEPROM");
}

void printEEPROM() {
  for(int k = 0; k < 4; k++) {
  for(int i = 0; i <= 255; i += 16) {
    char buf[80];
    sprintf(buf, "%03x ",k * 0x100 + i);
    for(int j = 0; j < 16; j++) {
      sprintf(buf + strlen(buf), "%02x ", readEEPROM(i+j+0x100*k));
    }
    Serial.println(buf);
  }
  }
}

void setup() {
  pinMode(SHIFT_DATA, OUTPUT);
  pinMode(SHIFT_CLK, OUTPUT);
  pinMode(SHIFT_LATCH, OUTPUT);
  digitalWrite(WRITE_EN, HIGH);
  pinMode(WRITE_EN, OUTPUT);
  Serial.begin(57600);


  //setAddress(0, false);

  printEEPROM();
  Serial.println();


  Serial.print("Programming EEPROM");
  byte digits[] = { 0x7e, 0x30, 0x6d, 0x79, 0x33, 0x5b, 0x5f, 0x70, 0x7f, 0x7b };
  for(int address = 0; address < 255; address += 1) {
    writeEEPROM(0x300 + address, digits[address % 10]);
    writeEEPROM(0x100 + address, (address / 10 % 10) == 0 && (address / 100 % 10) < 1 ? 0 : digits[address / 10 % 10]);
    writeEEPROM(0x200 + address, (address / 100 % 10) == 0 ? 0 : digits[address / 100 % 10]);
    writeEEPROM(0x000 + address, 0);
    if(address % 64 == 0) Serial.print(".");
  }
  Serial.println(" Done");

  //clearEEPROM();
  printEEPROM();
}

void loop() {
 
 

}
