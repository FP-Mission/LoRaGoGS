from datetime import datetime
import serial

# Configure the serial connections
ser = serial.Serial(
    port='/dev/ttyS3',
    baudrate=57600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

ser.isOpen()

def send(command):
    print("~" + command)
    ser.write(("~" + command + "\r\n").encode())

send("F434.225")
send("M0")

out=""
while 1 :    
    while ser.inWaiting() > 0:
        char = ser.read(1).decode("utf-8") 
        if char == '\n':
            dt = datetime.now().strftime("%H:%M:%S")
            print(dt + " " + out)
            out = ""
        else:
            out += char