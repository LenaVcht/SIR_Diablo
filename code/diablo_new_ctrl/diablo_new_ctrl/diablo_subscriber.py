# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node

from motion_msgs.msg import MotionCtrl  # Import du message MotionCtrl



class MotionCommandSubscriber(Node):

    def __init__(self):
        super().__init__('motion_command_subscriber')
        self.subscription = self.create_subscription(
            MotionCtrl,
            '/diablo/MotionCmd',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        # Construction d'un log détaillé avec tous les champs du message
        log_message = (
            f"I heard:\n"
            f"  mode_mark: {msg.mode_mark}\n"
            f"  value:\n"
            f"    forward: {msg.value.forward}\n"
            f"    left: {msg.value.left}\n"
            f"    up: {msg.value.up}\n"
            f"    roll: {msg.value.roll}\n"
            f"    pitch: {msg.value.pitch}\n"
            f"    leg_split: {msg.value.leg_split}\n"
            f"  mode:\n"
            f"    pitch_ctrl_mode: {msg.mode.pitch_ctrl_mode}\n"
            f"    roll_ctrl_mode: {msg.mode.roll_ctrl_mode}\n"
            f"    height_ctrl_mode: {msg.mode.height_ctrl_mode}\n"
            f"    stand_mode: {msg.mode.stand_mode}\n"
            f"    jump_mode: {msg.mode.jump_mode}\n"
            f"    split_mode: {msg.mode.split_mode}\n"
        )
        # Affichage du log
        self.get_logger().info(log_message)

def main(args=None):
    rclpy.init(args=args)

    motion_command_subscriber = MotionCommandSubscriber()

    rclpy.spin(motion_command_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    motion_command_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
