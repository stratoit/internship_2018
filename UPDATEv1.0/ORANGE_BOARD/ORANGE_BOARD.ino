#include <SPI.h>
#include "WizFi250.h"
#include <SoftwareSerial.h>
#include <Servo.h>

int out1 = 9;
int out2 = 10;
String val1;
int val=0;
int speed =538,n=8;
int ang =70;
char c;
int count=0;
SoftwareSerial mySerial(3, 2); // RX, TX

Servo Throttle, Steer;

//RPM
const int ledPin = 13;//the led attach to pin13
int sensorPin = A0; // select the input pin for the potentiometer
int digitalPin=7; //D0 attach to pin7
long rpm=0;

int sensorValue = 0;// variable to store the value coming from A0
boolean digitalValue=0, prevdigitalValue=0;// variable to store the value coming from pin7

unsigned long t=0,cur_t,t1=0,t2=0,t3=0,t4=0;//time variables
unsigned long t5=0;
//RPM
//int rpm_int=0;
long rpm_int=0;
void setSpeed(int speed){
    int angle = map(speed, 0, 1000, 0, 180); //Sets servo positions to different speeds
    Throttle.write(angle);
    }

char ssid[] = "stratoit2";    // your network SSID (name)
char pass[] = "strato1010";          // your network password
int status = WL_IDLE_STATUS;       // the Wifi radio's status

char server[] = "192.168.0.10";

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

  // RPM
  pinMode(digitalPin,INPUT);//set the state of D0 as INPUT
  pinMode(ledPin,OUTPUT);//set the state of pin13 as OUTPUT
  //RPM
  
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

int step = 0;
void loop()
{
  //
  cur_t=micros()/1000;
 
  // sped is sinousoidal and adjustable
  if(cur_t-t5 > 200) {

    double outval = speed + 5.0 * sin(360/n*step);
    step++;
    step%=n;

    setSpeed((int)outval);
    t5 = cur_t;  
  }


// code to convert the value coming into the client buffer to suitable steer/ speed write commands.

  while (client.available()) {
     c = client.read();
     val1=c;  
     val = atoi(val1.c_str());
     Serial.println(val);
     if(val == 1) {while (ang>30){ang=ang-10; Steer.write(ang);}}
     
     else if(val == 3) {if (ang>50){while(ang>50){ang=ang-10;Steer.write(ang);}}
                        else if(ang<50){ang=ang+10;Steer.write(ang);ang=ang+10;Steer.write(ang);}}
                        
     else if(val == 5) {if(ang>70){while(ang>70){ang=ang-10;Steer.write(ang);}}
                        else if(ang<70){while(ang<70){ang=ang+10;Steer.write(ang);}}
                        else {ang=70; Steer.write(ang);}}
                        
     //else if(val == 6) {ang=70; Steer.write(ang);}
     
     else if(val == 7) {if (ang<90){while(ang<90){ang=ang+10;Steer.write(ang);}}
                        else if(ang>90){ang=ang-10;Steer.write(ang);ang=ang-10;Steer.write(ang);}}
                        
     else if(val == 9) {while (ang<110){ang=ang+10;Steer.write(ang);}}
     
     else if(val == 6) {n-=1;}
     else if(val == 8) {n+=1;}
     else if(val == 2) {speed+=1;}
     else if(val == 4) {speed-=1;}
     else if(val == 0) {setSpeed(535);break;}
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


