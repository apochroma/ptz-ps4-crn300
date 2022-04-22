/*
 * Created by ArduinoGetStarted.com
 *
 * This example code is in the public domain
 *
 * Tutorial page: https://arduinogetstarted.com/tutorials/arduino-ethernet-shield-2
 */

#include <SPI.h>
#include <Ethernet.h>

// replace the MAC address below by the MAC address printed on a sticker on the Arduino Shield 2
byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };

// change the IP address, subnet mask, gateway's IP address, and DNS server's IP address depending on your network
IPAddress ip(10, 10, 10, 99);
IPAddress gateway(10, 10, 10, 1);
IPAddress subnet(255, 255, 255, 0);
IPAddress myDns(8, 8, 8, 8);

#define joyX A1 // blue x axis - PAN
#define joyY A0 // yellow y axis - TILT
#define joyZ A2 // white z axis - Zoom

EthernetClient client;

int    HTTP_PORT   = 80;
String HTTP_METHOD = "GET";
char   HOST_NAME[] = "10.10.10.100";
String PATH_NAME   = "/-wvhttp-01-/control.cgi";

void setup() {
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }
 // start the Ethernet connection:
  Serial.println("Initialize Ethernet with DHCP:");
  if (Ethernet.begin(mac) == 0) {
    Serial.println("Failed to configure Ethernet using DHCP");
    // Check for Ethernet hardware present
    if (Ethernet.hardwareStatus() == EthernetNoHardware) {
      Serial.println("Ethernet shield was not found.  Sorry, can't run without hardware. :(");
      while (true) {
        delay(1); // do nothing, no point running without Ethernet hardware
      }
    }
    if (Ethernet.linkStatus() == LinkOFF) {
      Serial.println("Ethernet cable is not connected.");
    }
    // try to congifure using IP address instead of DHCP:
    Ethernet.begin(mac, ip, myDns);
  } else {
    Serial.print("  DHCP assigned IP ");
    Serial.println(Ethernet.localIP());
  }
  // give the Ethernet shield a second to initialize:
  delay(1000);
  Serial.print("connecting to ");
  Serial.print(HOST_NAME);
  Serial.println("...");
}

void makeRequest(int pValue, int xValue, int yValue, int zValue)
{
    if(client.connect(HOST_NAME, HTTP_PORT))
    {
      Serial.println("Connected to server");
      String queryString = "?pan=right&pan.speed=";
    //Serial.print(queryString); Serial.println(xValue);
      client.println(HTTP_METHOD + " " + PATH_NAME + queryString + xValue + " HTTP/1.1");
      client.println("Host: " + String(HOST_NAME));
      client.println("Connection: close");
      client.println(); // end HTTP header

      while(client.connected())
      {
        if(client.available())
        {
         // read an incoming byte from the server and print it to serial monitor:
         char c = client.read();
         Serial.print(c);
        }
      }
    }
}

void loop()
{  
  int xValue, yValue, zValue, pValue;
  // put your main code here, to run repeatedly:
  pValue = digitalRead(2); //Serial.print(" P:"); Serial.print(pValue);
  xValue = analogRead(joyX); //Serial.print(" X:"); Serial.print(xValue);
  yValue = analogRead(joyY); //Serial.print(" Y:"); Serial.print(yValue);
  zValue = analogRead(joyZ); //Serial.print(" Z:"); Serial.print(zValue);
  Serial.println();

///////////////////////////
  
  if (xValue <= 400)
  {
    makeRequest( pValue, xValue, yValue, zValue );
    //Serial.print("makeRequest with xValue: ");Serial.print(xValue);
  }  

 delay(500);
 
    while(client.connected()) {
      if(client.available()){
        // read an incoming byte from the server and print it to serial monitor:
        char c = client.read();
        Serial.print(c);
      }
    }
}
