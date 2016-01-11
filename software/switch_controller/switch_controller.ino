
#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>


const char* ssid     = "your network ssid";
const char* password = "your password";
IPAddress ip(192, 168, 1, 71);    
IPAddress gateway(192,168,1,1);
IPAddress subnet(255,255,255,0);

ESP8266WebServer server(80);

int relay = 10;
int button = 11;
int val = 0;
int temp = 0;
String webString = "";

void handle_root() {
  server.send(200, "text/plain", "Hello. I am a mains relay. /on or /off");
  delay(100);
}

void setup(void)
{
  pinMode(relay, OUTPUT);
  pinMode(button, INPUT);

  Serial.begin(115200);


  WiFi.begin(ssid, password);
  WiFi.config(ip, gateway, subnet);
  Serial.print("\n\r \n\rWorking to connect");

  // Wait for connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

  server.on("/", handle_root);

  server.on("/off", [](){
    relayOff();
    webString = 'Off';
    server.send(200, "text/plain", webString);
  });

  server.on("/on", [](){
    relayOn();
    webString = 'On';
    server.send(200, "text/plain", webString);
  });

  server.begin();
  Serial.println("HTTP server started");
}

void loop(void)
{
  server.handleClient();
  checkButton();
}

void relayOn(){
  digitalWrite(relay, HIGH);
  val = HIGH;
}

void relayOff(){
  digitalWrite(relay, LOW);
  val = LOW;
}

void checkButton(){

  int current = digitalRead(button);

  if (current == HIGH && temp != current){

    if (val == HIGH){
      relayOff();
    }

    if (val == LOW){
      relayOn();
    }

    temp = current;
  }

  if (current == LOW && temp != current){
    temp = current;
  }

}
