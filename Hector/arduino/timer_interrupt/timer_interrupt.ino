int vel1 = 0;
int tmp = 0;
int vel2 = 0;

void setup(){
  pinMode(7,OUTPUT);
  pinMode(12,OUTPUT);
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
  OCR1A = 19990;
  OCR2A = 0;
  sei();
}

void loop(){
  if(Serial.available() > 0){
    vel1 = Serial.read();
    OCR0A = vel1;
    Serial.print("vel1: ");
    Serial.println(vel1);
  }
  if(Serial.available() > 0){
    vel2 = Serial.read();
    OCR2A = vel2;
    Serial.print("vel2: ");
    Serial.println(vel2);
  }
}


ISR(TIMER0_COMPA_vect){
  TCNT0 = 0;
  digitalWrite(7, 0);
}

ISR(TIMER1_COMPA_vect){
  TCNT0 = 0;
  TCNT1 = 0;
  TCNT2 = 0;
  digitalWrite(12, 1);
  digitalWrite(7, 1);
}

ISR(TIMER2_COMPA_vect){
  TCNT2 = 0;
  digitalWrite(12, 0);
}
