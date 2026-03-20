import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import threading

class SubscriberNode(Node):
    def __init__(self):
        super().__init__('subscriber_node')
        self.active_node = None
        self.sub = None
        self.lock = threading.Lock()

    def callback(self, msg):
        self.get_logger().info(f"[{self.active_node}] {msg.data}")

    def subscribe_to_node(self, node_name):
        with self.lock:
            if self.sub:
                self.destroy_subscription(self.sub)
                self.sub = None

            if node_name == 'node1':
                self.sub = self.create_subscription(String, 'node1_topic', self.callback, 10)
            elif node_name == 'node2':
                self.sub = self.create_subscription(String, 'node2_topic', self.callback, 10)
            else:
                print("Invalid node")
                return

            self.active_node = node_name
            print(f"Subscribed to {node_name}")
            self.get_logger().info(f"Now subscribing to {node_name}")

    def input_thread(self):
        while rclpy.ok():
            cmd = input("Press 's' to switch node, 'q' to quit: ").strip()

            if cmd == 's':
                while True:
                    new_node = input("Enter node (node1/node2): ").strip()
                    if new_node in ['node1', 'node2']:
                        self.subscribe_to_node(new_node)
                        break
                    else:
                        print("Invalid node!")

            elif cmd == 'q':
                print("Exiting...")
                rclpy.shutdown()
                break

def main(args=None):
    rclpy.init(args=args)
    node = SubscriberNode()

    # Initial selection
    while not node.active_node:
        choice = input("Select initial node (node1/node2): ").strip()
        if choice in ['node1', 'node2']:
            node.subscribe_to_node(choice)
        else:
            print("Invalid input!")

    # Start control thread
    thread = threading.Thread(target=node.input_thread, daemon=True)
    thread.start()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    if node.sub:
        node.destroy_subscription(node.sub)

    node.destroy_node()
    rclpy.shutdown()
