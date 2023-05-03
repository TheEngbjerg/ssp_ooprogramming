import mini_project_classes as mpc

sensor_1_data = mpc.DatabaseCollection()
sensor_2_data = mpc.DatabaseCollection()
sensor_3_data = mpc.DatabaseCollection()

sensor_1 = mpc.CO2Sensor('CO2', sensor_1_data, 0, serial_port='COM3')
sensor_2 = mpc.TempSensor('Temperature', sensor_2_data, 0, serial_port='COM4')
sensor_3 = mpc.HumidSensor('Humidity', sensor_3_data, 0, serial_port='COM5')
for _ in range(100):
    sensor_1.measure()
    sensor_2.measure()
    sensor_3.measure()

data_1 = sensor_1_data.get_data()
data_2 = sensor_2_data.get_data()
data_3 = sensor_3_data.get_data()

print(f'CO2 Sensor:\n{data_1}\n\nTemperature Sensor:\n{data_2}\n\nHumidity Sensor:\n{data_3}')