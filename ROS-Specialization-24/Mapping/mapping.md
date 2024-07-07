# Mapping 

***To understand this concept lets assume I drop you in a city of TYPE 4 civilisation on another planet and I order you to reach nearest launch pad for airlift will you be able to do it ?
Obviously no..
Because the city is completely unknown to you, You neither know where you are in the city nor where is the launch pad. Similar is the case of an autonomous bot. This is when mapping and Localisation comes into play
Mapping is when a robot explores its surroundings and creates a detailed map, just like drawing a blueprint of a house or a city. It notes down all the walls, furniture, and objects it encounters, so it knows where everything is.
this is done with the help of sensors like lidar, depth camera etc.***

> In the camp we have used gmapping for hands on, since it is easiest and beginner friendly but it maps the environment in 2 dimensions therefore it is not widely used in realworld application.

>Mapping techniques like 2D has hector, cartographer, and in 3D Rtab mapping, Octomapping, ORB SLAM etc are much more advanced.

## How Does 2D Mapping Work?

2D mapping typically involves the following steps:

1. **Sensor Data Collection**: Using sensors like LiDAR or cameras to gather information about the environment.
2. **Data Processing**: Filtering and preprocessing the sensor data.
3. **Map Building**: Integrating the processed data to build a consistent 2D map.
4. **Localization**: Determining the robot's position within the map.

**Types of mapping:**
- [Gmapping](Gmapping.md)
- [Hector](Hector.md)
- [Cartographer](Cartographer.md)


## Further Reading

For more detailed information on 2D mapping, check out the following resources:
- [Matlab tech talks series](https://www.youtube.com/playlist?list=PLn8PRpmsu08rLRGrnF-S6TyGrmcA2X7kg) - the best place to get a intuitive idea on what is going on.. :)
- [See all three types of mapping](https://www.youtube.com/watch?v=7iM2ynZEuf0)
- [2D Mapping Overview ros wiki](http://wiki.ros.org/navigation/Tutorials/RobotSetup)
