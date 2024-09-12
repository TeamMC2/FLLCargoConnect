# This file contains the instructions for solution 1

def solution_1():
  # Do awesome stuff!
  line_follow_until_color(
    line_sensor_right = ColorSensor(Port.E), 
    line_sensor_left = ColorSensor(Port.F), 
    drive_speed = 150,
    proportional_gain = 1.2,
    stop_color=Color.NONE)

  robot.turn(20)
  robot.drive(400,0)
  wait(500)
  # Now the robot is in front of the generator.  
  robot.drive(-500,0)
  wait(1200)
  robot.turn(-90)
  # Now the robot is in front of the back of the plane.
  robot.turn(-120)
  robot.drive(500,0)
  wait(1250)
  # Now the robot is in home


def mission_one():
    
    straight_speed = 900
    robot.reset()
    robot.straight(165)
    
    pid_line_follow_dist(
        sensor_to_track = "right", 
        side_of_line = "right",
        drive_speed = 150, 
        critical_gain = 1, 
        critical_period = 10, 
        stop_distance = 450)
     
    robot.straight(100)
 
    bottom_motor_mission_1.reset_angle(0)

    bottom_motor_mission_1.run_target(80,35)

    robot.straight(400)

    #bottom_motor_mission_1.run_target(80,30)
    #robot.straight(50)
    bottom_motor_mission_1.run_target(80,65)

    robot.straight(150)

    bottom_motor_mission_1.run_target(80,30)
    robot.straight(-30)

    bottom_motor_mission_1.run_target(80,45)

    robot.turn(60)
    
    #top_motor_mission_1.reset_angle(0)
    #top_motor_mission_1.run_target(80,0)

    robot.straight(-100)
    robot.turn(-32)
    robot.straight(680)
    robot.turn(30)
    robot.straight(-100)  
