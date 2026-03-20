# ROS2 Dynamic Publisher-Subscriber System

##  Overview
This project implements a ROS2 Humble system with:
- Two independent publishers (`publisher1`, `publisher2`)
- One intelligent subscriber acting as a control unit

The subscriber dynamically switches between publishers using user input without restarting nodes.

##  Features
- Real-time topic switching
- Dynamic unsubscribe and resubscribe
- Multi-threaded input handling
- Continuous data streaming
- Clean modular ROS2 architecture

##  Setup Instructions

### 1. Build Workspace
bash
cd ~/ros2_ws
colcon build --packages-select switch_pubsub
source install/setup.bash
Run Nodes


Open 3 terminals:
Terminal 1
  ros2 run switch_pubsub publisher1
Terminal 2
  ros2 run switch_pubsub publisher2
Terminal 3
  ros2 run switch_pubsub subscriber
Usage

Select initial node:
node1 / node2
During runtime:
  Press s → switch subscription
  Press q → quit

Example Flow
Subscribed to node1
[Node1] Publisher 1 data 10

Press 's'
Enter node → node2

Subscribed to node2
[Node2] Publisher 2 data 5
