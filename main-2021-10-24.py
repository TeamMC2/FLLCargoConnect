'''
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor,
from pybricks.parameters import Port, Direction, Color, Stop, Button
from pybricks.robotics import DriveBase
from pybricks.tools import wait

left = Motor(Port.C, Direction.COUNTERCLOCKWISE)
right = Motor(Port.D)

top_gear = Motor(Port.B, Direction.COUNTERCLOCKWISE, [[12,20],[4,4]], False)
wheel_diameter = 56
axle_track = 126

robot = DriveBase(left, right, wheel_diameter, axle_track)
#top_gear.reset_angle(45)
top_gear.run_target(80, 0)

def mission_one():
    robot.drive(500, 0)
    wait(1000)
    robot.drive(300, -45)
    wait(1000)
    robot.drive(-300, 45)
    wait(1000)
    robot.drive(-500, 0)
    wait(1000)
   
#mission_one()


def line_follow_until_color(line_sensor_right, line_sensor_left, drive_speed, proportional_gain, stop_color):
    # Calculate the light threshold. Choose values based on your measurements.
    BLACK = 10
    WHITE = 95
    threshold = (BLACK + WHITE) / 2

    while line_sensor_right.color() != stop_color:
        print(line_sensor_right.color())
        # Calculate the deviation from the threshold.aA
        deviation = line_sensor_left.reflection() - threshold

        # Calculate the turn rate.
        turn_rate = proportional_gain * deviation

        # Set the drive base speed and turn rate.
        robot.drive(drive_speed, turn_rate)

        # You can wait for a short time or do other things in this loop.
        wait(10)


line_follow_until_color(
    line_sensor_right = ColorSensor(Port.E), 
    line_sensor_left = ColorSensor(Port.F), 
    drive_speed = 150,
    proportional_gain = 1.2,
    stop_color=Color.NONE)

robot.turn(20)
robot.drive(400,0)
wait(500)
robot.drive(-500,0)
wait(1200)
robot.turn(-90)
robot.turn(-120)
robot.drive(500,0)
wait(1250)

robot.stop()

#line_follow_until_distance(
#    line_sensor_right = ColorSensor(Port.F), 
#    drive_speed = 150,
#    proportional_gain = 1.2,
#    distance=1500)
'''
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction, Color, Stop, Button
from pybricks.robotics import DriveBase
from pybricks.tools import wait

bottom_motor_mission_1 = Motor(
        Port.A,
        positive_direction=Direction.CLOCKWISE, 
        gears=[[12,20],[20,12]], 
        reset_angle=True)

top_motor_mission_1 = Motor(
        Port.B,
        positive_direction=Direction.CLOCKWISE, 
        gears=[[12,20]], 
        reset_angle=True)

# left = Motor(Port.C, Direction.COUNTERCLOCKWISE)
left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.D)
bottom_motor = Motor(Port.A)

top_motor = Motor(Port.B)
line_sensor_right = ColorSensor(Port.F)
line_sensor_left = ColorSensor(Port.E)

wheel_diameter = 56
axle_track = 126

straight_speed = 1000
straight_acceleration = 540
turn_rate = 390
turn_acceleration =  250

bottom_motor_speed = 100
top_motor_speed = 10

# Initialize the hub.
hub = PrimeHub()
#hub.system.set_start_button(Button.CENTER)
hub.system.set_stop_button(Button.BLUETOOTH)

robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)
robot.settings(straight_speed, straight_acceleration, turn_rate, turn_acceleration)
# this function moves robot to push blue box out of mat and back up to home

# Display test commands
#hub.display.text('A')
hub.display.pixel(0, 0, brightness=20)
hub.display.pixel(0, 1, brightness=40)
hub.display.pixel(0, 2, brightness=60)
hub.display.pixel(0, 3, brightness=80)
hub.display.pixel(0, 4, brightness=100)
wait(1000)

'''
# Calculate the light threshold. Choose values based on your measurements.
BLACK = 10
WHITE = 95
threshold = (BLACK + WHITE) / 2
# Set the drive speed at 100 millimeters per second.
DRIVE_SPEED = 200
# Set the gain of the proportional line controller. This means that for every
# percentage point of light deviating from the threshold, we set the turn
# rate of the drivebase to 1.2 degrees per second.
# For example, if the light value deviates from the threshold by 10, the robot
# steers at 10*1.2 = 12 degrees per second.
PROPORTIONAL_GAIN = 2.0
DISTANCE = 1535
# Start following the for a DISTANCE.
while robot.distance() < DISTANCE:
    #print(line_sensor.reflection(), line_sensor.color(), line_sensor.hsv())
    # Calculate the deviation from the threshold.
    deviation = line_sensor.reflection() - threshold
    # Calculate the turn rate.
    turn_rate = PROPORTIONAL_GAIN * deviation
    # Set the drive base speed and turn rate.
    robot.drive(DRIVE_SPEED, turn_rate)
    # You can wait for a short time or do other things in this loop.
    wait(10)
   '''

def monitor():
  solution = 0
  NumberOfSolutions = 6
  hub.display.number(solution)
  hub.speaker.beep(frequency=200, duration=100)
  while True:
    pressed = []
    while not any(pressed):
      pressed = hub.buttons.pressed()
      wait(10)
    
    # Wait for all buttons to be released.
    while any(hub.buttons.pressed()):
      wait(10)
    
    # Increment selection number based on button pressed.
    if Button.LEFT in pressed: # check if the left button is pressed
        hub.speaker.beep(frequency = 100, duration= 100)
        solution += -1 # If the left button was pressed, decrement the solution number by 1

        if solution < 0: # if the solution number is less than 0, wrap the number around to the max number. This way only numbers 0 to NumberOfSolutions (initially 15) is used.
            solution = NumberOfSolutions # Set solution number to the max number
        hub.display.number(solution) # Display the solution number on the PrimeHub
            #pressed.clear() # clear the array storing the button press to keep everything tidy.
    elif Button.RIGHT in pressed:
        hub.speaker.beep(frequency = 300, duration= 100)
        solution += 1
        if solution > NumberOfSolutions:
          solution = 0
        hub.display.number(solution)
        #Button.pressed.clear()
    elif Button.CENTER in pressed:
    # If center button is pressed, run the selected mission
      # Python switch statement syntax
      if solution == 0: # run solution 0
        #solution_0() # is there a solution 0?
        hub.speaker.beep(frequency=100, duration=100)
        hub.light.blink(Color.RED, [500, 500])
        wait(2000)
        mission_zero()
        # tried to break the loop but it doesn't interrupt
        #pressed2 = []
        #while not any(pressed2):
        #  pressed2 = hub.buttons.pressed()
        #  print("broke before this")
        #  mission_zero()
        hub.light.on(Color.BLUE)
      elif solution == 1: # run solution 1
        #solution_1()
        hub.speaker.beep(frequency=300, duration=100)
        hub.light.blink(Color.ORANGE, [500, 500])
        wait(2000)
        hub.light.on(Color.BLUE)
        mission_one()
        robot.stop()
        
      elif solution == 2: # run solution 2
        #solution_2() #corresponded with 3 instead of 2
        hub.speaker.beep(frequency=500, duration=100)
        hub.light.blink(Color.YELLOW, [500, 500])
        wait(500)
        hub.light.on(Color.BLUE)
        # Add the rest of the solutions
        mission_2()
      elif solution == 3:
        #solution_3()
        hub.speaker.beep(frequency=700, duration=100)
        hub.light.blink(Color.GREEN, [500, 500])
        wait(500)
        hub.light.on(Color.BLUE)
        mission_3()
      elif solution == 4:
       # solution_4()
        hub.speaker.beep(frequency=900, duration=100)
        hub.light.blink(Color.CYAN, [500, 500])
        #wait(2000)
        hub.light.on(Color.BLUE)
        mission_4()
      elif solution == 5:
        # solution_4()
        hub.speaker.beep(frequency=900, duration=100)
        hub.light.blink(Color.CYAN, [500, 500])
        #wait(2000)
        hub.light.on(Color.BLUE)
        run_test()  
      elif solution == 6:
        hub.speaker.beep(frequency=900, duration=100)
        hub.light.blink(Color.CYAN, [500, 500])
        #wait(2000)
        hub.light.on(Color.BLUE)
        run_3_next()  
      else :
        print("lost!")
'''
      elif solution == 6:
        solution_6()
      elif solution == 7:
        solution_7()
      elif solution == 8:
        solution_8()
      elif solution == 9:
        solution_9()
      elif solution == 10:
        solution_10()
      elif solution == 11:
        solution_11()
      elif solution == 12:
        solution_12()
      elif solution == 13:
        solution_13()
      elif solution == 14:
        solution_14()
      elif solution == 15:
        solution_15()
      else :
          print("lost!")
        # default solution, what to do if a solution number is not implemented above?
        '''





def pid_line_follow(sensor_to_track, side_of_line, drive_speed, critical_gain, critical_period, stop_color):
    # sensor_to_track - need to be left or right'
    # side_of_line - need to be 'left or right'

    # Calculate the light threshold. Choose values based on your measurements.
    BLACK = 10
    WHITE = 95
    target = (BLACK + WHITE) / 2
    # PID contol for line follwing
    # Tune rate is in degrees / second

    # Ziegler-nicholes Method Gail Vaules
    # Finding the gains Kp, Ki, and Kd - turning
    # Step 1: Set the Gains Ki and Kd to zero (making it only proportional)
    # Step 2: Start w/ Kp as a SMALL value and increase Kp until the output the robot
    #           starts to oscillate. - this is Kc
    # Step 3: Measure the time period of the oscillation at that Kp value - this is Pc
    # critical_gain = 2   # Kc
    # critical_period = .5   # Pc
    Previous_Error = 0
    Integral = 0
    DeltaT = 1/100
    '''
    # use this for calibration
    PROPORTIONAL_GAIN = 3.5
    INTEGRAL_GAIN = 0
    Derivative_GAIN = 0
    '''
    PROPORTIONAL_GAIN = 0.6 * critical_gain  # Kp
    INTEGRAL_GAIN = 2 * PROPORTIONAL_GAIN / critical_period # Ki
    Derivative_GAIN = PROPORTIONAL_GAIN * critical_period / 8  #Kd
    
    if sensor_to_track == "right":
        print("sensor to track is right ")
        watch = line_sensor_left
        track = line_sensor_right
    else :
        print("sensor to track is left ")
        watch = line_sensor_right
        track = line_sensor_left      

    if side_of_line == "right":
        print("side of line is right")
        direction = -1
    else :
        print("side of line is left")
        direction = 1
    count = 0

    print(stop_color)
    while watch.color() != stop_color:

        print(watch.color())
        Error = track.reflection() - target
        Integral = Integral + (Error * DeltaT)
        Derivative = (Error - Previous_Error) /DeltaT
        Previous_Error = Error

        # Calculate the turn rate.
        p = PROPORTIONAL_GAIN * Error
        i = INTEGRAL_GAIN * Error
        d = Derivative_GAIN * Error

        turn_rate = (p + i + d) * direction
        print(turn_rate)
        # Set the drive base speed and turn rate.
        robot.drive(drive_speed, turn_rate)

        # You can wait for a short time or do other things in this loop.
        wait(10)
        count = count +1
        #print(count, turn_rate, Error, line_sensor_right.reflection())

def pid_line_follow_dist(sensor_to_track, side_of_line, drive_speed, critical_gain, critical_period, stop_distance):
    # sensor_to_track - need to be left or right'
    # side_of_line - need to be 'left or right'

    # Calculate the light threshold. Choose values based on your measurements.
    BLACK = 10
    WHITE = 95
    target = (BLACK + WHITE) / 2
    # PID contol for line follwing
    # Tune rate is in degrees / second

    # Ziegler-nicholes Method Gail Vaules
    # Finding the gains Kp, Ki, and Kd - turning
    # Step 1: Set the Gains Ki and Kd to zero (making it only proportional)
    # Step 2: Start w/ Kp as a SMALL value and increase Kp until the output the robot
    #           starts to oscillate. - this is Kc
    # Step 3: Measure the time period of the oscillation at that Kp value - this is Pc
    # critical_gain = 2   # Kc
    # critical_period = .5   # Pc
    Previous_Error = 0
    Integral = 0
    DeltaT = 1/100
    '''
    # use this for calibration
    PROPORTIONAL_GAIN = 3.5
    INTEGRAL_GAIN = 0
    Derivative_GAIN = 0
    '''
    PROPORTIONAL_GAIN = 0.6 * critical_gain  # Kp
    INTEGRAL_GAIN = 2 * PROPORTIONAL_GAIN / critical_period # Ki
    Derivative_GAIN = PROPORTIONAL_GAIN * critical_period / 8  #Kd
    stop_distance = abs(stop_distance)


    if sensor_to_track == "right":
        print("sensor to track is right ")
        watch = line_sensor_left
        track = line_sensor_right
    else :
        print("sensor to track is left ")
        watch = line_sensor_right
        track = line_sensor_left      

    if side_of_line == "right":
        print("side of line is right")
        direction = -1
    else :
        print("side of line is left")
        direction = 1

    count = 0
    robot.reset()
    while robot.distance() <= stop_distance:

        #print(line_sensor_right.reflection(), line_sensor_right.color(), line_sensor_right.hsv())
        Error = track.reflection() - target
        Integral = Integral + (Error * DeltaT)
        Derivative = (Error - Previous_Error) /DeltaT
        Previous_Error = Error

        # Calculate the turn rate.
        p = PROPORTIONAL_GAIN * Error
        i = INTEGRAL_GAIN * Error
        d = Derivative_GAIN * Error

        turn_rate = (p + i + d) * direction

        # Set the drive base speed and turn rate.
        robot.drive(drive_speed, turn_rate)

        # You can wait for a short time or do other things in this loop.
        wait(10)
        count = count +1
        #print(count, turn_rate, Error, line_sensor_right.reflection())

def run_test():
  print("start test")
  bottom_motor_mission_1 = Motor(
        Port.A,
        positive_direction=Direction.CLOCKWISE, 
        gears=[[12,20],[20,12]], 
        reset_angle=True)
  bottom_motor_mission_1.reset_angle(0)
  bottom_motor_mission_1.run_target(100,90)
  print("end test")

def module1_home():
    bottom_motor_speed = -500
    bottom_motor_mission_1.run_until_stalled(bottom_motor_speed, then=Stop.COAST, duty_limit=None)
    print("home finished")
def mission_zero():
    
    wait(10)
    hub.speaker.beep(frequency=1000, duration=200)
    hub.speaker.beep(frequency=100, duration=500)

def mission_one():
    bottom_motor_mission_1.reset_angle(0)
    bottom_motor_mission_1.run_target(80,-10) # was 80, 40
    straight_speed = 900
    robot.reset()
    robot.straight(165)
    
    pid_line_follow_dist(
      sensor_to_track = "right", 
      side_of_line = "left",
      drive_speed = 150, 
      critical_gain = 1, 
      critical_period = 10, 
      stop_distance = 450)
    
    robot.straight(180)  # was 160
    robot.straight(-10)
    # trucks latched

    bottom_motor_mission_1.run_target(160,90) #Was (80, 40)
    #wait_until_button()
    #wait_until_button()
    #knock-down first part of bridge
    #robot.straight(140)
    #pid_line_follow(sensor_to_track = "right", side_of_line = "left", drive_speed = 100, critical_gain = 1, 
    #    critical_period = 10, stop_color = Color.NONE)
    pid_line_follow_dist(
      sensor_to_track = "right", 
      side_of_line = "left",
      drive_speed = 150, 
      critical_gain = 1, 
      critical_period = 10, 
      stop_distance = 260)
    robot.stop()
    wait_until_button()

    bottom_motor_mission_1.run_target(80,45) #Goes down to pass over trucks
    wait_until_button()

    #robot.straight(200) # was 400
    pid_line_follow_dist(
      sensor_to_track = "right", 
      side_of_line = "left",
      drive_speed = 150, 
      critical_gain = 1, 
      critical_period = 10, 
      stop_distance = 200)
    robot.stop()
    wait_until_button()

    bottom_motor_mission_1.run_target(80,90) #raises arm to clear drawbridge
    wait_until_button()

    robot.straight(130) #passes bridge
    #wait_until_button()

    bottom_motor_mission_1.run_target(80,45) #lowers arm to hit bridge
    #wait_until_button()
    #robot.straight(-80)
    #wait_until_button()

    robot.straight(-40)
    #wait_until_button()

    robot.turn(60)# turns into cargo connect circle
  
    
    
    top_motor_mission_1.reset_angle(0)
    top_motor_mission_1.run_target(80,90)

    
    #bottom_motor_mission_1.run_target(80,90)
    robot.straight(-50) #clearing circle #100
    #wait_until_button()
    bottom_motor_mission_1.run_target(80,0)
    
  

    robot.reset()
    robot.turn(20) #was 155
    #wait_until_button()
    robot.drive(-200,0)
    wait(1000)
    robot.straight(20)
    robot.turn(90) # solves mission 7 lift cargo on dock
    #wait_until_button()

    #robot.straight(-150)
    #robot.turn(-30)

    #top_motor_mission_1.reset_angle(0)
    top_motor_mission_1.run_target(100,45)
    #bottom_motor_mission_1.reset_angle(0)
    bottom_motor_mission_1.run_target(100,75)
    robot.straight(-440)
    robot.straight(20)
    robot.turn(-75)
    #wait_until_button()
    robot.drive(-150, 0)
    wait(1400)
    #wait_until_button()
    robot.turn(-40)
    robot.straight(50)
    #robot.turn(-30)
    #robot.straight(250)
    #bottom_motor_mission_1.run_target(80,0)
    #wait_until_button()
    pid_line_follow_dist(sensor_to_track = "left", side_of_line = "left",drive_speed = 75, critical_gain = 1, 
          critical_period = 10, stop_distance = 200)
    bottom_motor_mission_1.run_target(100,0)
    pid_line_follow_dist(sensor_to_track = "left", side_of_line = "left",drive_speed = 100, critical_gain = 1, 
          critical_period = 10, stop_distance = 45)
    robot.stop()      
    bottom_motor_mission_1.run_target(100,45)
    robot.straight(-360)
    bottom_motor_mission_1.run_target(100,0)

    pid_line_follow_dist(sensor_to_track = "left", side_of_line = "left",drive_speed = 150, critical_gain = 1, 
          critical_period = 10, stop_distance = 420)
    robot.stop()
        
    bottom_motor_mission_1.run_target(100,45)

    robot.straight(-400)
    robot.turn(50)
    robot.straight(400)
    robot.turn(40)
    robot.straight(150)
    pid_line_follow_dist(sensor_to_track = "left", side_of_line = "left",drive_speed = 150, critical_gain = 1, 
          critical_period = 10, stop_distance = 1000)
    robot.stop()      
    robot.straight(300)
    
def mission_2():
  print("Starting Mission 2")
  print("Line follow until black")
  pid_line_follow(
        sensor_to_track = "right", 
        side_of_line = "left",
        drive_speed = 150, 
        critical_gain = 1, 
        critical_period = 10, 
        stop_color = Color.NONE)
  print("Turn 15 degrees")
  robot.turn(15)
  print("Drive straight ")
  robot.straight(130)
  top_motor_mission_1.reset_angle(0)
  top_motor_mission_1.run_target(80,105)
  # Now the robot is in front of the generator.  
  robot.turn(-10)
  robot.straight(-190)
  
  robot.turn(-90)
  robot.straight(30)
  # Now the robot is in front of the back of the plane.
  top_motor_mission_1.run_target(160,0)
  robot.turn(-120)
  robot.straight(400)
  robot.stop()

def mission_3():
  robot.turn(50)
  robot.straight(400)
  robot.turn(40)
  robot.straight(150)
  pid_line_follow_dist(sensor_to_track = "left", side_of_line = "left",drive_speed = 150, critical_gain = 1, 
        critical_period = 10, stop_distance = 1000)
  robot.stop()      
  robot.straight(300)
  '''
  top_motor_mission_1.reset_angle(0)
  top_motor_mission_1.run_target(100,45)
  bottom_motor_mission_1.reset_angle(0)
  bottom_motor_mission_1.run_target(100,45)
  robot.straight(-440)
  robot.straight(20)
  robot.turn(-75)
  #wait_until_button()
  robot.drive(-150, 0)
  wait(1400)
  #wait_until_button()
  robot.turn(-40)
  robot.straight(50)
  #robot.turn(-30)
  #robot.straight(250)
  #bottom_motor_mission_1.run_target(80,0)
  #wait_until_button()
  pid_line_follow_dist(sensor_to_track = "left", side_of_line = "left",drive_speed = 75, critical_gain = 1, 
        critical_period = 10, stop_distance = 200)
  bottom_motor_mission_1.run_target(100,0)
  pid_line_follow_dist(sensor_to_track = "left", side_of_line = "left",drive_speed = 100, critical_gain = 1, 
        critical_period = 10, stop_distance = 45)
  robot.stop()      
  bottom_motor_mission_1.run_target(100,45)
  robot.straight(-360)
  bottom_motor_mission_1.run_target(100,0)

  pid_line_follow_dist(sensor_to_track = "left", side_of_line = "left",drive_speed = 150, critical_gain = 1, 
        critical_period = 10, stop_distance = 420)
  robot.stop()
      
  bottom_motor_mission_1.run_target(100,45)

  robot.straight(-400)
  '''
  '''
  robot.straight(30)
  robot.turn(10)
  robot.straight(20)
  robot.turn(80)
  robot.straight(450)
  pid_line_follow_dist(sensor_to_track = "left", side_of_line = "left",drive_speed = 150, critical_gain = 1, 
        critical_period = 10, stop_distance = 350)
  robot.stop()
  '''
def mission_4():
  wait(600)
  #robot.settings(400, straight_acceleration, turn_rate, turn_acceleration)
  robot.reset()
  top_motor.reset_angle(0)
  robot.straight(703)
  robot.turn(45)
  robot.straight(203)
  #bottom_motor.run_target(100, 180, then=Stop.HOLD, wait=True)
  top_motor.run_target(1000, 4000, then=Stop.HOLD, wait=True)
  robot.straight(-203)
  robot.turn(-87)
  robot.straight(-85)
  top_motor.run_target(1000, -100, then=Stop.HOLD, wait=True)
  top_motor.run_target(800, 4000, then=Stop.HOLD, wait=True)
  robot.turn(45)
  top_motor.run_target(800,650, then=Stop.HOLD, wait=True)
  robot.turn(-45)
  robot.straight(-85)
  top_motor.run_target(800, 2000, then=Stop.HOLD, wait=True)
  robot.turn(-57)
  #top_motor.run_target(800, 700, then=Stop.HOLD, wait=True)
  #robot.turn(-70)
  ##robot.straight(15)
  #top_motor.run_target(800, 3000, then=Stop.HOLD, wait=True)
  #robot.straight(-20)
  #robot.turn(-80)
  robot.straight(500)
  #robot.straight(400)
  '''
  pid_line_follow_dist(
        sensor_to_track = "left", 
        side_of_line = "left",
        drive_speed = -150, 
        critical_gain = 1, 
        critical_period = 10, 
        stop_distance = 300)
  '''
def run_three():
    #Robot starts at fixture with cargo and positioned at 45 degrees (450)
    robot.reset() 
    robot.straight(150)
    robot.turn(45)
    
    robot.straight(505)
    robot.turn(-10)
    '''
    pid_line_follow_dist(
        sensor_to_track = "right", 
        side_of_line = "left",
        drive_speed = 200, 
        critical_gain = 1, 
        critical_period = 10, 
        stop_distance = 600)
    robot.turn(-10)
    pid_line_follow(
        sensor_to_track = "right", 
        side_of_line = "left",
       drive_speed = 200, 
        critical_gain = 1.5, 
        critical_period = 10, 
        stop_color = Color.NONE) 
    pid_line_follow_dist(
        sensor_to_track = "right", 
        side_of_line = "left",
        drive_speed = 200, 
        critical_gain = 1, 
        critical_period = 10, 
        stop_distance = 600)
        '''
def run_3_next():
    #Robot starts at fixture with cargo and positioned at 45 degrees (450)
    robot.reset() 
    robot.straight(150)
    robot.turn(45)
    robot.straight(540)
    robot.turn(-25)
    
    pid_line_follow(
        sensor_to_track = "right", 
        side_of_line = "left",
        drive_speed = 125, 
        critical_gain = 1, 
        critical_period = 10, 
        stop_color = Color.NONE) 

    robot.stop()
    robot.turn(-70)
    #wait_until_button()
    pid_line_follow_dist(
        sensor_to_track = "right", 
        side_of_line = "right",
        drive_speed = 150, 
        critical_gain = 1, 
        critical_period = 10, 
        stop_distance = 300)
    pid_line_follow(
        sensor_to_track = "right", 
        side_of_line = "right",
        drive_speed = 150, 
        critical_gain = 1, 
        critical_period = 10, 
        stop_color = Color.NONE)
    robot.stop()
    #wait_until_button()
    robot.turn(40)
    #wait_until_button()
    robot.straight(60)
    #wait_until_button()
    robot.turn(-40)
    #wait_until_button()
    robot.straight(85)
    # droped pagej
    #wait_until_button()
    robot.straight(-85)
    #wait_until_button()
    robot.turn(40)
    #wait_until_button()
    robot.straight(-60)
    #wait_until_button()
    robot.turn(-40)
    #wait_until_button()
    robot.straight(-40)
    #wait_until_button()
    robot.turn(-150)
    #wait_until_button()
    pid_line_follow_dist(
        sensor_to_track = "left", 
        side_of_line = "right",
        drive_speed = 100, 
        critical_gain = 1, 
        critical_period = 10, 
        stop_distance = 150)
    robot.stop()
    #wait_until_button()
    robot.turn(-85)
    #wait_until_button()
    robot.stop()

    #This is the next half of run 5.
    top_motor_mission_3 = Motor(Port.B, positive_direction=Direction.CLOCKWISE, gears=[[12,24],[1,24]], reset_angle=True)
    top_motor_mission_3.reset_angle(0)
    top_motor_mission_3.run_target(1000, -80)
    robot.straight(-70)
    robot.turn(90)
    robot.straight(1000)
    top_motor_mission_3.run_target(1500, 0)



def wait_until_button():
    pressed = []
    robot.stop()
    while not any(pressed):
      pressed = hub.buttons.pressed()
      wait(10)


monitor()
'''
module1_home()
bottom_motor_rotation_angle = 90
bottom_motor_speed = 250
bottom_motor_mission_1.reset_angle(angle=None)
bottom_motor_mission_1.run_angle(bottom_motor_speed, bottom_motor_rotation_angle, then=Stop.HOLD, wait=True)
mission_one()
#bottom_motor_mission_1.run_until_stalled(bottom_motor_speed, then=Stop.COAST, duty_limit=None)
'''
