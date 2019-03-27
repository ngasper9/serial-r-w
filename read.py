import serial, sys

ser = serial.Serial('/dev/ttyUSB1')
ser.baudrate = 9600
print("\npovezano na: {}\n".format(ser.portstr))


while 1:
    c = ser.read()
    sys.stdout.write(c)
    if c == '.':
    	print('\n')

ser.close()



