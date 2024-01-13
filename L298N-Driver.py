#L298N Driver code
#This works but very inefficient so I will buy a TMC driver instead.
import time
import board
from digitalio import DigitalInOut, Direction

# Define the pins connected to the L298N
IN1 = DigitalInOut(board.GP0)
IN1.direction = Direction.OUTPUT
IN2 = DigitalInOut(board.GP1)
IN2.direction = Direction.OUTPUT
IN3 = DigitalInOut(board.GP2)
IN3.direction = Direction.OUTPUT
IN4 = DigitalInOut(board.GP3)
IN4.direction = Direction.OUTPUT

# Define the sequence of signals for one motor revolution
sequence = [
    [1,0,0,0],#1
    [1,0,1,0],#13
    [0,0,1,0],#3
    [0,1,1,0],#23
    [0,1,0,0],#2
    [0,1,0,1],#24
    [0,0,0,1],#4
    [1,0,0,1]#41  
]

def set_pins(pins):
    IN1.value = pins[0]
    IN2.value = pins[1]
    IN3.value = pins[2]
    IN4.value = pins[3]

def rotate_motor(steps):
    for i in range(steps):
        for pins in sequence:
            set_pins(pins)
            #time.sleep(0.00000001)  # Adjust delay to control motor speed
            

# Rotate the motor for 512 steps (replace with the number of steps you want)
rotate_motor(50000)


