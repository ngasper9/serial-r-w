import serial
ser = serial.Serial('/dev/ttyUSB0')
ser.baudrate = 9600
print("\npovezano na: {}".format(ser.portstr))

i = 1
while i == 1:
    g = raw_input("Send: ")
    g.decode('utf-8')
    ser.write(g)
