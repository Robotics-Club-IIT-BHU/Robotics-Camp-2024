

## Gmapping?

Gmapping is a ROS package that implements a particle filter-based SLAM (Simultaneous Localization and Mapping) algorithm. It is used to create 2D maps from laser scan data while simultaneously determining the robot's position within the map.

**Key features of GMapping:**

* **Particle filter:** Utilizes a set of particles (hypotheses) to represent the robot's possible poses and the corresponding map.
* **Sensor data:** Relies on sensor data, typically from laser rangefinders (LIDAR), to update the particles and refine the map.
* **Open-source:** Freely available and widely used within the ROS community. 

### How GMapping Works

GMapping operates in a continuous cycle:

1. **Prediction:** The algorithm predicts the robot's movement based on odometry data (wheel encoder readings). This prediction updates the position of each particle in the filter.
2. **Update:** GMapping receives sensor data, usually from a LIDAR. It compares the sensor measurements with the predicted map for each particle.
3. **Weight assignment:** Particles that better align with the sensor data receive higher weights, indicating a higher probability of representing the robot's true pose and map.
4. **Resampling:** Based on the assigned weights, GMapping resamples the particle set. Particles with higher weights are more likely to be replicated, while those with lower weights are less likely to survive.

Over time, GMapping iterates through this cycle, progressively refining the map and robot pose estimation as it accumulates sensor data.


***Limitations of GMapping***
```
Static environment: Assumes a static environment. Moving objects can cause errors in the map.
```

#### Further Reading

For more detailed information on Gmapping, check out the following resources:
- [Youtube tutorial](https://www.youtube.com/watch?v=MFqn9i68bfM)
- [Gmapping Overview ros wiki](http://wiki.ros.org/gmapping)