# This is a sample Python script.
import sys
from dronekit import connect
from pymavlink import mavutil
from new_mav import  *
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#mavutil.set_dialect()

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
def send_msg():
    the_connection=mavutil.mavlink_connection("/dev/ttyUSB0",baud=57600)
    the_connection.mav.heartbeat_send(mavutil.mavlink.MAV_TYPE_ONBOARD_CONTROLLER,mavutil.mavlink.MAV_AUTOPILOT_INVALID, 1, 0, 0)
    #msg=MAVLink_message(1111,"KEY")

    #the_connection.mav.send(msg)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    send_msg()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
