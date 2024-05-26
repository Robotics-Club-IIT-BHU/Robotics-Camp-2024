# Building the Blueprint: URDF and Robot Design
We've explored robot building blocks (links & joints) and their power source (actuators). Now, meet URDF: the robot's blueprint! This format describes a robot's structure (links, joints, connections) and actuators in a way computers understand. Think building a robot in a simulation - URDF lets software grasp the robot's capabilities and simulate its movements.

<img src="https://github.com/Krishnendu8904/RobotDesign/blob/main/URDF/14689398051725704.png?raw=true" width="500" height="350">

### Here's a step-by-step guide to get you started creating your own URDF file:
 
* Warm Up with XML: If you're new to coding, a [quick video](https://www.youtube.com/watch?v=1JblVElt5K0) on basic XML syntax will be helpful.
* URDF 101: Get familiar with the fundamentals of URDF through [this introductory lecture](https://ocw.tudelft.nl/course-lectures/2-2-1-introduction-to-urdf).
* Hands-on Practice: Now it's time to write your own URDF file! [These tutorials will guide you through the process](http://wiki.ros.org/urdf/Tutorials/Create%20your%20own%20urdf%20file), focusing on the current core structure. Don't worry about making it look fancy yet.
* Decoding the Code: The various tags and attributes in URDF might initially seem complex, especially regarding joint and link placement. [These resources offer detailed explanations](http://wiki.ros.org/urdf/Tutorials/Building%20a%20Visual%20Robot%20Model%20with%20URDF%20from%20Scratch) to help you decipher the code.
* Additional Resource: You may follow this [ROS wiki tutorials for URDF](http://wiki.ros.org/urdf). Explore the entire page and learn about URDF

_Pro Tip: The "visual" tag defines your robot’s appearance, while the "collision" tag defines how it interacts with its environment. Ensure both tags have the same settings to avoid unexpected behaviour during simulation._

* Debugging Help: Creating URDF files can be tricky, and syntax errors are common. Enter the following in terminal.

        $ sudo apt-get install liburdfdom-tools

Now, you should be able to run a command named 'check_urdf'. Pass the relative path of your urdf file as an attribute to the command:

        $ check_urdf <path to the URDF file>

This will parse the URDF file and tell you exactly which line has an error. If the file is parsed successfully, a summary of the parent and child links will be outputted.

Remember, creating a URDF file takes practice. Don't get discouraged if it takes some time to master! 

Once you've written your URDF file, you can [visualise it using this online tool](https://mymodelrobot.appspot.com/5629499534213120). Simply paste your code and click "Load URDF" to see your robot come to life on the screen! 

We've included a [sample URDF file for an R2D2 robot](https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/blob/main/Mastering__Pybullet/PART_1/(2)%20Pybullet%20Basic%20Functions/sample.urdf) and a [Python script (visualizer.py)](https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/blob/main/Mastering__Pybullet/PART_1/(2)%20Pybullet%20Basic%20Functions/visualizer.py) to visualise any URDF file. Download both files and play around!



#### Additional Resources

* [Robot Geometry in URDF](http://wiki.ros.org/urdf/Tutorials/Create%20your%20own%20urdf%20file)
* [Building a visual robot](http://wiki.ros.org/urdf/Tutorials/Building%20a%20Visual%20Robot%20Model%20with%20URDF%20from%20Scratch)

*Tip: If they're not in the same folder, update the path to the URDF file in the Python script.*


### [TASK 1 -->](https://github.com/Krishnendu8904/RobotDesign/blob/main/URDF/urdf_task_A.md)