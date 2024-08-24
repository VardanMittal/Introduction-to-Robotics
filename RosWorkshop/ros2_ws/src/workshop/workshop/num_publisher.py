import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class NumPublisher(Node):
    def __init__(self) -> None:
        super().__init__("num_publisher")
        self.pub1 = self.create_publisher(Float32,'Number_1', 10)
        self.pub2 = self.create_publisher(Float32, 'Number_2', 10)
        self.timer = self.create_timer(0.5, self.pub_nums)
    def pub_nums(self):
        msg1 = Float32()
        msg2 = Float32()

        msg1.data = 5.0
        msg2.data = 10.0

        self.pub1.publish(msg=msg1)
        self.pub2.publish(msg=msg2)

def main(args=None):
    rclpy.init(args=args)
    node = NumPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()