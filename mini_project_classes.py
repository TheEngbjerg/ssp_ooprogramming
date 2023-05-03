""" This module is made for our mini project.

It contains all classes of the project.

"""
import random

class DatabaseCollection():
    """ The DatabaseCollection class is used for generating a .txt file and
    storing measurements from sensors in the file.

    """

    def __init__(self) -> None:
        self.sensor_id = None

    def get_data(self):
        """ Opens the .txt file with data, and reads each line.

        Returns:
            list[float]: data

        """
        with open(f'{self.sensor_id}.txt', 'r') as fd:
            data = [float(line) for line in fd.readlines()]
        return data

    def add_data(self, data):
        """ Opens the .txt file with data, and writes new data.

        Args:
            data (float): sensor measurement

        """
        with open(f'{self.sensor_id}.txt', 'a') as fd:
            fd.write(str(data)+'\n')

class Sensor():
    """ The Sensor class is used as a parent class for the different types of
    sensors used in the system.
    """

    def __init__(self, sensor_id, database, connection_mode,
                 serial_port=None, address=None, port=None) -> None:
        self.sensor_id = sensor_id
        self.database: DatabaseCollection = database
        self.database.sensor_id = self.sensor_id
        if connection_mode == 0 and serial_port:
            self.receiver = serial_port
        elif connection_mode == 1 and address and port:
            self.receiver = (address, port)
        else:
            raise ValueError('connection_mode error.')

    def measure(self, data):
        """ Adds measurement to database file.

        Args:
            data (float): sensor measurement

        """
        self.database.add_data(data)

class TempSensor(Sensor):
    """ The TempSensor class is used for creating a temperature sensor
    objects.

    """

    def __init__(self, sensor_id, database, connection_mode, serial_port=None,
                 address=None, port=None) -> None:
        super().__init__(sensor_id, database, connection_mode,
                         serial_port, address, port)

    def measure(self):
        """ Makes a hypothetical measurement of the temperature. Then uses 
        the parent method "measure" to write the data to database.

        """
        data = random.uniform(16, 24)
        super().measure(data)

class HumidSensor(Sensor):
    """ The HumidSensor class is used for creating a humidity sensor objects.

    """

    def __init__(self, sensor_id, database, connection_mode, serial_port=None,
                 address=None, port=None) -> None:
        super().__init__(sensor_id, database, connection_mode,
                         serial_port, address, port)

    def measure(self):
        """ Makes a hypothetical measurement of the humidity. Then uses 
        the parent method "measure" to write the data to database.

        """
        data = random.uniform(0, 17.3)
        super().measure(data)

class CO2Sensor(Sensor):
    """ The CO2Sensor class is used for creating a CO2 sensor objects.

    """

    def __init__(self, sensor_id, database, connection_mode, serial_port=None,
                 address=None, port=None) -> None:
        super().__init__(sensor_id, database, connection_mode,
                         serial_port, address, port)

    def measure(self):
        """ Makes a hypothetical measurement of the CO2 level. Then uses 
        the parent method "measure" to write the data to database.

        """
        data = random.uniform(200, 8000)
        super().measure(data)
