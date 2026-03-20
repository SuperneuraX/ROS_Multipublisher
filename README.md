ROS2 Dynamic Publisher–Subscriber Control System
# ROS2 Dynamic Publisher–Subscriber Control System

> Real-time, interactive control over multiple ROS2 data streams using a single intelligent subscriber node.

---

## ✨ Overview

This project demonstrates a modular ROS2 Humble architecture with two independent publishers and a smart subscriber that dynamically switches between them at runtime. The system eliminates the need for restarts or additional control nodes, enabling seamless real-time topic management.

---

## 🧠 Key Highlights

- 🔄 **Dynamic Subscription Switching** — Change active data source at runtime
- ⚡ **Real-Time Communication** — Continuous streaming using ROS2 topics
- 🧩 **Modular Design** — Independent publishers with a centralized control subscriber
- 🛠️ **Thread-Safe Execution** — Uses multi-threading for uninterrupted input handling
- 🚫 **Zero Restart Required** — Switch nodes instantly without stopping the system

---

## 🏗️ Architecture


+----------------+ +----------------+
| Publisher 1 | | Publisher 2 |
| (node1_topic) | | (node2_topic) |
+--------+-------+ +--------+-------+
| |
| |
+-----------+-------------+
|
+-------v--------+
| Subscriber |
| (Control Unit) |
+----------------+


---

## 📂 Project Structure


switch_pubsub/
├── publisher1.py # Publishes data on node1_topic
├── publisher2.py # Publishes data on node2_topic
├── subscriber.py # Dynamic subscriber + control interface


---

## ⚙️ Getting Started

### Prerequisites

- ROS2 Humble installed
- Python 3.8+
- Colcon build system

---

### 🔧 Build Instructions

```bash
cd ~/ros2_ws
colcon build --packages-select switch_pubsub
source install/setup.bash
▶️ Run the System

Open three terminals:

# Terminal 1
ros2 run switch_pubsub publisher1

# Terminal 2
ros2 run switch_pubsub publisher2

# Terminal 3
ros2 run switch_pubsub subscriber
🎮 Interactive Usage

Select initial node:

node1 / node2

Runtime controls:

s → Switch active publisher

q → Exit system

🔄 Example Output
Subscribed to node1
[Node1] Publisher 1 data 12

Press 's'
Enter node → node2

Subscribed to node2
[Node2] Publisher 2 data 3
