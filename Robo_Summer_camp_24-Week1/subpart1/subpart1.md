<p align="center"><img src="https://answers.ros.org/upfiles/14554624266871161.png" width="60" height="60"> <b>R</b>obotic<b>O</b>perating<b>S</b>ystem 

<h1>Robotics-Summer-Camp 2024</h1> </p>

Welcome to the week 1 of SummerCamp24 offered by Robotics Club, IIT(BHU) Varanasi. We Aim to deliver a Beginner Level of Understanding to ROS to get you started with projects with it.

In this section we plan to Teach you the basics of ROS Nodes, Topics, and services. 

**NOTE**: We would always prefer you to look up [**ros wiki**](http://wiki.ros.org/Documentation) and [**ros answers**](https://answers.ros.org/questions/) as they containing literally everything  from where most of us have learnt ROS.

## What is ROS

ROS stands for Robot Operating System. Even if it says so, ROS is not a real operating system since it goes on top of operating systems like Linux. ROS is a framework on top of the O.S. that allows it to abstract the hardware from the software. This means you can think in terms of software for all the hardware of the robot. And that’s good news for you because this implies that you can actually create programs for robots without having to deal with the hardware. Cool right!
<br/><br/>


## Why ROS?

ROS makes it easy to get a robot running and do the required task.
> These are the lines from the [original paper](http://robotics.stanford.edu/~ang/papers/icraoss09-ROS.pdf) :

>  Writing software for robots is difficult, particularly as the scale and scope of robotics continues to grow. Different types of robots can have wildly varying hardware, making code reuse nontrivial. On top of this, the sheer size of the required code can be daunting, as it must contain a deep stack starting from driver-level software and continuing up through perception, abstract reasoning, and beyond. Since the required breadth of expertise is well beyond the capabilities of any single researcher, robotics software architectures must also support large-scale software integration efforts.  

> To meet these challenges, many robotics researchers, including ourselves, have previously created a wide variety of frameworks to manage complexity and facilitate rapid prototyping of software for experiments, resulting in the many robotic software systems currently used in academia and industry. Each of these frameworks was designed for a particular purpose, perhaps in response to perceived weaknesses of other available frameworks, or to place emphasis on aspects which were seen as most important in the design process.

> ROS is also the product of tradeoffs and prioritizations made during its design cycle. We believe its emphasis on large-scale integrative robotics research will be useful in a wide variety of situations as robotic systems grow ever more complex

For most of your journy you will be mostly using packages that other people have made. To install a new package just simply search for the ROS package and it will do the trick for you. This is an example of a ROS package called Gmapping, you will be doing this in ROS Specilization.
```bash
$ sudo apt-get install ros-openslam-gmapping
$ roslaunch gmapping gmapping.launch
...
....
......[process-started] Node launched
```
![slam](https://user-images.githubusercontent.com/56990337/122931433-84afe680-d38a-11eb-82b4-67c0014d80a3.gif)



Proceed to the [Basics](Basics.md)