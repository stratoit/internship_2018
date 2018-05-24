#include <Debug.h>
#include <JSN270.h>
#include <Arduino.h>
#include <SoftwareSerial.h>

#define SSID      "stratoit2"		// your wifi network SSID
#define KEY       "strato1010"		// your wifi network password
#define AUTH       "WPA2" 		// your wifi network security (NONE, WEP, WPA, WPA2)
int out1 = 9;
int out2 = 10;
String val1;
int val;

#define USE_DHCP_IP 1

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

void setup() {
	char c;

	mySerial.begin(9600);
	Serial.begin(9600);
        pinMode(9,OUTPUT);
        pinMode(9,OUTPUT);
        pinMode(10,OUTPUT);
        pinMode(10,OUTPUT);

	Serial.println("--------- JSN270 TCP Client with WPA2 Test --------");

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
	delay(1000);

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

	JSN270.sendCommand("at+wstat\r");
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
	delay(1000);

	if (!JSN270.client(HOST_IP, REMOTE_PORT, PROTOCOL)) {
		Serial.println("Failed connect to " HOST_IP);
		Serial.println("Restart System");
	} else {
		Serial.println("Socket connect to " HOST_IP);
		delay(2000);
		
		// Enter data mode
		JSN270.sendCommand("at+exit\r");
		delay(5);
	}
        JSN270.clear();
}

void loop() {
	if(JSN270.available()) {
                val1="";
                val=JSN270.read()-48;
                Serial.print(val);
                //Serial.print(val);
                //JSN270.print((char)val);
                if (val == 0) {analogWrite(out1, 0)  ; Serial.println("Speed is = 0"); val = 100;}
                if (val == 1) {analogWrite(out1, 255); delay(10); analogWrite(out1, 175) ; Serial.println("Speed is = 1"); val = 100;}
                if (val == 2) {analogWrite(out1, 255); delay(10); analogWrite(out1, 185) ; Serial.println("Speed is = 2"); val = 100;}
                if (val == 3) {analogWrite(out1, 255); delay(10); analogWrite(out1, 195); Serial.println("Speed is = 3"); val = 100;}
                if (val == 4) {analogWrite(out1, 255); delay(10); analogWrite(out1, 205); Serial.println("Speed is = 4"); val = 100;}
                if (val == 5) {analogWrite(out1, 255); delay(10); analogWrite(out1, 215); Serial.println("Speed is = 5"); val = 100;}
                if (val == 6) {analogWrite(out1, 255); delay(10); analogWrite(out1, 225); Serial.println("Speed is = 6"); val = 100;}
                if (val == 7) {analogWrite(out1, 255); delay(10); analogWrite(out1, 235); Serial.println("Speed is = 7"); val = 100;}
                
               // Right Angle Control
                if (val == 10) {analogWrite(out2, 170)  ; Serial.println(" Right Angle is = 0"); val = 100;}
                if (val == 11) {analogWrite(out2, 255); delay(10); analogWrite(out2, 180) ; Serial.println(" Right Angle is = 1"); val = 100;}
                if (val == 12) {analogWrite(out2, 255); delay(10); analogWrite(out2, 190) ; Serial.println(" Right Angle is = 2"); val = 100;}
                if (val == 13) {analogWrite(out2, 255); delay(10); analogWrite(out2, 200); Serial.println(" Right Angle is = 3"); val = 100;} 
                if (val == 14) {analogWrite(out2, 255); delay(10); analogWrite(out2, 210); Serial.println(" Right Angle is = 4"); val = 100;}
                if (val == 15) {analogWrite(out2, 255); delay(10); analogWrite(out2, 220); Serial.println(" Right Angle is = 5"); val = 100;}
                if (val == 16) {analogWrite(out2, 255); delay(10); analogWrite(out2, 230); Serial.println(" Right Angle is = 6"); val = 100;}
                if (val == 17) {analogWrite(out2, 255); delay(10); analogWrite(out2, 240); Serial.println(" Right Angle is = 7"); val = 100;}
            
               // Left Angle Control
                if (val == 20) {analogWrite(out2, 170)  ; Serial.println(" Left Angle is = 0"); val = 100;}
                if (val == 21) {analogWrite(out2, 255); delay(10); analogWrite(out2, 160) ; Serial.println(" Left Angle is = 1"); val = 100;}
                if (val == 22) {analogWrite(out2, 255); delay(10); analogWrite(out2, 150) ; Serial.println(" Left Angle is = 2"); val = 100;}
                if (val == 23) {analogWrite(out2, 255); delay(10); analogWrite(out2, 140); Serial.println(" Left Angle is = 3"); val = 100;}
                if (val == 24) {analogWrite(out2, 255); delay(10); analogWrite(out2, 130); Serial.println(" Left Angle is = 4"); val = 100;}
                if (val == 25) {analogWrite(out2, 255); delay(10); analogWrite(out2, 120); Serial.println(" Left Angle is = 5"); val = 100;}
                if (val == 26) {analogWrite(out2, 255); delay(10); analogWrite(out2, 110); Serial.println(" Left Angle is = 6"); val = 100;}
                if (val == 27) {analogWrite(out2, 255); delay(10); analogWrite(out2, 100); Serial.println(" Left Angle is = 7"); val = 100;}  
                            
	}
	if(Serial.available()) {
		//JSN270.print((char)Serial.read());
	}
}
