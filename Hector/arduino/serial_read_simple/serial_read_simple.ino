void setup(){
  pinMode(21, OUTPUT); // motor
  pinMode(22, OUTPUT); // servo
  
  for(int i = 2; i < 20; i++){
    pinMode(i, INPUT);
  }
  Serial.begin(115200);
}

/*
 *                                  RASPBERRY
 +-----+-----+---------+------+---+---Pi 3B--+---+------+---------+-----+-----+
 |     | Ard |   Name  | Mode |   | Physical |   | Mode | Name    | Ard |     |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 |     |     |    3.3v |      |   |  1 || 2  |   |      | 5v      |     |     |
 |     |     |   SDA.1 | ALT0 | 1 |  3 || 4  |   |      | 5v      |     |     |
 |     |     |   SCL.1 | ALT0 | 1 |  5 || 6  |   |      | 0v      | GND |     |
 |     |   2 | GPIO. 7 |   IN | 1 |  7 || 8  | 1 | ALT5 | TxD     |     |     |
 |     |     |      0v |      |   |  9 || 10 | 1 | ALT5 | RxD     |     |     |
 |     |   3 | GPIO. 0 |   IN | 0 | 11 || 12 | 0 | IN   | GPIO. 1 |  4  |     |
 |     |   5 | GPIO. 2 |   IN | 0 | 13 || 14 |   |      | 0v      |     |     |
 |     |   6 | GPIO. 3 |   IN | 0 | 15 || 16 | 0 | IN   | GPIO. 4 |  7  |     |
 |     |     |    3.3v |      |   | 17 || 18 | 0 | IN   | GPIO. 5 |  8  |     |
 |     |     |    MOSI | ALT0 | 0 | 19 || 20 |   |      | 0v      |     |     |
 |     |     |    MISO | ALT0 | 0 | 21 || 22 | 0 | IN   | GPIO. 6 |  9  |     |
 |     |     |    SCLK | ALT0 | 0 | 23 || 24 | 1 | OUT  | CE0     |     |     |
 |     |     |      0v |      |   | 25 || 26 | 1 | OUT  | CE1     |     |     |
 |     |     |   SDA.0 |   IN | 1 | 27 || 28 | 1 | IN   | SCL.0   |     |     |
 |     |  10 | GPIO.21 |   IN | 1 | 29 || 30 |   |      | 0v      |     |     |
 |     |  11 | GPIO.22 |   IN | 1 | 31 || 32 | 0 | IN   | GPIO.26 | 12  |     |
 |     |  13 | GPIO.23 |   IN | 0 | 33 || 34 |   |      | 0v      |     |     |
 |     |  14 | GPIO.24 |   IN | 0 | 35 || 36 | 0 | IN   | GPIO.27 | 15  |     |
 |     |  16 | GPIO.25 |   IN | 0 | 37 || 38 | 0 | IN   | GPIO.28 | 17  |     |
 |     |     |      0v |      |   | 39 || 40 | 0 | IN   | GPIO.29 | 18  |     |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 | BCM | Ard |   Name  | Mode | V | Physical | V | Mode | Name    | Ard | BCM |
 +-----+-----+---------+------+---+---Pi 3B--+---+------+---------+-----+-----+

 +-----+-----+---------+------+---+---Pi 4B--+---+------+---------+-----+-----+
 | BCM | Ard |   Name  | Mode | V | Physical | V | Mode | Name    | Ard | BCM |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 |     |     |    3.3v |      |   |  1 || 2  |   |      | 5v      |     |     |
 |     |     |   SDA.1 | ALT0 | 1 |  3 || 4  |   |      | 5v      |     |     |
 |     |     |   SCL.1 | ALT0 | 1 |  5 || 6  |   |      | 0v      |     |     |
 |     |   2 | GPIO. 7 |   IN | 1 |  7 || 8  | 1 | ALT5 | TxD     |     |     |
 |     |     |      0v |      |   |  9 || 10 | 1 | ALT5 | RxD     |     |     |
 |     |   3 | GPIO. 0 |   IN | 0 | 11 || 12 | 0 | IN   | GPIO. 1 | 4   |     |
 |     |   5 | GPIO. 2 |   IN | 0 | 13 || 14 |   |      | 0v      |     |     |
 |     |   6 | GPIO. 3 |   IN | 0 | 15 || 16 | 0 | IN   | GPIO. 4 | 7   |     |
 |     |     |    3.3v |      |   | 17 || 18 | 0 | IN   | GPIO. 5 | 8   |     |
 |     |     |    MOSI | ALT0 | 0 | 19 || 20 |   |      | 0v      |     |     |
 |     |     |    MISO | ALT0 | 0 | 21 || 22 | 0 | IN   | GPIO. 6 | 9   |     |
 |     |     |    SCLK | ALT0 | 0 | 23 || 24 | 1 | OUT  | CE0     |     |     |
 |     |     |      0v |      |   | 25 || 26 | 1 | OUT  | CE1     |     |     |
 |     |     |   SDA.0 |   IN | 1 | 27 || 28 | 1 | IN   | SCL.0   |     |     |
 |     |  10 | GPIO.21 |   IN | 1 | 29 || 30 |   |      | 0v      |     |     |
 |     |  11 | GPIO.22 |   IN | 1 | 31 || 32 | 0 | IN   | GPIO.26 | 12  |     |
 |     |  13 | GPIO.23 |   IN | 0 | 33 || 34 |   |      | 0v      |     |     |
 |     |  14 | GPIO.24 |   IN | 0 | 35 || 36 | 0 | IN   | GPIO.27 | 15  |     |
 |     |  16 | GPIO.25 |   IN | 0 | 37 || 38 | 0 | IN   | GPIO.28 | 17  |     |
 |     |     |      0v |      |   | 39 || 40 | 0 | IN   | GPIO.29 | 18  |     |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+---Pi 4B--+---+------+---------+-----+-----+

 *
 * Protocolo:
 *  +-----+-------------+---------+
 *  | Pin | Significado | Bandera |
 *  +-----+-------------+---------+
 *  |  2  | Start flag  | True    |
 *  +-----+-------------+---------+
 *  |  3  | Servo digit | False   |
 *  +-----+-------------+---------+
 *  |  4  | Servo digit | False   |
 *  +-----+-------------+---------+
 *  |  5  | Servo digit | False   |
 *  +-----+-------------+---------+
 *  |  6  | Servo digit | False   |
 *  +-----+-------------+---------+
 *  |  7  | Servo digit | False   |
 *  +-----+-------------+---------+
 *  |  8  | Servo digit | False   |
 *  +-----+-------------+---------+
 *  |  9  | Servo digit | False   |
 *  +-----+-------------+---------+
 *  |  10 | Servo digit | False   |
 *  +-----+-------------+---------+
 *  |  11 | Servo digit | False   |
 *  +-----+-------------+---------+
 *  |  12 | Servo digit | False   |
 *  +-----+-------------+---------+
 *  |  13 |  Motor digi | False   |
 *  +-----+-------------+---------+
 *  |  14 |  Motor digi | False   |
 *  +-----+-------------+---------+
 *  |  15 |  Motor digi | False   |
 *  +-----+-------------+---------+
 *  |  16 |  Motor digi | False   |
 *  +-----+-------------+---------+
 *  |  17 |  Motor digi | False   |
 *  +-----+-------------+---------+
 *  |  18 |  End flag   | True    |
 *  +-----+-------------+---------+
 */

int read_parallel_speed(){
  int pins[4] = {3, 4, 5, 8};
  int x = 0;
  for(int i = 0; i < 4; i++){
    x <<= 1;
    x += digitalRead(pins[i]);
    Serial.print(i);
    Serial.print(": ");
    Serial.println(digitalRead(pins[i]));
  }
  return x;
}

void loop(){
//  int spd[6];
//  int strng[10];
  bool flag = false;
  String spd = "";
  String strng = "";
  if(digitalRead(2) == 1 and digitalRead(18) == 0 and not flag){
      flag = true;
//    Serial.print("2: ");
//    Serial.println(digitalRead(2));
      Serial.println(read_parallel_speed());
//    Serial.print("18: ");
//    Serial.println(digitalRead(18));
  }
}

//
//void loop(){
//  int velocidad_motor = 500;
//  int steering_servo = 0;
//  long lectura = 0;
//  int val[16];
//  int duty_cycle_h_m = 1000 + velocidad_motor;
//  int duty_cycle_l_m = 20000 - duty_cycle_h_m;
////  int duty_cycle_h_s = 700 + + ( ( lectura * 6) / 10);
//  int duty_cycle_h_s = 700;
//  int duty_cycle_l_s = 20000 - duty_cycle_h_s;
//  for(int i = 2; i < 18; i+=2){
//    val[2 - i] = digitalRead(i);
//    Serial.println(i);
//    Serial.println(val[2-i]);
//  }
//  digitalWrite(10, 1);
//  delayMicroseconds(duty_cycle_h_m);
//  digitalWrite(10, 0);
//  delayMicroseconds(duty_cycle_l_m);
//  digitalWrite(11, 1);
//  delayMicroseconds(duty_cycle_h_s);
//  digitalWrite(11, 0);
//  delayMicroseconds(duty_cycle_l_m);
//}
