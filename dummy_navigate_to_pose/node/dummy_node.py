import time

from rclpy.node import Node
from rclpy.action import ActionServer
from rclpy.action.server import ServerGoalHandle

from nav2_msgs.action import NavigateToPose


RCLPY_NODE_NAME: str = 'dummy_navigate_to_pose'
RCLPY_ACTION_SERVER_NAME: str = 'navigate_to_pose'

class DummyNavigateToPose(Node):
    
    def __init__(self) -> None:
        super().__init__(RCLPY_NODE_NAME)
        self.get_logger().info(f'===== [{RCLPY_NODE_NAME}] created =====')
        
        self.action_server = ActionServer(
            node = self,
            action_type = NavigateToPose,
            action_name = RCLPY_ACTION_SERVER_NAME,
            execute_callback = self.execute_cb
        )
        
    
    def execute_cb(self, goal_handle: ServerGoalHandle) -> NavigateToPose.Result:
        self.get_logger().info(f'{RCLPY_NODE_NAME} request goal : {goal_handle.request}')
        sleep_seconds: float = 5.0
        time.sleep(secs = sleep_seconds)
        goal_handle.succeed()
        result: NavigateToPose.Result = NavigateToPose.Result()
        return result