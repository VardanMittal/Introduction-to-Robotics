import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
import PyKDL as kdl

class EndEffectorPosition(Node):
    def __init__(self):
        super().__init__('end_effector_position_node')

        # Create a kinematic chain
        self.robot_chain = kdl.Chain()
        self.robot_chain.addSegment(kdl.Segment(kdl.Joint(kdl.Joint.RotZ), kdl.Frame(kdl.Vector(0.5, 0.0, 0.0))))
        self.robot_chain.addSegment(kdl.Segment(kdl.Joint(kdl.Joint.RotZ), kdl.Frame(kdl.Vector(0.5, 0.0, 0.0))))

        # Create a FK solver
        self.fk_solver = kdl.ChainFkSolverPos_recursive(self.robot_chain)

        # Initialize joint positions array
        self.joint_positions = kdl.JntArray(self.robot_chain.getNrOfJoints())

        # Create a subscriber to the joint states topic
        self.subscription = self.create_subscription(
            JointState,
            '/joint_states',
            self.joint_state_callback,
            10
        )

    def joint_state_callback(self, msg):
        for i in range(self.robot_chain.getNrOfJoints()):
            self.joint_positions[i] = msg.position[i]

        # Calculate the end effector position
        end_effector_frame = kdl.Frame()
        self.fk_solver.JntToCart(self.joint_positions, end_effector_frame)

        # Output the end effector position
        self.get_logger().info(
            f"End Effector Position: x={end_effector_frame.p.x()} y={end_effector_frame.p.y()} z={end_effector_frame.p.z()}"
        )

def main(args=None):
    rclpy.init(args=args)

    node = EndEffectorPosition()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
