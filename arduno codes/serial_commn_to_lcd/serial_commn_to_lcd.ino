#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

int datafromUser=0;

void setup() {
  // put your setup code here,   to run once:
  lcd.init(); // initialize the lcd
  lcd.backlight();
  pinMode( LED_BUILTIN , OUTPUT );
  Serial.begin(9600);
}

void   loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()   > 0)
  {
    datafromUser=Serial.read();
  }

  if(datafromUser ==   '1')
  {
    digitalWrite( LED_BUILTIN , HIGH );
    lcd.clear();                 // clear display
    lcd.setCursor(0, 0);         // move cursor to   (0, 0)
    lcd.print("led on"); 
  }
  else if(datafromUser   == '0')
  {
    digitalWrite( LED_BUILTIN, LOW);
    lcd.clear();                 // clear display
    lcd.setCursor(0, 0);         // move cursor to   (0, 0)
    lcd.print("led off"); 
  }
  
}
