# Cách kết nối robot ev3  --> thông qua WinSCP hoặc filezilla --> nhập user: passwork = robot: maker --> port = 22?  --> vào terminal nhập lệnh ssh robot@ev3dev
# để kết nối đến ev3, nhập password -> xong chạy file robot.py chứa lệnh thực thi đã viết sau khi copy vào bộ nhớ của ev3 bằng lệnh python3 robot.pypy
#!/usr/bin/env python3
from ev3dev.ev3 import LargeMotor
import time

# Initialize the motor connected to port A
motorA = LargeMotor('outA')

# Define the voltages to test (in percentage)
voltages = [100, 80, 60, 40, 20, -20, -40, -60, -80, -100]

try:
    # Loop through each voltage value
    for vol in voltages:
        # Record the start time and initial position
        timeStart = time.time()
        startPos = motorA.position

        # Create a unique filename for each voltage
        filename = "data_{}.txt".format(vol)
        file = open(filename, "w")

        # Run the motor with the specified voltage
        motorA.run_direct(duty_cycle_sp=vol)

        # Collect data for 1 second
        while True:
            # Calculate the elapsed time
            timeNow = time.time() - timeStart

            # Get the current position and speed of the motor
            currentPos = motorA.position - startPos  # Relative position
            currentSpeed = motorA.speed

            # Write the data to the file: time (s), angle (deg), speed (deg/s)
            file.write("{:.4f} {:.4f} {:.4f}\n".format(timeNow, currentPos, currentSpeed))

            # Stop after 1 second
            if timeNow > 1:
                motorA.stop(stop_action='brake')  # Stop the motor
                time.sleep(5)  # To let the Beginning speed return to 0 after each time runrun
                break

        # Close the file
        file.close()

except Exception as e:
    # Handle any errors that occur
    raise e

finally:
    # Ensure the motor stops and files are closed
    motorA.stop(stop_action='brake')
    if 'file' in locals():
        file.close()