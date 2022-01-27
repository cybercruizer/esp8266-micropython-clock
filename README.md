# esp8266-micropython-clock
The original of this project is:
- https://randomnerdtutorials.com/esp32-ntp-client-date-time-arduino-ide/

#Library used:
- TM1637 from https://github.com/mcauser/micropython-tm1637

#Hardware list:
- Wemos D1 Mini
- TM1637 clock seven segment diplay
- Jumper wires

#Wiring :
- WeMos D1 Mini -- 4 Digit Display
- D1 (GPIO5) ----- CLK
- D2 (GPIO4) ----- DIO
- 5v ------------- VCC
- G -------------- GND

#Features:
- Internet connection detector
- NTP Client
- Clock 24H format
- Scroll Date
- Syncronizing after 5 hr

thank you ... @anurkholis
