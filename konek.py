def connect():
    import network
 
    ssid = "SSID" #change with your wifi SSID
    password = "password" #change with your wifi password
 
    station = network.WLAN(network.STA_IF)
 
    if station.isconnected() == True:
        print("Sudah Konek")
        print(station.ifconfig(),"ssid:",ssid)
 
    station.active(True)
    station.connect(ssid, password)
 
    while station.isconnected() == False:
        pass
 
    print("Konek sukses")
    print(station.ifconfig())
