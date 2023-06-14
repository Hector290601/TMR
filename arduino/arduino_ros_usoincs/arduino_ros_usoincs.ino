int enables[] = {3, 4};
int vccs[] = {5, 6, 7, 8};
int triggers[] = {9, 10, 11, 12};
int echos[] = {13, 14, 15, 16};
int usonics[3][4] = {
  {
    1, 2, 3, 4
    },
  {
    5, 6, 7, 8
    },
  {
    9, 10, 11, 12
    },
};
int distances[12];

void setup() {
  // put your setup code here, to run once:
  for(int i = 0; i < 2; i++){
    pinMode(enables[i], OUTPUT);
    pinMode(vccs[i], OUTPUT);
    digitalWrite(vccs[i], 0);
    pinMode(triggers[i], OUTPUT);
    pinMode(echos[i], INPUT);
  }
  for(int i = 2; i < 4; i++){
    pinMode(vccs[i], OUTPUT);
    digitalWrite(vccs[i], 0);
    pinMode(triggers[i], OUTPUT);
    pinMode(echos[i], INPUT);
  }
  Serial.begin(115200);
}

void reader(int group){
  long duration, distance;
  int writable = group * 3;
  if(group == 0 or group == 1){
    digitalWrite(enables[0], 1);
  }
  for(int i = 0; i < 4; i++){
    digitalWrite(vccs[i], 0);
  }
  digitalWrite(vccs[group], 1);
  for(int i = 0; i < 4; i++){
    digitalWrite(triggers[i], 0);
    delayMicroseconds(2);
    digitalWrite(triggers[i], 1);
    delayMicroseconds(10);
    digitalWrite(triggers[i], 0);
    duration = pulseIn(echos[i], HIGH);
    distance = duration * 0.0344 / 2;
    distances[i + writable] = (int)distance;
  }
}

void loop() {
  long duration, distance;
  int writable = 0 * 3;
    digitalWrite(triggers[0], 0);
    delayMicroseconds(2);
    digitalWrite(triggers[0], 1);
    delayMicroseconds(10);
    digitalWrite(triggers[0], 0);
    duration = pulseIn(echos[0], HIGH);
    distance = duration * 0.0344 / 2;
    distances[0 + writable] = (int)distance;
  for(int i = 0; i < 11; i++){
    Serial.println(distances[i]);
  }
  Serial.println("##############");
}
