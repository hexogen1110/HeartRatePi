# Python script to set the time on the Hexiwear
import pexpect
import time
from time import gmtime, strftime
 
print("---------------------")
print("Setting linux time")
print("local time: "),
print(time.ctime())
unixTime = int(time.time())
print("secs since 1970: "),
print(int(unixTime))
print("---------------------")
 
DEVICE = "00:32:40:08:00:12"
 
# Run gatttool interactively.
print("Running gatttool...")
child = pexpect.spawn("gatttool -I")
 
# Connect to the device.
print("Connecting to"),
print(DEVICE),
child.sendline("connect {0}".format(DEVICE))
child.expect("Connection successful", timeout=5)
print("Connected!")
 
# Write local time
command = "char-write-req 61 0304{0:02x}{1:02x}{2:02x}{3:02x}0000000000000000000000000000".format(unixTime&0xff, (unixTime>>8)&0xff, (unixTime>>16)&0xff, (unixTime>>24)&0xff)
print(command)
child.sendline(command)
child.expect("Characteristic value was written successfully", timeout=10)
 
print("done!")