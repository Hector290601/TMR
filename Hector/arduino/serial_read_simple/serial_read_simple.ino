void setup(){
  pinMode(10, OUTPUT); // motor
  pinMode(11, OUTPUT); // servo
  pinMode(A0, OUTPUT);
  pinMode(A4, OUTPUT);
  for(int i = 22; i < 49; i+=2){
    pinMode(i, INPUT);
  }
  Serial.begin(115200);
}

/*
 +-----+-----+---------+------+---+---Pi 3B--+---+------+---------+-----+-----+
 |     | Ard |   Name  | Mode |   | Physical |   | Mode | Name    | Ard |     |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 |     |     |    3.3v |      |   |  1 || 2  |   |      | 5v      |     |     |
 |     |     |   SDA.1 | ALT0 | 1 |  3 || 4  |   |      | 5v      |     |     |
 |     |     |   SCL.1 | ALT0 | 1 |  5 || 6  |   |      | 0v      | GND |     |
 |     |  22 | GPIO. 7 |   IN | 1 |  7 || 8  | 1 | ALT5 | TxD     |     |     |
 |     |     |      0v |      |   |  9 || 10 | 1 | ALT5 | RxD     |     |     |
 |     |  24 | GPIO. 0 |   IN | 0 | 11 || 12 | 0 | IN   | GPIO. 1 | 26  |     |
 |     |  28 | GPIO. 2 |   IN | 0 | 13 || 14 |   |      | 0v      |     |     |
 |     |  30 | GPIO. 3 |   IN | 0 | 15 || 16 | 0 | IN   | GPIO. 4 | 32  |     |
 |     |     |    3.3v |      |   | 17 || 18 | 0 | IN   | GPIO. 5 | 34  |     |
 |     |     |    MOSI | ALT0 | 0 | 19 || 20 |   |      | 0v      |     |     |
 |     |     |    MISO | ALT0 | 0 | 21 || 22 | 0 | IN   | GPIO. 6 | 36  |     |
 |     |     |    SCLK | ALT0 | 0 | 23 || 24 | 1 | OUT  | CE0     |     |     |
 |     |     |      0v |      |   | 25 || 26 | 1 | OUT  | CE1     |     |     |
 |     |     |   SDA.0 |   IN | 1 | 27 || 28 | 1 | IN   | SCL.0   |     |     |
 |     |  38 | GPIO.21 |   IN | 1 | 29 || 30 |   |      | 0v      |     |     |
 |     |  40 | GPIO.22 |   IN | 1 | 31 || 32 | 0 | IN   | GPIO.26 | 42  |     |
 |     |  44 | GPIO.23 |   IN | 0 | 33 || 34 |   |      | 0v      |     |     |
 |     |  46 | GPIO.24 |   IN | 0 | 35 || 36 | 0 | IN   | GPIO.27 | 48  |     |
 |     |     | GPIO.25 |   IN | 0 | 37 || 38 | 0 | IN   | GPIO.28 |     |     |
 |     |     |      0v |      |   | 39 || 40 | 0 | IN   | GPIO.29 |     |     |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+---Pi 3B--+---+------+---------+-----+-----+

 */

void loop(){
  int velocidad_motor = 500;
  int steering_servo = 0;
  long lectura = 0;
  int val[14];
  digitalWrite(A0, LOW);
  digitalWrite(A4, HIGH);
  lectura = analogRead(A2);
//  Serial.println(lectura);
  int duty_cycle_h_m = 1000 + velocidad_motor;
  int duty_cycle_l_m = 20000 - duty_cycle_h_m;
  int duty_cycle_h_s = 700 + + ( ( lectura * 6) / 10);
  int duty_cycle_l_s = 20000 - duty_cycle_h_s;
  for(int i = 22; i < 49; i+=2){
    val[22 - i] = digitalRead(i);
    Serial.println(i);
    Serial.println(val[22-i]);
  }
  digitalWrite(10, 1);
  delayMicroseconds(duty_cycle_h_m);
  digitalWrite(10, 0);
  delayMicroseconds(duty_cycle_l_m);
  digitalWrite(11, 1);
  delayMicroseconds(duty_cycle_h_s);
  digitalWrite(11, 0);
  delayMicroseconds(duty_cycle_l_m);
}
