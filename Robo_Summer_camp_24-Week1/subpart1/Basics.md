<p align="center"> <h1>Robotics-Summer-Camp 2024</h1> </p>

Hope you all have completed the ROS installation. And are familiar with what a workspace is and how to source your workspace. If not view [Week 0](https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2024/tree/week-1/Robo_Summer_camp_24-Week0) of summer camp!

# ROS (Robot Operating System) Basics

## Introduction
ROS, short for Robot Operating System, is an open-source framework that provides a collection of tools, libraries, and conventions to simplify the task of creating complex and robust robot behavior across a wide variety of platforms. It is not an operating system in the traditional sense, but rather a middleware that runs on top of a traditional operating system like Linux.

## Nodes
In ROS, a node is a process that performs computation. Nodes are designed to be modular and communicate with each other through passing messages. Each node can perform a specific task, such as controlling a sensor, processing data, or executing a behavior.
<p align="center">
<img src="ros101.png"></p>

### Basic Commands:
- **Creating a Node:**
  ```bash
  rosrun <package_name> <node_name>
  ```
  Example: `rosrun turtlesim turtlesim_node`

## Topics
Topics are named buses over which nodes exchange messages. They enable communication between nodes in a decoupled manner, allowing nodes to communicate without needing to know about each other. Nodes can publish messages to topics or subscribe to topics to receive messages.

<p align="center">
<img src="ros_master_communication_topics.png"></p>

### Basic Commands:
- **Viewing Active Topics:**
  ```bash
  rostopic list
  ```
- **Viewing Information about a Topic:**
  ```bash
  rostopic info <topic_name>
  ```
- **Displaying Messages from a Topic:**
  ```bash
  rostopic echo <topic_name>
  ```

## Publishers and Subscribers
- **Publishers:** Nodes that produce and send messages on a topic are called publishers. They are responsible for creating and transmitting messages to the specified topic.
- **Subscribers:** Nodes that receive and process messages from a topic are called subscribers. They listen for messages on the specified topic and react accordingly when messages are received.

### Basic Commands:
- **Publishing a Message to a Topic:**
  ```bash
  rostopic pub <topic_name> <message_type> <message>
  ```
  Example: `rostopic pub /turtle1/cmd_vel geometry_msgs/Twist '{linear: {x: 0.1, y: 0, z: 0}, angular: {x: 0, y: 0, z: 0.1}}'`

## Services

In ROS, services provide a way for nodes to send requests and receive responses from other nodes. Unlike topics, which facilitate asynchronous communication through message passing, services enable synchronous communication, where a node sends a request and waits for a response before proceeding. Services are useful for tasks that require direct interaction or immediate feedback, such as querying information or triggering actions.

### Components of a Service

A ROS service consists of two main components:

1. **Service Server**: The service server is a node that provides the service. It defines the available service and handles incoming requests. When a request is received, the server processes it and sends back a response.

2. **Service Client**: The service client is a node that sends requests to the service server and waits for responses. It initiates communication by sending a request message to the server and then waits for the server to process the request and send back a response message.

### Basic Commands

Here are some basic commands to interact with ROS services:

- **Viewing Available Services**:
  ```bash
  rosservice list
  ```
  This command lists all the available services in the ROS system.

- **Viewing Service Details**:
  ```bash
  rosservice info <service_name>
  ```
  This command provides detailed information about a specific service, including its data type and where it is located.

- **Calling a Service**:
  ```bash
  rosservice call <service_name> <request_message>
  ```
  This command sends a request message to the specified service and displays the response message returned by the service server.

### Example

Let's say we have a service named `/add_two_ints` that adds two integers. We can call this service using the following command:

```bash
rosservice call /add_two_ints "a: 5
b: 3"
```

This command sends a request to add 5 and 3 to the `/add_two_ints` service and displays the result returned by the service server.

**Although you will not be using services for you tasks in Phase 1.**

### Use Cases

Services are commonly used in ROS for various tasks, such as:

- Requesting sensor information (e.g., querying the current temperature from a temperature sensor).
- Triggering actions (e.g., starting or stopping a robot's movement).
- Requesting data processing (e.g., requesting a map update from a mapping node).

By providing a synchronous communication mechanism, services complement the asynchronous communication facilitated by topics, allowing for a wide range of interactions between nodes in a ROS system.


### **The complete communication between nodes via topics and service calls etc. looks like this**

<p align="center"><img src="Nodes-TopicandService.gif"> </p>    

## Useful Tools
### rqt
rqt is a powerful ROS graphical user interface (GUI) plugin framework. It provides various plugins for visualization, debugging, and interaction with ROS systems. Some commonly used rqt plugins include rqt_graph for visualizing the ROS computation graph and rqt_plot for plotting data from ROS topics.

### Basic Command:
- **Launching rqt:**
  ```bash
  rqt
  ```

### rqt Tools and Plugins

1. **rqt_graph**: This plugin provides a visualization of the ROS computation graph. It displays the relationships between nodes, topics, and services in your ROS system.
This will be very important tool to quickly analyse your robot and the way it is communicating. 


2. **rqt_plot:** This plugin allows you to plot data from ROS topics in real-time. It's useful for visualizing numerical data such as sensor readings or robot positions over time.

3. **rqt Topic Monitor:** This plugin provides a graphical interface for monitoring ROS topics in real-time. It displays a list of active topics along with their message types and message frequencies. You can subscribe to topics and view the messages being published, making it easy to inspect and debug data flowing through your ROS system.

4. **rqt Message Publisher:** The rqt Message Publisher plugin allows you to manually publish messages to ROS topics. It provides a graphical interface for selecting a topic, specifying the message type, and entering message data. This plugin is useful for testing and simulating behavior in your ROS system by sending custom messages to topics.


---

## Always Refer Google Or Roswiki for any confusion, The are the best resources for Learning

Proceed to [Subpart 2](/Robo_Summer_camp_24-Week1/subpart2/subpart2.md)