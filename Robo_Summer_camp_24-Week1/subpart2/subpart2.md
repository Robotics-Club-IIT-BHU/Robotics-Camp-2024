<p align="center"><img src="https://answers.ros.org/upfiles/14554624266871161.png" width="60" height="60"> <b>R</b>obotic<b>O</b>perating<b>S</b>ystem 

<h1>Robotics-Summer-Camp 2024</h1> </p>

Welcome to the Robotics Summer Camp 2024! This camp is designed to introduce you to the exciting world of robotics using the Robotic Operating System (ROS). After going through the theoretical aspects, it's time to dive into practical applications and get hands-on experience.

## Overview
In this camp, you'll learn how to create and manage ROS packages, develop nodes for communication between robots, and build a functional robotics project. By the end of this camp, you'll be comfortable working with ROS and capable of developing your own robotics applications.

## Packages
In your workspace, you'll organize different groups of nodes that perform similar tasks or are closely related to each other into packages. This modular approach makes managing and developing complex systems easier. 

### What is a ROS Package?
A ROS package is a directory that contains:
- Metadata about the package in an XML file (`package.xml`)
- Instructions for building the package with catkin tools (`CMakeLists.txt`)

### Creating a ROS Package
To create a package, follow these steps:

1. Navigate to the `src` folder of your catkin workspace:
    ```bash
    cd ~/catkin_ws/src/
    ```

2. Create a new package named `beginner_tutorials` with dependencies on `std_msgs`, `rospy`, and `roscpp`:
    ```bash
    catkin_create_pkg beginner_tutorials std_msgs rospy roscpp
    ```

Congratulations, you've created your first package!

### Building the Workspace
After creating a package, you need to build your workspace and source the setup file. This makes the newly created package available for use.

1. Navigate to your catkin workspace:
    ```bash
    cd ~/catkin_ws
    ```

2. Build the workspace using catkin tools:
    ```bash
    catkin build
    ```
    Alternatively, if you're familiar with `catkin_make`, you can use:
    ```bash
    catkin_make
    ```

3. Source the setup file to update your environment:
    ```bash
    source devel/setup.bash
    ```

You can verify the successful creation and build of your package by running:
```bash
rospack find beginner_tutorials
```

For more information on creating packages, you can visit the [official ROS tutorial](https://wiki.ros.org/ROS/Tutorials/CreatingPackage).

## Task 1: Python Publisher and Subscriber

Your first task is to create a publisher and a subscriber node in Python. These nodes will communicate by sending and receiving messages.

### Steps to Complete Task 1

1. **Follow the Tutorial**:
    Refer to the [Writing a Simple Publisher and Subscriber (Python)](https://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29) tutorial for detailed instructions.

2. **Message Format**:
    The message published by your node should follow this format:
    ```
    "Communication is working smoothly! Ping no. %d"
    ```
    Here, `%d` is an integer that increments by 1 with each message.

3. **Submit Your Work**:
    Record a video of your publisher and subscriber working together. The video should clearly show the messages being published and subscribed.

### Task 1b (Bonus): C++ Publisher and Subscriber

For an additional challenge, implement the publisher and subscriber nodes in C++. This will help you understand the differences and similarities between Python and C++ in ROS.

### Steps to Complete Task 1b

1. **Follow the Tutorial**:
    Refer to the [Writing a Simple Publisher and Subscriber (C++)](https://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28c%2B%2B%29) tutorial.

2. **Message Format**:
    Ensure the message format is the same as in Task 1:
    ```
    "Communication is working smoothly! Ping no. %d"
    ```

3. **Submit Your Work**:
    Record a video of your C++ publisher and subscriber nodes working together. The video should demonstrate the successful communication between the nodes.

### Tips for Video Submissions
- Use OBS Studio or any other screen recording software to capture your work.
- Ensure the video clearly shows the terminal outputs and the functioning of both nodes.

We hope you find these tasks both challenging and rewarding. Good luck, and have fun exploring ROS!
