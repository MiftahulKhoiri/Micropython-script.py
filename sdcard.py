
#Setup SD card for use as filesystem
from machine import SPI, Pin
import sdcard, uos
sd_spi = SPI(1,sck=Pin(14,Pin.OUT), mosi=Pin(15,Pin.OUT), miso=Pin(12,Pin.OUT))
sd = sdcard.SDCard(sd_spi, Pin(13,Pin.OUT))

print(sd)

#Start using SD card
vfs=uos.VfsFat(sd)
print("vfs is type: ",vfs)
uos.mount(vfs, "/sd")

print("Size: {} MB".format(sd.sectors/2048))

lijst=uos.listdir("/sd")
print("information directory: \n",lijst)
f=open("/sd/test.txt","w")
for i in range(5):
    f.write(str(i)+str(i+1)+str(i+2)+str(i+3)+"\n")
f.close()
f=open("/sd/test.txt","r")
filetje=f.read()
print("contents file f:\n",filetje)
f.close()

uos.umount("/sd")  #uncomment to hide /sd contents