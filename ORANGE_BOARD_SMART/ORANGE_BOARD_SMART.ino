#include <SPI.h>
#include "WizFi250.h"
#include <SoftwareSerial.h>
#include <Servo.h>

int out1 = 9;
int out2 = 10;
String val1;
int val=0;
int speed =0;
int ang =70;
char c;
int count=0;
SoftwareSerial mySerial(3, 2); // RX, TX

Servo Throttle, Steer;

void setSpeed(int speed){
    int angle = map(speed, 0, 1000, 0, 180); //Sets servo positions to different speeds
    Throttle.write(angle);
    }

char ssid[] = "Protec";    // your network SSID (name)
char pass[] = "protec1234";          // your network password
int status = WL_IDLE_STATUS;       // the Wifi radio's status

char server[] = "192.168.201.31";

// Initialize the Ethernet client object
WiFiClient client;

void printWifiStatus();

void setup()
{
  char c;
  Serial.begin(115200);
  
  mySerial.begin(115200); //Changed
  Throttle.attach(10); //Adds ESC to certain pin. arm();
  Steer.attach(9); 
  
  WiFi.init();

    // check for the presence of the shield
    if (WiFi.status() == WL_NO_SHIELD) {
      Serial.println("WiFi shield not present");
      // don't continue
      while (true);
    }

    // attempt to connect to WiFi network
    while ( status != WL_CONNECTED) {
      Serial.print("Attempting to connect to WPA SSID: ");
      Serial.println(ssid);
      // Connect to WPA/WPA2 network
      status = WiFi.begin(ssid, pass);
    }

    // you're connected now, so print out the data
    Serial.println("You're connected to the network");

    printWifiStatus();

    Serial.println();
    Serial.println("Starting connection to server...");
    // if you get a connection, report back via serial
    if (client.connect(server, 8888)) {
      Serial.println("Connected to server");
      // Make a HTTP request
    
    }
}



void loop()
{
  while (client.available()) {
     c = client.read();
     val1=c;  
     val = atoi(val1.c_str());
     Serial.print(val);
     Serial.println("");
     count+=1;
     Serial.println(count);
     if(val == 3) {ang = 30; Steer.write(ang);}
     else if(val == 6) {ang = 70; Steer.write(ang);}
     else if(val == 9) {ang = 110; Steer.write(ang);}
     else if(val == 8) {speed = speed+1;setSpeed(539 + speed);}             
     else if(val == 0) {speed = speed-1; setSpeed(539 + speed);}

  }

  // if the server's disconnected, stop the client
  if (!client.connected()) {
    Serial.println();
    Serial.println("Disconnected");
   // client.stop();

    // do nothing forevermore
    while (true);
  }
}

void printWifiStatus()
{
  // print the SSID of the network you're attached to
  Serial.print("SSID: ");
  Serial.println(WiFi.SSID());

  // print your WiFi shield's IP address
  IPAddress ip = WiFi.localIP();
  Serial.print("IP Address: ");
  Serial.println(ip);

  // print the received signal strength
  long rssi = WiFi.RSSI();
  Serial.print("Signal strength (RSSI):");
  Serial.print(rssi);
  Serial.println(" dBm");
}


