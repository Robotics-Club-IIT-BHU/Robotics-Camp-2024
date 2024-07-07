# Hector SLAM in ROS

## What is Hector SLAM?

Hector SLAM is a ROS package that uses Gauss-Newton optimization to perform SLAM (Simultaneous Localization and Mapping) with high accuracy and **without requiring odometry data**, this is one of the key differences in gmapping and hector slam. It is particularly well-suited for platforms that cannot provide reliable odometry.(but honestly is a pain to work with, we generally relay on cartographer)

## How Hector SLAM Works

Hector SLAM relies on high-frequency LiDAR data and matches it directly to the map using scan matching techniques. It uses a multi-resolution approach to improve the efficiency and accuracy of the SLAM process.


## Further Reading

For more detailed information on Hector SLAM, check out the following resources:
- [Hector SLAM Overview](http://wiki.ros.org/hector_slam)
- [youtube Vid ](https://www.youtube.com/watch?v=F8pdObV_df4&t=1s)
- [hector vs cartographer](https://www.youtube.com/watch?v=NtxTa1wjE4I)