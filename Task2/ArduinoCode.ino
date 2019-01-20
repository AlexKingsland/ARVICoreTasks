int input;
int pin = 8;
void setup() { 
  
  Serial.begin(9600);
  pinMode(pin, OUTPUT);

  Serial.write("Enter 1 to turn LED on, enter 0 to turn LED off");
}
 
void loop() {

  input = Serial.read();

  if (input == '1'){
    digitalWrite (pin, HIGH);
  }else if (input == '0'){
    digitalWrite (pin, LOW);
  }

}
