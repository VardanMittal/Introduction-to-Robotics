import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class SumPublisher(Node):
    def __init__(self) -> None:
        super().__init__("sum_publisher")
        self.pub = self.create_publisher(Float32,'Sum', 10)
        self.sub1= self.create_subscription(
            Float32,
            'Number_1',
            self.listener_num1,
            10)
        self.sub2= self.create_subscription(
            Float32,
            'Number_2',
            self.listener_num2,
            10)
        self.timer = self.create_timer(0.5, self.pub_sum)
        self.num1 = 0
        self.num2 = 0
    def listener_num1(self,msg):
        self.num1=msg.data
    def listener_num2(self,msg):
        self.num2=msg.data

    def pub_sum(self):
        msg = Float32()
        msg.data = self.num1 + self.num2
        self.pub.publish(msg=msg)

def main(args=None):
    rclpy.init(args=args)
    node = SumPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
