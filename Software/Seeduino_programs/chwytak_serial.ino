#include <Servo.h>
Servo servo; 
String in_byte;
int state;

void setup() {
 
  servo.attach(8);
  Serial.begin(9600);
  servo.write(180);
}

void loop()
{    
  if(Serial.available()) 
  { 
    in_byte = Serial.readStringUntil('\n');
    state = in_byte.toInt();        
    servo.write(state);   
  }
}
