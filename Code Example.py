from controller import Robot

def execute_robot(robot):
    
    time_step = 32
    maximum_volocity = 2
    
    # engines
    left_engine = robot.getDevice('le')
    right_engine = robot.getDevice('re')
    left_engine.setPosition(float('inf'))
    right_engine.setPosition(float('inf'))
    left_engine.setVelocity(0.0)
    right_engine.setVelocity(0.0)    
    
    # activate infrared sensors
    iv_left = robot.getDevice('ds_infra_red3')
    iv_left.enable(time_step)
    
    ir_right = robot.getDevice('ds_infra_red1')
    ir_right.enable(time_step)
    
    iv_middle = robot.getDevice('ds_infra_red2')
    iv_middle.enable(time_step)
    
    # activate sonar sensor
    front_sonar = robot.getDevice('ds_sonar2')
    front_sonar.enable(time_step)
            
    while robot.step(time_step)  != -1:
        
        # read infrared sensors
        iv_left_value = iv_left.getValue()
        iv_right_value = ir_right.getValue()
        iv_middle_value = iv_middle.getValue()
        
        # read sonar sensor
        front_sonar_value = front_sonar.getValue()         
                        
        if(580 < iv_left_value < 625) and (580 < iv_right_value < 625) and (580 < iv_middle_value < 625):
            if(front_sonar_value < 514):
                left_engine.setVelocity(-maximum_volocity)
                right_engine.setVelocity(maximum_volocity)
                delay_function(robot, 1.8)
                                
                left_engine.setVelocity(maximum_volocity)
                right_engine.setVelocity(maximum_volocity)
                delay_function(robot, 3)
                
                left_engine.setVelocity(maximum_volocity)
                right_engine.setVelocity(-maximum_volocity)
                delay_function(robot, 1.8)
                
                left_engine.setVelocity(maximum_volocity)
                right_engine.setVelocity(maximum_volocity)
                delay_function(robot, 8)
                
                left_engine.setVelocity(maximum_volocity)
                right_engine.setVelocity(-maximum_volocity)
                delay_function(robot, 1.8)
                
                left_engine.setVelocity(maximum_volocity)
                right_engine.setVelocity(maximum_volocity)
                delay_function(robot, 3)
                
                left_engine.setVelocity(-maximum_volocity)
                right_engine.setVelocity(maximum_volocity)
                delay_function(robot, 2.35)
                               
            else:
                left_engine.setVelocity(maximum_volocity)
                right_engine.setVelocity(maximum_volocity)
                delay_function(robot, 1.3)
                
                left_engine.setVelocity(maximum_volocity)
                right_engine.setVelocity(-maximum_volocity)
                delay_function(robot, 1.8)
        elif (iv_left_value > 625) and (iv_right_value > 625) and (iv_middle_value <= 625):
            left_engine.setVelocity(maximum_volocity)
            right_engine.setVelocity(maximum_volocity)
        elif (iv_left_value <= 625) and (iv_right_value > 625) and (iv_middle_value <= 625):
            left_engine.setVelocity(-maximum_volocity)
            right_engine.setVelocity(maximum_volocity)
        elif (iv_left_value > 625) and (iv_right_value <= 625) and (iv_middle_value <= 625):
            left_engine.setVelocity(maximum_volocity)
            right_engine.setVelocity(-maximum_volocity)
        elif (iv_left_value <= 625) and (iv_right_value > 625) and (iv_middle_value > 625):
            left_engine.setVelocity(-maximum_volocity)
            right_engine.setVelocity(maximum_volocity)
        elif (iv_left_value > 625) and (iv_right_value <= 625) and (iv_middle_value > 625):
            left_engine.setVelocity(maximum_volocity)
            right_engine.setVelocity(-maximum_volocity)
        elif (iv_left_value > 625) and (iv_right_value > 625) and (iv_middle_value > 625):
            left_engine.setVelocity(maximum_volocity)
            right_engine.setVelocity(maximum_volocity)
        
def delay_function(robot, time):
    current_time_1 = float(robot.getTime())
    current_time_2 = float(robot.getTime())
    
    while current_time_2 < (current_time_1 + time): 
        
        current_time_2 = float(robot.getTime())
        robot.step(1)

if __name__ == "__main__":
    my_robot = Robot()
    execute_robot(my_robot)



