import serial
import csv, time
try:
    ser = serial.Serial("COM4", 115200) # change your respective serial port with COM4 and serial rate with 115200.
    serial_try = True
except:
    # if no serial communicating device is detected then program will show error for 2 seconds.
    serial_try = False
    print('Failed to connect to serial port')
    time.sleep(2)
    exit()
# create a file name data.csv
f2 = open('data.csv', 'w')
writer = csv.writer(f2)
writer.writerow(['acc_x', 'acc_y', 'acc_z', 'gyro_x', 'gyro_y','gyro_z','temperature']) 

while serial_try:
    # this loop will look for seial data and will save it to csv file
    try:
        raw_data = str(ser.readline())
        data = raw_data[2:-5]
        split_data = data.split(',')
        result = time.localtime(time.time())
        acc_x = split_data[0]
        acc_y = split_data[1]
        acc_z = split_data[2]
        gyro_x = split_data[3][1:]
        gyro_y = split_data[4]
        gyro_z = split_data[5]
        temperature = split_data[6]
        writer.writerow([acc_x, acc_y, acc_z, gyro_x, gyro_y, gyro_z, temperature]) 
        print(acc_x, acc_y, acc_z, gyro_x, gyro_y, gyro_z, temperature)

    except:
        print('Error!')
