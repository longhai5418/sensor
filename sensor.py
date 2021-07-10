import time
import paho.mqtt.client as mqtt
import json
import random


def fake_sensor():
    # xyz轴加速度
    accel_x = random.randint(2, 50)
    accel_y = random.randint(2, 50)
    accel_z = random.randint(2, 50)
    # xyz轴陀螺仪
    gyro_x = random.randint(2, 50)
    gyro_y = random.randint(2, 50)
    gyro_z = random.randint(2, 50)
    # 依次为横滚角、俯仰角、航向角
    roll = random.randint(2, 50)
    pitch = random.randint(2, 50)
    yaw = random.randint(2, 50)

    return {'accel_x': accel_x, 'accel_y': accel_y, 'accel_z': accel_z,
            'gyro_x': gyro_x, 'gyro_y': gyro_y, 'gyro_z': gyro_z,
            'pitch': pitch, 'roll': roll, 'yaw': yaw, }

print("start")
client = mqtt.Client("DevTool_Sensor", clean_session=False, transport="websockets")
client.connect("192.168.52.222", 8083)
client.loop_start()
count = 0


while True:
    sensor_data = fake_sensor()
    client.publish("sensor", payload=json.dumps(sensor_data))
    print(sensor_data)
    count += 1
    print(count)
    time.sleep(2)
