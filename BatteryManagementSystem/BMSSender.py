from BMSSensors import BMSSensors
from Constants import STANDARD_FORMAT
class BMSSender:
    def __init__(self) -> None:
        self.sensors_supported = []
        self.bms_sensors = BMSSensors()
        self.standard_output = []

    def configure_sensors(self, sensors):
        self.sensors_supported.extend(sensors)
    
    def read_sensors_data(self):
        sensor_readings = {}
        for sensor in self.sensors_supported:
            readings = self.bms_sensors.read_data(sensor)
            sensor_readings.update({sensor: readings})
        return sensor_readings

    def standardize_output(self, headers, readings):
        self.standard_output.append(STANDARD_FORMAT.format(*headers, width=11))
        for reading in readings:
            self.standard_output.append(STANDARD_FORMAT.format(*reading, width=11))

    def output_readings(self):
        for output in self.standard_output:
            print(output)

    def preprocess(self, sensor_readings):
        self.standardize_output(tuple(sensor_readings.keys()), \
            list(zip(*sensor_readings.values())))

    def send_data(self):
        sensor_readings = self.read_sensors_data()
        self.preprocess(sensor_readings)
        self.output_readings()


if __name__ == '__main__':
    bms_sender = BMSSender()
    bms_sender.configure_sensors(["TEMPERATURE", "SOC"])
    bms_sender.send_data()


