void setup() {
  // Inicializar la comunicación serial a 9600 baudios
  Serial.begin(9600);
}

void loop() {
  // Leer el valor del potenciómetro
  int PD = analogRead(A1);
  int ID = analogRead(A0);
  int MD = analogRead(A6);
  int MI = analogRead(A9);
  int II = analogRead(A8);
  int Pi = analogRead(A7);
  int Flex1 = analogRead(A10);
  int Flex2 = analogRead(A11);
  int Flex3 = analogRead(A12);
  int Flex4 = analogRead(A13);
  // Enviar el valor a través de la comunicación serial
    Serial.print("A0: ");
  Serial.println(ID);
    Serial.print("A1: ");
  Serial.println(PD);
    Serial.print("A6: ");
  Serial.println(MD);


    Serial.print("A9: ");
  Serial.println(MI);
    Serial.print("A8: ");
  Serial.println(II);
    Serial.print("A7: ");
  Serial.println(Pi);

     Serial.print("A10: ");
  Serial.println(Flex1);
    Serial.print("A11: ");
  Serial.println(Flex2);
    Serial.print("A12: ");
  Serial.println(Flex3);
    Serial.print("A13: ");
  Serial.println(Flex4); 
  // Esperar un breve periodo de tiempo antes de leer el siguiente valor
  delay(100);
}

