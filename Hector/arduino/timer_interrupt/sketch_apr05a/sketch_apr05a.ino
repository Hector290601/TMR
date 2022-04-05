bool LED_STATE = true;

void setup(){
  pinMode(13,OUTPUT);
  cli();
  TCCR1A = 0;
  TCCR1B = 0;
  TCCR1B |= B00000101;
  TIMSK1 |= B00000010;
  OCR1A = 125;
  sei();
}

void loop(){
}

ISR(TIMER1_COMPA_vect){
  TCNT1 = 0;
  LED_STATE = !LED_STATE;
  digitalWrite(13, LED_STATE);
}
