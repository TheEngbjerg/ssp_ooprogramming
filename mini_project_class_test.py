import mini_project_classes as mpc

sensor_1_data = mpc.DatabaseCollection()

sensor_1 = mpc.CO2Sensor('CO2_1', sensor_1_data, 0, serial_port='COM3')
for _ in range(100):
    sensor_1.measure()

data = sensor_1_data.get_data()
print(data)