import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Publisher2(Node):
    def __init__(self):
        super().__init__('publisher2')
        self.pub = self.create_publisher(String, 'node2_topic', 10)
        self.timer = self.create_timer(1.0, self.publish_msg)
        self.count = 0

    def publish_msg(self):
        msg = String()
        msg.data = f"Publisher 2 data {self.count}"
        self.pub.publish(msg)
        self.get_logger().info(msg.data)
        self.count += 1

def main(args=None):
    rclpy.init(args=args)
    node = Publisher2()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()
