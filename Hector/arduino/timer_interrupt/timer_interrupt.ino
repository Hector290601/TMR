int vel1 = 0;
int tmp = 0;
int vel2 = 0;
int a = 0;
/*
 * This program control a servo on the pin 7 via serial comunication@115200 Bauds
 * The Serial port wait from a char and convert it to a dutycycle.
 * The values goes from the 32Ascii " " to thw 127 Ascii "~" and the range is 60 degrees on all the range
 * The bad aspect about this program is, the middle (127Ascii "O") it not the servo middle.
 * The servo middle is moved to 10 degrees to the lower range (it can say, the first 127 values just moves over 10 degrees)
 * TODO:
 *  - Correct the servo range
 *  - Improve the algorithm
 *  - Make some data chekout, like a SHA to validate the information's correct sending/reciving
 *  - be happy :)
 */
void setup(){
  pinMode(7,OUTPUT);
  Serial.begin(115200);
  cli();
  TCCR0A = 0;
  TCCR0B = 0;
  TCCR1A = 0;
  TCCR1B = 0;
  TCCR2A = 0;
  TCCR2B = 0;
  TCCR0B |= B00000011;
  TCCR1B |= B00000010;
  TCCR2B |= B00000100;
  TIMSK0 |= B00000010;
  TIMSK1 |= B00000010;
  TIMSK2 |= B00000010;
  OCR0A = 255;
  OCR1A = 39980;
  OCR2A = 0;
  sei();
}

void loop(){
  while(Serial.available() == 0){
  }
  a = Serial.read();
  OCR0A = int((2.71*a)-86.81);
}


ISR(TIMER0_COMPA_vect){
  TCNT0 = 0;
  digitalWrite(7, 0);
}

ISR(TIMER1_COMPA_vect){
  TCNT0 = 0;
  TCNT1 = 0;
  TCNT2 = 0;
  digitalWrite(7, 1);
}

ISR(TIMER2_COMPA_vect){
  TCNT2 = 0;
}
