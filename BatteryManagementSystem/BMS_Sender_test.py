import unittest
from unittest.mock import patch
from io import StringIO
import sys
import test_data
from BMSSensors import BMSSensors

STD_OUT = 'sys.stdout'

class BMSSensorTest(unittest.TestCase):
  def __init__(self, method_name: str = ...) -> None:
    super().__init__(method_name)
    self.bms_sensors = BMSSensors()

  def test_sensor_reading_ranges(self):
    for test in test_data.sensor_ranges:
      self.assertEqual(self.bms_sensors.get_ranges_by_type(test.get(test_data.SENSOR_TYPE)), test.get(test_data.RANGE))
    for test in test_data.invalid_sensor:
        with patch(STD_OUT, new = StringIO()) as fake_out:
            self.bms_sensors.get_ranges_by_type(test.get(test_data.SENSOR_TYPE))
            self.assertEqual(fake_out.getvalue().strip(), test.get(test_data.EXCEPTION))
        self.assertEqual(self.bms_sensors.get_ranges_by_type(test.get(test_data.SENSOR_TYPE)), test.get(test_data.RANGE))

  def test_simulated_sensor_readings(self):
    for test in test_data.validate_readings:
      self.assertEqual(len(self.bms_sensors.read_data(test.get(test_data.SENSOR_TYPE))), test.get(test_data.TOTAL_EXPECTED_READINGS))
      self.assertEqual(all(x in [i for i in test.get(test_data.RANGE)] for x in self.bms_sensors.read_data(test.get(test_data.SENSOR_TYPE))), True)

if __name__ == '__main__':
  sys.exit(unittest.main()) # pragma: no cover
