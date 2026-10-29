#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan 
import math 


class FakeLidarNode(Node):  
    def __init__(self):
        super().__init__("lidar_pub")  
        self.publisher = self.create_publisher(LaserScan,'/scan',10)
        self.timer = self.create_timer(0.1, self.publish_scan )
        self.get_logger().info("Lidar is reading now")
    def publish_scan(self) :
        scan = LaserScan()
        scan.header.stamp = self.get_clock().now().to_msg()
        scan.header.frame_id = "laser_frame "
        scan.angle_min = -math.pi
        scan.angle_max = math.pi
        scan.angle_increment = math.pi / 180.0
        scan.time_increment = 0.0
        scan.scan_time = 0.1
        scan.range_min = 0.1
        scan.range_max = 10.0

        ranges = []
        for i in range(361):
            angle = scan.angle_min + i * scan.angle_increment
            angle_deg = math.degrees(angle)
            distance = 5.0
            # Obstacle 1
            if -70 <= angle_deg <= -50:
                distance = 1.2
            # Obstacle 2
            elif 30 <= angle_deg <= 50:
                distance = 2.0
            ranges.append(float(distance))
            

        scan.ranges = ranges
        self.publisher.publish(scan)



def main(args=None):
    rclpy.init(args=args)
    node = FakeLidarNode()  
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
