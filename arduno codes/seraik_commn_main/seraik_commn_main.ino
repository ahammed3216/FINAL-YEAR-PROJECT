#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

int timer=0;

void setup() {
  // put your setup code here,   to run once:
  lcd.init(); // initialize the lcd
  lcd.backlight();
  pinMode( LED_BUILTIN , OUTPUT );
  Serial.begin(9600);
}

void   loop() {
  // put your main code here, to run repeatedly:
  for (int k=0;k<4;k++)
  {
    if(Serial.available()   > 0)
    {
        timer=Serial.parseInt();
        lcd.clear();                 // clear display
        lcd.setCursor(0, 0);
        lcd.print(k+1);// move cursor to   (0, 0)
        lcd.setCursor(0, 1);
        for(int j=timer;j>=0;j--)
          lcd.print(j);
        
    }


  
}
}
