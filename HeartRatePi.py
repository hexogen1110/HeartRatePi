import tkinter as tk	# For python 3.4 and above
import pexpect
import time

# Device
# 62:80:E1:00:0E:6F Geonaute BLE HRM
DEVICE = "62:80:E1:00:0E:6F"

#===========================================
# Connect /Disconnect
#===========================================
def Connect():
	global bConnected, ConncetBtn, DisconncetBtn, child

	if bConnected == False:
		# Start connection clean
		child2 = pexpect.spawn("bluetoothctl")
		child2.sendline("power off")
		time.sleep(2)
		child2.sendline("power on")
		child2.sendline("exit")	
		
		# Run gatttool interactively.
		print("Run gatttool...")
		child = pexpect.spawn("gatttool -I")
		
		# Connect to the device.
		print("Connecting to "+ DEVICE)
		child.sendline("connect {0}".format(DEVICE))
		child.expect("Connection successful", timeout=30)
		print("Connected!")
		bConnected = True
		ConncetBtn.config(state=tk.DISABLED)
		DisconncetBtn.config(state=tk.NORMAL)
		StartMonitorBtn.config(state=tk.NORMAL)
		
def Disconnect():
	global bConnected, ConncetBtn, DisconncetBtn, child
	
	if bConnected == True:

		child.sendline("disconnect")
		child.sendline("quit")
		print("Disconnected!")
		bConnected = False
		ConncetBtn.config(state=tk.NORMAL)
		DisconncetBtn.config(state=tk.DISABLED)
		
#===========================================
# Start/ stop Monitor
#===========================================	
def StartMonitor():
	global bMonitoring, child, StartMonitorBtn
	
	if bConnected == True:
		bMonitoring = True
		print("StartMonitor!")
		StartMonitorBtn.config(state=tk.DISABLED)
		StopMonitorBtn.config(state=tk.NORMAL)
		# Send a command to init a periodically HR report from BLE device
		child.sendline("char-write-req 17 0100")
		MainWin.after(1000,MonitorEvent)
		
		
def StopMonitor():	
	global child, bMonitoring, HRValueLabel
	# Send a command to stop a periodically report from BLE device
	if bMonitoring == True:
		bMonitoring = False
		StartMonitorBtn.config(state=tk.NORMAL)
		StopMonitorBtn.config(state=tk.DISABLED)		
		child.sendline("char-write-req 17 0000")
		HRValueLabel.config(text="---")
		HRValueLabel.update_idletasks()
		print("Stop Monitor!")
		
#===========================================
# MonitorEvent
#===========================================	
def MonitorEvent():
	global child, HRValueLabel, MainWin
	
	try:
		if bMonitoring == False or bConnected == False:
			print("bMonitoring == False or bConnected == False")
			MainWin.after(1000,None)
	except:
		return
		
	if bMonitoring == True and bConnected == True:
		print("Monitor Event Start!")
		# Listen to the client
		child.expect("Notification handle = 0x0016 value: 06 ", timeout=5)
		child.expect(" \r\n", timeout=5)
		HR_Value = int(child.before,16)
		print("HR: {}".format(HR_Value))
		# Update the HR value
		HRValueLabel.config(text=str(HR_Value))
		HRValueLabel.update_idletasks()
		MainWin.after(1000,MonitorEvent)

#===========================================
# GUI
#===========================================
def InitGUI():
	global HRValueLabel, child, MainWin, ConncetBtn, DisconncetBtn, StartMonitorBtn, StopMonitorBtn
	# Setup main window
	MainWin=tk.Tk()
	MainWin.title("HR Monitor Pi")
	MainWin.resizable(0, 0) #Don't allow resizing in the x or y direction
	
	HRLabel=tk.Label(MainWin, text="Current HeartRate:")
	HRLabel.grid(column=0,row=0)

	HRValueLabel=tk.Label(MainWin, text="---",)
	HRValueLabel.config(font=("Courier", 26))
	HRValueLabel.grid(column=0,row=1)

	ConncetBtn=tk.Button(MainWin, text="Conncet Device", command=Connect)
	ConncetBtn.grid(column=0,row=2)

	DisconncetBtn=tk.Button(MainWin, text="Disconnect Device", command=Disconnect, state=tk.DISABLED)
	DisconncetBtn.grid(column=1,row=2)

	StartMonitorBtn=tk.Button(MainWin, text="Start Monitoring", command=StartMonitor, state=tk.DISABLED)
	StartMonitorBtn.grid(column=0,row=3)
	
	StopMonitorBtn=tk.Button(MainWin, text="Stop Monitoring", command=StopMonitor, state=tk.DISABLED)
	StopMonitorBtn.grid(column=1,row=3)
	
	ExitBtn=tk.Button(MainWin, text="Exit", command=Quit)
	ExitBtn.grid(column=2,row=3)

	return MainWin
	
def Quit():
	MainWin.destroy()
#===========================================
if __name__ == '__main__':

	# Global variable declaration
	global bConnected, bMonitoring
	bConnected = False
	bMonitoring = False
	
	MainWin = InitGUI()

	MonitorEvent()
	MainWin.mainloop()
	