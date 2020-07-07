#define tmp 2000

void setup() {
  Serial1.begin(9600);
}

void loop() {
  Serial1.write('A');
  delay(tmp);
  Serial1.write('a');
  delay(tmp);  
}
