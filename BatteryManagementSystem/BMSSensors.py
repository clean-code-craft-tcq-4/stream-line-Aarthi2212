import random
from Constants import SENSOR_RANGES, MAX, MIN, TOTAL_READINGS_TO_READ, INVALID_SENSOR

class BMSSensors:

    def __init__(self) -> None:
        self.sensor_ranges = SENSOR_RANGES

    def get_ranges_by_type(self, sensor_type):
        sensor_min_value, sensor_max_value = None, None
        try:
            sensor_max_value =  self.sensor_ranges.get(sensor_type).get(MAX)
            sensor_min_value = self.sensor_ranges.get(sensor_type).get(MIN)
        except Exception:
            print(INVALID_SENSOR)
        return sensor_min_value, sensor_max_value
    
    def read_data(self, sensor_type):
        sensor_min_value, sensor_max_value = self.get_ranges_by_type(sensor_type)
        return [random.randint(sensor_min_value, sensor_max_value) for x in range(TOTAL_READINGS_TO_READ)]


BMSSensors().get_ranges_by_type("ROC")