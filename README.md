# HeartRatePi
## A simple heart rate monitor on Raspberry Pi 3 for Geonaute BLE (Bluetooth Low Engergy) chest band.

![Devices](https://drive.google.com/file/d/0B2hzR9sLs37CRW9sS2F1Q0d1cnc/view?usp=sharing)
![GUI](https://drive.google.com/file/d/0B2hzR9sLs37CZGd4UUJqUGJtQ00/view?usp=sharing)

  * GUI:  
  Using **tkinter** module, Python's build-in standard GUI package. Additional PIL package for Image & ImageTk.  
```
sudo pip3 install pillow
```

  * BLE:  
  **Bluez** module is requied for **gatttool** and **bluetoothctl**.  

```
sudo apt-get install bluez
```
  bluetoothctl is used to issue a bluetooth controller power cycle before every connection, just in case.

  * Manipuilate BLE with **pexpect**:  
> - Pexpect is a pure Python module for spawning child applications; controlling them; and responding to expected patterns in their output. 
> - Pexpect works like Don Libes’ Expect Pexpect allows your script to spawn a child application and control it as if a human were typing commands.

  * Test mode:  
  Run with parameter x for demo without an actual BLE device for development. 
  

## Reference:

* [Tutorial: BLE Pairing the Raspberry Pi 3 Model B with Hexiwear](https://mcuoneclipse.com/2016/12/19/tutorial-ble-pairing-the-raspberry-pi-3-model-b-with-hexiwear)
* [An Introduction to Tkinter](http://effbot.org/tkinterbook)
* [GATT Overview](https://www.bluetooth.com/specifications/gatt/generic-attributes-overview)
