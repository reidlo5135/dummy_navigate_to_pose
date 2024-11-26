import time;
import asyncio;
from rclpy.node import Node;
from rclpy.action import ActionServer, GoalResponse, CancelResponse;
from rclpy.action.server import ServerGoalHandle;
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup;

from nav2_msgs.action import NavigateToPose


RCLPY_NODE_NAME: str = 'dummy_navigate_to_pose'
RCLPY_ACTION_SERVER_NAME: str = 'navigate_to_pose'

class DummyNavigateToPose(Node):
    
    def __init__(self) -> None:
        super().__init__(RCLPY_NODE_NAME);
        self.get_logger().info(f'===== [{RCLPY_NODE_NAME}] created =====');
        
        self.action_server_cb_group: MutuallyExclusiveCallbackGroup = MutuallyExclusiveCallbackGroup();
        self.action_server: ActionServer = ActionServer(
            node = self,
            action_type = NavigateToPose,
            action_name = RCLPY_ACTION_SERVER_NAME,
            goal_callback = self.goal_callback,
            cancel_callback = self.cancel_callback,
            execute_callback = self.execute_cb,
            callback_group=self.action_server_cb_group
        );
    
        self.is_canceled: bool = False;
    
    def goal_callback(self, goal_request):
        self.get_logger().info('Received goal request');
        return GoalResponse.ACCEPT;

    def cancel_callback(self, goal_handle: ServerGoalHandle):
        self.get_logger().info(f'Received cancel request for goal: {goal_handle.goal_id}');
        self.is_canceled = True;
        # goal_handle.canceled();
        return CancelResponse.ACCEPT;
    
    def execute_cb(self, goal_handle: ServerGoalHandle):
        self.get_logger().info(f'Goal received: {goal_handle.request}');
        
        result = NavigateToPose.Result();

        try:
            for i in range(1, 16):
                if self.is_canceled is True:
                    self.get_logger().info(f'Goal {goal_handle.goal_id} was canceled');
                    goal_handle.canceled();
                    return result;
                else:
                    pass;
                self.get_logger().info(f'Executing... {i}');
                time.sleep(1.0);

            goal_handle.succeed();
            self.get_logger().info(f'Goal {goal_handle.goal_id} succeeded');
            return result;

        except Exception as e:
            self.get_logger().error(f'Error occurred: {str(e)}');
            goal_handle.abort();
            return result;
    