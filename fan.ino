/*  
 * Arduino side sketch
 * I'm using arduino nano 328 
 *
 */

#define RELAY 8
char perintah;

void setup() {
  Serial.begin(9600);
  pinMode(RELAY, OUTPUT);
  Serial.flush();
}

void loop() {
  if (Serial.available()) {
    perintah = Serial.read();
    Serial.flush();
		
    switch(perintah) {
      case 'n':
        if(digitalRead(RELAY) == HIGH) {
          digitalWrite(RELAY, LOW);
          Serial.println("success on");
        }
        else Serial.println("already on");
        break;

      case 'm':
        if(digitalRead(RELAY) == LOW) {
          digitalWrite(RELAY, HIGH);
          Serial.println("success off");
        }
        else Serial.println("already off");
      default:
        Serial.println("undefined");
     }
   }
}

