#!/usr/bin/env python3

import rospy
import asyncio
import numpy as np

from spatialmath import SE3, Twist3
from armer_robot import Robot

async def main():
  robot = Robot()
  
  await robot.move_to(SE3.Tx(0.1) * SE3.Tz(0.4) * SE3.Ty(0.4) * SE3.Rx(np.pi), speed=0.4)
  
  await robot.home(speed=0.4)
  
  motion = robot.move_at(Twist3.Ry(-0.3))
  await asyncio.sleep(2)
  motion.cancel()

  motion = robot.move_at(Twist3.Tz(0.05) * Twist3.Rz(0.5), frame_id=robot.ee_link)
  await asyncio.sleep(2)
  motion.cancel()

  robot.set_frame(robot.ee_link)
  
  motion = robot.move_at(Twist3.Tz(-0.05) * Twist3.Rz(-0.5))
  await asyncio.sleep(2)
  motion.cancel()

  await asyncio.sleep(0.5)
  
  future = robot.home()
  future.add_done_callback(lambda f: print(f'{f.result()}'))
  await future
    
if __name__ == '__main__':
  rospy.init_node('test')
  asyncio.run(main())
