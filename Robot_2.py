from ev3dev.ev3 import LargeMotor
import time

# Initialize the motor on port A
motor = LargeMotor('outA')

# List of voltage levels to test
power_levels = [100, 80, 60, 40, 20, -20, -40, -60, -80, -100]

try:
    for power in power_levels:
        # Ensure the motor is fully stopped before adjusting power
        motor.stop(stop_action='brake')
        time.sleep(0.5)  # Short pause to ensure full stop

        # Record the starting time and initial position
        start_time = time.time()
        initial_position = motor.position  

        # Create a file to store data safely
        file_name = f"data_{power}.txt"
        with open(file_name, "w") as log_file:  

            # Apply the power setting before entering the logging loop
            motor.run_direct(duty_cycle_sp=power)

            while True:
                elapsed_time = time.time() - start_time
                current_position = motor.position - initial_position  
                current_speed = motor.speed  # Get actual motor speed

                # Write time, position, and speed to the file
                log_file.write(f"{elapsed_time:.3f} {current_position} {current_speed}\n")

                # Stop the motor after 5 seconds
                if elapsed_time > 5:
                    motor.stop(stop_action='brake')
                    break

                time.sleep(0.05)  # Adjust sampling rate if needed

except Exception as error:
    print("An error occurred:", error)

finally:
    motor.stop(stop_action='brake')  