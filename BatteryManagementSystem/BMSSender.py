from BMSSensors import BMSSensors
from Constants import STANDARD_FORMAT, TEMPERATURE, SOC, WIDTH
class BMSSender:
    def __init__(self, number_of_readings = None) -> None:
        self.sensors_supported = []
        self.bms_sensors = BMSSensors()
        self.standard_output = []
        self.number_of_readings = number_of_readings
        if number_of_readings is None:
            self.number_of_readings = 50       

    def configure_sensors(self, sensors):
        [self.sensors_supported.append(sensor) for sensor in sensors if sensor not in self.sensors_supported]
    
    def read_sensors_data(self, number_of_readings):
        sensor_readings = {}
        for sensor in self.sensors_supported:
            readings = self.bms_sensors.read_data(sensor, number_of_readings)
            sensor_readings.update({sensor: readings})
        return sensor_readings

    def standardize_output(self, headers, readings):
        self.standard_output = []
        self.standard_output.append(STANDARD_FORMAT.format(*headers, width=WIDTH))
        for reading in readings:
            self.standard_output.append(STANDARD_FORMAT.format(*reading, width=WIDTH))

    def output_readings(self):
        for output in self.standard_output:
            print(output)

    def preprocess(self, sensor_readings):
        self.standardize_output(tuple(sensor_readings.keys()), \
            list(zip(*sensor_readings.values())))

    def send_data(self):
        sensor_readings = self.read_sensors_data(self.number_of_readings)
        self.preprocess(sensor_readings)
        self.output_readings()


if __name__ == '__main__':
    bms_sender = BMSSender()
    bms_sender.configure_sensors([TEMPERATURE, SOC])
    bms_sender.send_data()


