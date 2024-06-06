'''
Task 3 - 

A car is loaded. You have to develop a PID controller for that car such that it runs along the line y = 0.
The line is also visible on the plane.
Callibrate the PID gains such that car gets to the line as fast as possible and follows it without much disturbance.
Refer to the past two taks and their codes for hints.



INSTRUCTIONS -
    Select the simulation window and Press ENTER to execute


'''




import numpy as np 
import pybullet as p 
import time
import math
import cv2

p_id = p.connect(p.GUI)                #Loading the simulation
p.setGravity(0, 0, -10)                #Setting the gravity

plane = p.loadURDF("src/plane.urdf")        #Loading the plane
carPos = [0,3,0.1]                      #This is where the car will spawn, this is constant. Don't change

m = 0                           #Declaring the slope of the required line y = mx + c
c = 0                           #Declaring the contsnat of the reuired line  y = mx + c
angle = math.atan(m)

car = p.loadURDF("src/car/car1.urdf", carPos, p.getQuaternionFromEuler([0,0,angle]))  #Loading the car with head parallel to the given line


def printLine(m, c):                        #This functions draws a line that we need to follow
    angle = math.atan(m)
    z = 0.02
    origin = [0,c,z]
    line = p.loadURDF("src/line.urdf", origin, p.getQuaternionFromEuler([0,0,angle]))

printLine(m, c)                    #Calling the function to print the line


num = p.getNumJoints(car)                  #Getting the total number of joints in the car
for i in range(num):
    print(p.getJointInfo(car, i))           #Printing the information of each joint to get the motor joints


#These are the 4 motor joints that we need to manipulate, we declare them here.

fl = 2        #Front Left wheel        
fr = 3        #Front Right wheel
bl = 4        #Back Left wheel
br = 5        #Back Right wheel

p.setJointMotorControlArray(car, [fl, bl, fr, br], p.VELOCITY_CONTROL, forces = [0,0,0,0])   #This is done to enable torque control in wheels of the car
p.stepSimulation()



'''
Above this is the loading code, make no changes to it
Below this is the code that you need to work with.
'''



#Declare the desired_state and base_torque globally
desired_state = 0  #Set Value Yourself
base_torque = 0   #Set Value Yourself


def moveCar(base_torque, action):  #Enter the motor control here to move the car, give base torque and action calculated as input
    pass
    #Use p.JointMotorControlArray() function in torque mode
    #Use differential drive to nullify the error
    #The differential drive must increase or decrease the speed of the tyres about a constant base torque using gains



def calc_error(): #You can calculate the error and required action using this function
    pass
    #Calculate error by getting the car's position using getBasePositionAndOrientation() function
    #The error is upto your imagination to select. Hint : It can be a distance between the line and the car
    #After getting the error, calculate actions using PID gains.
    #Calibrate your PID gains experimentally. Refer to the earlier tasks for hints.




#Select the simulation window and Press ENTER to execute




while(True):                         #This while loop will run until ESCAPE key is pressed, then it will start the simulation.
    keycode = p.getKeyboardEvents()       #Getting the keyboard events through PyBullet
    if keycode.get(p.B3G_RETURN) == 1:                     #As soon as any key is pressed and it's ENTER key, simulation starts
        p.resetSimulation()       #Simulation is reseted
        p.setGravity(0, 0, -10)

        plane = p.loadURDF("src/plane.urdf")
        car = p.loadURDF("src/car/car1.urdf", carPos, p.getQuaternionFromEuler([0,0,angle]))   #Plane and car loaded again
        p.setJointMotorControlArray(car, [fl, bl, fr, br], p.VELOCITY_CONTROL, forces = [0,0,0,0])   #This is done to enable torque control in wheels of the car
        printLine(m, c)   #This draws a line along y = 0, which we have to follow

        while(True):
            p.resetDebugVisualizerCamera(7, -90, -45, p.getBasePositionAndOrientation(car)[0])  #This will keep the camera on the car always
            p.stepSimulation()    #This steps the simulation further by 0.01 seconds approx

            #Call all the other functions inside this while loop

            #k = cv2.waitKey(1)    Uncomment this while using trackbars, otherwise they won't work in real time.
            time.sleep(1./240.)
            print("running")

            keycode = p.getKeyboardEvents()    #This will keep tracking if ENTER key is pressed again.
            if keycode.get(p.B3G_RETURN) == 1:              #We end the current simulation and start a new one again if ENTER key is pressed
                print("Episode finished")                   #This is a way to re-run the simulation without re-executing the code
                p.resetSimulation()  #Reseting the simulation
                break                #Breaking out of the inner while loop

    


