const int soilMoisturePin = A0; // Analog pin A0
int soilMoistureValue = 0; // Variable to store the value from the sensor

void setup() {
  // Initialize serial communication at 9600 bits per second
  Serial.begin(9600);
}

void loop() {
  // Read the value from the soil moisture sensor
  soilMoistureValue = analogRead(soilMoisturePin);

  // Print the value to the serial port
  Serial.print("Soil Moisture Value: ");
  Serial.println(1023 - soilMoistureValue);

  // Wait for a bit before taking another reading
  delay(1000); // 1 second delay
}
