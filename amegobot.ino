#define M1_DIR 4
#define M1_PWM 5
#define M2_DIR 7
#define M2_PWM 6

int speed = 100;
int LidL;
int LidR;
int position;
int min_value;
int time_one_calibration_position = 2000;
int time_two_calibration_position = 5000;
int time_three_calibration_position = 5000;
bool line;
int synchronization_with_line = 3;

void Motor(int SpeedL, int SpeedR) {
  digitalWrite(M1_DIR, SpeedL);
  digitalWrite(M2_DIR, SpeedR);
}

void SensorsPoll() {
  LidL = analogRead(A0);
  LidR = analogRead(A1);
}

void setup() {
  // put your setup code here, to run once:
  pinMode(M1_DIR, OUTPUT);
  pinMode(M1_PWM, OUTPUT);
  pinMode(M2_DIR, OUTPUT);
  pinMode(M2_PWM, OUTPUT);
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
}

void one_calibration() {
  for (int i = 0; 0 <= time_one_calibration_position; i++) {
    SensorsPoll();
    Motor(-speed, speed);
    if (LidL || LidR > min_value) {
      Motor(speed, speed);
      delay(100);
      line = true;
      break;
    }
  }
}

void two_calibration() {
  for (int i = 0; 0 <= time_two_calibration_position; i++) {
    SensorsPoll();
    Motor(0, speed);
    if (LidL || LidR > min_value) {
      Motor(speed, speed);
      delay(100);
      line = true;
      break;
    }
  }
}

void three_calibration() {
  for (int i = 0; 0 <= time_three_calibration_position; i++) {
    SensorsPoll();
    Motor(speed / 2, speed);
    if (LidL || LidR > min_value) {
      Motor(speed, speed);
      delay(100);
      line = true;
      break;
    }
  }
}

void Motor_Stop() {
  Motor(0, 0);
}

void Calibrate_Left() {
  if (LidL > LidR) {
    Motor(speed / 2, speed);
    delay(300);
    Motor_Stop();
  }
}

void Calibrate_Right() {
  if (LidL < LidR) {
    Motor(speed, speed / 2);
    delay(300);
    Motor_Stop();
  }
}

void loop() {
  SensorsPoll();
  if (LidL > LidR) {
    Motor(speed - map(LidL - LidR, 0, LidL, 0, speed), speed);
  }
  if (LidL < LidR) {
    Motor(speed, speed - map(LidR - LidL, 0, LidR, 0, speed));
  }

  if (LidL && LidR < min_value) {
    if (line = false) one_calibration();
    if (line = false) two_calibration();
    if (line = false) three_calibration();
    if (line = false) exit(0);
    if (line = true) {
      for (int i = 0; i <= synchronization_with_line; i++) {
        SensorsPoll();
        Calibrate_Left();
        Calibrate_Right();
      }
      line = false;
    }
  }
}
