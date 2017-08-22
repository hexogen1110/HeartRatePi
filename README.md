# HeartRatePi
## A simple heart rate monitor on Raspberry Pi 3 for Geonaute BLE (Bluetooth Low Engergy) chest band.

  * GUI:  
  Using **tkinter** module, Python's build-in standard GUI package. Additional PIL package for Image & ImageTk.  
```
sudo pip3 install pil
```

  * BLE:  
  **Bluez** module is requied for **gatttool** and **bluetoothctl**.  

```
sudo apt-get install bluez
```

  * Manipuilate BLE with **pexpect**:  
> - Pexpect is a pure Python module for spawning child applications; controlling them; and responding to expected patterns in their output. 
> - Pexpect works like Don Libes’ Expect Pexpect allows your script to spawn a child application and control it as if a human were typing commands.

* Reference:

[Tutorial: BLE Pairing the Raspberry Pi 3 Model B with Hexiwear](https://mcuoneclipse.com/2016/12/19/tutorial-ble-pairing-the-raspberry-pi-3-model-b-with-hexiwear)

