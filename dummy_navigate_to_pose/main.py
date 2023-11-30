import rclpy

from rclpy.node import Node
from rclpy.exceptions import ROSInterruptException

from .node.dummy_node import DummyNavigateToPose


def main(args=None) -> None:
    rclpy.init(args=args)
    
    try:
        node: Node = DummyNavigateToPose()
        node_name: str = node.get_name()
        rclpy.spin(node)
    except ROSInterruptException as rie:
        node.get_logger().warn(f'===== [{node_name}] terminated with Ctrl-C {rie} =====')
    
    node.destroy_node()
    rclpy.shutdown()
    

if __name__ == '__main__':
    main()    