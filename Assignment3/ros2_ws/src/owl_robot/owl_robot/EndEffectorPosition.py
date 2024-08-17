import rclpy
from rclpy.node import Node
from tf2_ros import TransformListener, Buffer
from geometry_msgs.msg import TransformStamped

class EndEffectorPose(Node):

    def __init__(self):
        super().__init__('EndEffectorPose')
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)
        self.timer = self.create_timer(1.0, self.lookup_transform)

    def lookup_transform(self):
        try:
            now = rclpy.time.Time()
            trans = self.tf_buffer.lookup_transform('world', 'end_effector', now)
            position = trans.transform.translation
            orientation = trans.transform.rotation

            self.get_logger().info(f'End-Effector Position: x={position.x}, y={position.y}, z={position.z}')
            self.get_logger().info(f'End-Effector Orientation: x={orientation.x}, y={orientation.y}, z={orientation.z}, w={orientation.w}')
        except Exception as e:
            self.get_logger().error(f'Could not transform: {str(e)}')

def main(args=None):
    rclpy.init(args=args)
    node = EndEffectorPose()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
