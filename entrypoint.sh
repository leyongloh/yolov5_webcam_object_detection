#!/bin/bash
# Basic entrypoint for ROS / Colcon Docker containers

# Source ROS and Colcon workspaces
source /opt/ros/galactic/setup.bash
echo "Sourced ROS2 Galactic"
if [ -f /yolov5_webcam_tutorial_ws/install/setup.bash ]
then
  source /yolov5_webcam_tutorial_ws/install/setup.bash
  echo "Sourced TurtleBot3 base workspace"
fi

# Execute the command passed into this entrypoint
exec "$@"