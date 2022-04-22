void setup() {
  Serial.begin(115200);
  pinMode(2, INPUT_PULLUP);
}

void loop() {
  Serial.print(" X:"); Serial.print(analogRead(A1));
  Serial.print(" Y:"); Serial.print(analogRead(A0));
  Serial.print(" Z:"); Serial.print(analogRead(A2));
  Serial.print(" A:"); Serial.print(digitalRead(2));
  Serial.println();
  delay(250);
}
