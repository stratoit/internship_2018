#include <Debug.h>
#include <JSN270.h>
#include <Arduino.h>
#include <SoftwareSerial.h>
#include <Servo.h>

#define SSID      "stratoit2"		// your wifi network SSID
#define KEY       "strato1010"		// your wifi network password
#define AUTH       "WPA2" 		// your wifi network security (NONE, WEP, WPA, WPA2)
int out1 = 9;
int out2 = 10;
String val1;
int val=0;
int speed =0;
int ang =70;
char c;

#define USE_DHCP_IP 15

#if !USE_DHCP_IP
#define MY_IP          "192.168.1.133"
#define SUBNET         "255.255.255.0"
#define GATEWAY        "192.168.1.254"
#endif

#define HOST_IP        "192.168.0.5"
#define REMOTE_PORT    8888
#define PROTOCOL       "TCP"

SoftwareSerial mySerial(3, 2); // RX, TX
 
JSN270 JSN270(&mySerial);

Servo Throttle, Steer;

void setSpeed(int speed)
  {
    int angle = map(speed, 0, 1000, 0, 180); //Sets servo positions to different speeds
    Throttle.write(angle);
  }


void setup() {
	char c;

	mySerial.begin(9600);
	Serial.begin(9600);
        Throttle.attach(10); //Adds ESC to certain pin. arm();
        Steer.attach(9); 

	/*Serial.println("--------- JSN270 TCP Client with WPA2 Test --------");

	// wait for initilization of JSN270
	delay(5000);
	//JSN270.reset();
	delay(1000);

	//JSN270.prompt();
	JSN270.sendCommand("at+ver\r");
	delay(5);
	while(JSN270.receive((uint8_t *)&c, 1, 1000) > 0) {
		Serial.print((char)c);
	}
	delay(1000);*/

#if USE_DHCP_IP
	JSN270.dynamicIP();
#else
	JSN270.staticIP(MY_IP, SUBNET, GATEWAY);
#endif    
    
	if (JSN270.join(SSID, KEY, AUTH)) {
		Serial.println("WiFi connect to " SSID);
	}
	else {
		Serial.println("Failed WiFi connect to " SSID);
		Serial.println("Restart System");

		return;
	}
	delay(1000);

	/*JSN270.sendCommand("at+wstat\r");
	delay(5);
	while(JSN270.receive((uint8_t *)&c, 1, 1000) > 0) {
		Serial.print((char)c);
	}
	delay(1000);        

	JSN270.sendCommand("at+nstat\r");
	delay(5);
	while(JSN270.receive((uint8_t *)&c, 1, 1000) > 0) {
		Serial.print((char)c);
	}
	delay(1000);*/

	if (!JSN270.client(HOST_IP, REMOTE_PORT, PROTOCOL)) {
		Serial.println("Failed connect to " HOST_IP);
		Serial.println("Restart System");
	} else {
		Serial.println("Socket connect to " HOST_IP);
		//delay(2000);
		
		// Enter data mode
		//JSN270.sendCommand("at+exit\r");
		//delay(5);
	}
        JSN270.clear();
}

void loop() {
        val1="";
	while(JSN270.available()) {
                c=JSN270.read();
                val1+=c;  
                if(!JSN270.available()){
                  val = atoi(val1.c_str());
                  Serial.print(val);
                  Serial.println("");
                  if(val == 8) {speed = speed+1; setSpeed(530 + speed);}
                  else if(val == 9) {{speed = speed-1; setSpeed(530 + speed);}} 
                  else if(val == 3) { if(ang<100) {ang = ang+10; Steer.write(ang);}  }
                  else if(val == 4) { if(ang>24){ang = ang-10; Steer.write(ang); } }
                  else if(val == 1) { if(ang<90) {ang = ang+20; Steer.write(ang);}  }
                  else if(val == 6) { if(ang>34){ang = ang-20; Steer.write(ang); } }
                  else if(val == 2) {if(ang<105){ang = ang+5; Steer.write(ang);  }}
                  else if(val == 5) {if(ang>19){ang = ang-5; Steer.write(ang);}}
                  else if(val == 7) {ang = 70; Steer.write(ang);}
                  else if(val == 0) {speed = 0; setSpeed(530);}

                }
                
                            
	}
	if(Serial.available()) {
		//JSN270.print((char)Serial.read());
	}
}
