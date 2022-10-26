# Python Imports

# ROS Imports
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from sensor_msgs.msg import Imu

# IMU Imports
import adafruit_gy85
import board
from adafruit_extended_bus import ExtendedI2C as I2C
#i2c = board.I2C()
i2c = I2C(1)
sensor = adafruit_bno055.BNO055_I2C(i2c)


class IMUPublisher(Node):

    def __init__(self):
        super().__init__('imu_publisher')

        # Remind user to start PiGPIO Library
        print("Remember to start PiGPIO Libs using: sudo pigpiod")

        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        imu_msg = Imu()

        # print(sensor.temperature)
        # print(sensor.euler)
        # print(sensor.gravity)

        print("Accelerometer (m/s^2): {}".format(sensor.acceleration))
        print("Magnetometer (microteslas): {}".format(sensor.magnetic))
        print("Gyroscope (rad/sec): {}".format(sensor.gyro))
        print("Euler angle: {}".format(sensor.euler))
        print("Quaternion: {}".format(sensor.quaternion))
        print("Linear acceleration (m/s^2): {}".format(sensor.linear_acceleration))
        print("Gravity (m/s^2): {}".format(sensor.gravity))
        print()

        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = IMUPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
