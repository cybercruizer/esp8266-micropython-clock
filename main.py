# ESP8266 MicroPython Web Clock
# by Alan Wang
# Modified by Dan Anderson
# Add some toppings by @anurkholis

import tm1637,network, time, machine, konek, ntptime 
from machine import RTC,Pin

# HW-069 4 Digit 7 Segment display
tm = tm1637.TM1637(clk=Pin(5), dio=Pin(4))
#tm.numbers(00, 00, True)
tm.scroll('connecting') # 4 fps

# internal real time clock
rtc = RTC()

# wifi connection
konek.connect()
station = network.WLAN(network.STA_IF)
if station.isconnected() == True:
  tm.scroll('inet ok') # 4 fps
nextsinkron=0
# set timer
def sinkronisasi():
  rtc=RTC()
  ntptime.settime()
  waktu=rtc.datetime()
  jam=waktu[4]+7
  print("berhasil sinkronisasi")
  nextsinkron=jam+5   #sync after 5 hr later

  print("sinkronisasi selanjutnya pukul: ",nextsinkron)

sinkronisasi()

# main loop
while True:
  waktu=rtc.datetime()
  jam=waktu[4]+7
  menit=waktu[5]
  detik=waktu[6]
  tahun=waktu[0]
  bulan=waktu[1]
  tanggal=waktu[2]
  
  print(tanggal,"/",bulan, " ",jam,":",menit)
  
  #Push numbers to display with level 2 brightness 
  tm.brightness(2)
  for x in range(5):
    tm.numbers(jam, menit, True)
    time.sleep(0.5)
    tm.numbers(jam, menit, False)
    time.sleep(0.5)
  for x in range(2):
    tampil=str(tanggal)+"-"+str(bulan)+"-"+str(tahun)
    tm.scroll(tampil)
  if jam==nextsinkron and menit==0 and detik==0:
    sinkronisasi()
