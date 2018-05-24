
#include <Servo.h>

Servo Steer;

int val;
int out1 = 10; //for speed control

void setup()
  {
   Steer.attach(9);
   Serial.begin(9600);
   pinMode(out1,OUTPUT);
   pinMode(out1,OUTPUT);
   Serial.println("Bluetooth");
  }

void loop()
  {
    if (Serial.available())
    {
      val = Serial.parseInt();
        if (val == 0) {analogWrite(out1, 0)  ; Serial.println("Speed is = 0"); val = 200;}
        if (val == 1) {analogWrite(out1, 255); delay(10); analogWrite(out1, 170) ; Serial.println("Speed is = 1"); val = 200;}
        if (val == 2) {analogWrite(out1, 255); delay(10); analogWrite(out1, 180) ; Serial.println("Speed is = 2"); val = 200;}
        if (val == 3) {analogWrite(out1, 255); delay(10); analogWrite(out1, 190); Serial.println("Speed is = 3"); val = 200;}
        if (val == 4) {analogWrite(out1, 255); delay(10); analogWrite(out1, 200); Serial.println("Speed is = 4"); val = 200;}
        if (val == 5) {analogWrite(out1, 255); delay(10); analogWrite(out1, 210); Serial.println("Speed is = 5"); val = 200;}
        if (val == 6) {analogWrite(out1, 255); delay(10); analogWrite(out1, 220); Serial.println("Speed is = 6"); val = 200;}
        if (val == 7) {analogWrite(out1, 255); delay(10); analogWrite(out1, 230); Serial.println("Speed is = 7"); val = 200;}
        if (val == 8) {analogWrite(out1, 255); delay(10); analogWrite(out1, 240); Serial.println("Speed is = 8"); val = 200;}
        if (val == 9) {analogWrite(out1, 255); delay(10); analogWrite(out1, 250); Serial.println("Speed is = 9"); val = 200;}
    if(val > 10 && val < 190){Steer.write(val); Serial.println(val);}
    }
  }
