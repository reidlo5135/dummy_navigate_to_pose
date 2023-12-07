from rclpy.node import Node
from rclpy.action import ActionServer
from rclpy.timer import Timer
from rclpy.action.server import ServerGoalHandle
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup

from nav2_msgs.action import NavigateToPose


RCLPY_NODE_NAME: str = 'dummy_navigate_to_pose'
RCLPY_ACTION_SERVER_NAME: str = 'navigate_to_pose'

class DummyNavigateToPose(Node):
    
    def __init__(self) -> None:
        super().__init__(RCLPY_NODE_NAME)
        self.get_logger().info(f'===== [{RCLPY_NODE_NAME}] created =====')
        
        self.action_server_cb_group: MutuallyExclusiveCallbackGroup = MutuallyExclusiveCallbackGroup()
        self.action_server: ActionServer = ActionServer(
            node = self,
            action_type = NavigateToPose,
            action_name = RCLPY_ACTION_SERVER_NAME,
            execute_callback = self.action_server_execute_cb,
            callback_group=self.action_server_cb_group
        )
        
        self.count: int = 0
        self.timer_cb_group: MutuallyExclusiveCallbackGroup = MutuallyExclusiveCallbackGroup()
        self.timer_period_sec: float = 1.0
        self.timer: Timer = self.create_timer(
            timer_period_sec=self.timer_period_sec,
            callback_group=self.timer_cb_group,
            callback=self.timer_cb
        )
        
    
    def action_server_execute_cb(self, goal_handle: ServerGoalHandle) -> NavigateToPose.Result:
        self.get_logger().info(f'{RCLPY_NODE_NAME} request goal : {goal_handle.request}')
        
        goal_handle.succeed()
        result: NavigateToPose.Result = NavigateToPose.Result()
        return result
            

    
    def timer_cb(self) -> None:
        self.count += 1