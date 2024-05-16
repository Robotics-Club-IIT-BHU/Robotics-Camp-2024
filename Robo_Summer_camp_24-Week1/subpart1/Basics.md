<h1>Robotics-Summer-Camp 2024</h1> 

Hope you all have completed the ROS installation. And are familiar with what a workspace is and how to source your workspace. If not view [Week 0](https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2024/tree/week-1/Robo_Summer_camp_24-Week0) of summer camp!

## What are Nodes
A node really isn't much more than an executable file within a ROS package. ROS nodes use a ROS client library to communicate with other nodes. Nodes can publish or subscribe to a Topic. Nodes can also provide or use a Service. 
<br></br>
#### What does a Node do then?

A node is a process that performs computation. Nodes are combined together into a graph and communicate with one another using streaming topics.

<img src="ros101.png">
<br></br>
A robot control system will usually comprise many nodes. For example, one node controls a laser range-finder, one Node controls the robot's wheel motors, one node performs localization, one node performs path planning, one node provides a graphical view of the system, and so on. 

For more info visit [Node](http://wiki.ros.org/Nodes)


## Topics 

Topics are named buses over which nodes exchange messages. Topics have anonymous publish/subscribe semantics, which decouples the production of information from its consumption. In general, nodes are not aware of who they are communicating with. Instead, nodes that are interested in data subscribe to the relevant topic; nodes that generate data publish to the relevant topic. There can be multiple publishers and subscribers to a topic. 

<img src="ros_master_communication_topics.png">

You can see all the topics that are running with the command
```
rostopic list
``` 

And you see what is being published to that topic by the cmd 
```
rostopic echo /topic_name
```
