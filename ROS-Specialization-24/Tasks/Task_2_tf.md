## Task2
- Open up the modified husky you made in the last task in Rviz.  
- Visualize the Tf tree in rqt and submit the screenshot.  
- Now open up a terminal and run this
```
rosrun tf tf_echo source_frame target_frame
```
(replace source_frame and target_frame with any two frames which are present in your tf tree)
- You should be getting a similar output to this (numbers will vary)
```
At time 1657366984.951
- Translation: [0.000, 0.000, 0.250]
- Rotation: in Quaternion [0.000, 0.000, 0.000, 1.000]
            in RPY (radian) [0.000, -0.000, 0.000]
            in RPY (degree) [0.000, -0.000, 0.000]
At time 1657366985.951
- Translation: [0.000, 0.000, 0.250]
- Rotation: in Quaternion [0.000, 0.000, 0.000, 1.000]
            in RPY (radian) [0.000, -0.000, 0.000]
            in RPY (degree) [0.000, -0.000, 0.000]
```
- If you are confused by what source_frame and target_frame are refer to [this](#useful-info-and-links)  

## What you will do  
1. You will be doing the same thing as above but through a python script. (Easier to grasp concepts in Python)
2. You will be printing out on the terminal the translation and rotational matrices of the **camera_link** from the **husky_robot_model__base_link**.  
3. Next you will be creating a new frame called **carrot** that will **always** be **1 metre** in front of husky on the XY plane.  
4. Print out the same matrices now of the **carrot** from the **camera_link** using your python script.  
5. Now that was a static frame you created, its time to make a dynamic frame, the **carrot** frame should always be at a distance of sin(ROS Time in secs)
in front of the base_link.  


## Submission Instructions  
- A screenshot of your Tf Tree with the urdf created for task1  
- The final python script that you created which includes printing the lookup of (camera_link from base_link) and publishing the dynamic carrot frame.
-  Now run your python script and open up a new Terminal,
```
rosrun tf tf_echo husky_robot_model__base_link carrot
```
- A screenshot of the output of the above command. 

## Useful info and links  
- [ ] The links given in the Tf section especially [this](http://wiki.ros.org/tf/Tutorials/Adding%20a%20frame%20%28Python%29) :)
- [ ] Clear your concepts of source_frame and target_frame.  
Read this very carefully- Imagine there is a **global** frame of reference like the cartesian frame in XYZ axes with origin at (0,0,0). Now let there
 be two more frames **F1** and **F2** which can be anywhere in this global frame, in any orientation.  
You want to find the position of **F1** in the cartesian frame. It is equivalent to running 
```
rosrun tf tf_echo global F1
```  
The translation matrix will give you the position of F1 and rotation matrix will give you the orientation.  
Similarly you can find the tf of F2. Again these will only work when these frames are connected in the Tf Tree.  
You can also find the position of **F2** with respect to **F1**, here the difference in translation and orientation are calculated w.r.t the **F1** frame.  
```
rosrun tf tf_echo F1 F2     //(change in position and orientation of F2 from F1 in the F1 frame axes)
```  
- [ ] Another important point to notice is that the lookupTransform function api is exactly the same as tf_echo above,but in the sendTransform function
the target frame is written first and the source frame next, so it is the exact opposite of lookupTransform.  
