import serial
import csv, time
try:
    ser = serial.Serial("COM4", 115200) # change your serial port with COM4
    serial_try = True
except:
    # gives failed to connect to serial port error if serial port is not available
    serial_try = False
    print('Failed to connect to serial port')
    time.sleep(2)
    exit()
# create a file data.csv for storing sensor values
f2 = open('data.csv', 'w')
writer = csv.writer(f2)
writer.writerow(['time (ms)','acc_x', 'acc_y', 'acc_z', 'gyro_x', 'gyro_y','gyro_z','temperature']) 

while serial_try:
    try:
        # processes raw values from arduino and store it in data.csv which we created earlier
        raw_data = str(ser.readline())
        data = raw_data[2:-5]
        split_data = data.split(',')
        time = split_data[0]
        acc_x = split_data[1]
        acc_y = split_data[2]
        acc_z = split_data[3]
        gyro_x = split_data[4][1:]
        gyro_y = split_data[5]
        gyro_z = split_data[6]
        temperature = split_data[7]
        writer.writerow([time,acc_x, acc_y, acc_z, gyro_x, gyro_y, gyro_z, temperature]) 
        print(time, acc_x, acc_y, acc_z, gyro_x, gyro_y, gyro_z, temperature)

    except:
        # if any error is found the system will show error!
        print('Error!')
