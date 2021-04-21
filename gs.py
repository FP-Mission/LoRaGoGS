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
    dt = datetime.now().strftime("%H:%M:%S")
    print('[' + dt + "] ~" + command)
    ser.write(("~" + command + "\r\n").encode())

send("F434.225")
send("M0")
send("D")
send("V")

out=""
while 1 :    
    while ser.inWaiting() > 0:
        char = ser.read(1)
        try:
            char = char.decode() # .decode("utf-8") 
        except:
            #print(char)
            continue
        if char == '\n':
            dt = datetime.now().strftime("%H:%M:%S")

            # print('[' + dt + '] LoRaGo - ' + out)

            fields = out.split('=', 2)
            if len(fields) == 2:
                if fields[0] == 'CurrentRSSI':
                    #send("Ttest")
                    pass
                else:
                    print('[' + dt + '] LoRaGo - ' + out)


            out = ""
        else:
            out += char
