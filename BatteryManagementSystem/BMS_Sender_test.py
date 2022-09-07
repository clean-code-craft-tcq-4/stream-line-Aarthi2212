import unittest
from unittest.mock import patch
from io import StringIO
import sys
from Constants import SOC, TEMPERATURE
import test_data
from BMSSensors import BMSSensors
from BMSSender import BMSSender

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
      self.assertEqual(len(self.bms_sensors.read_data(
        test.get(test_data.SENSOR_TYPE), \
        test.get(test_data.TOTAL_READINGS_TO_READ))), test.get(test_data.TOTAL_EXPECTED_READINGS))
      self.assertEqual(all(x in [i for i in test.get(test_data.RANGE)] for x in self.bms_sensors.read_data(
        test.get(test_data.SENSOR_TYPE), \
        test.get(test_data.TOTAL_READINGS_TO_READ))), True)

class BMSSenderTest(unittest.TestCase):
  def __init__(self, method_name: str = ...) -> None:
    super().__init__(method_name)
    self.bms_sender = BMSSender()
    self.bms_sender.configure_sensors([TEMPERATURE, SOC])
    self.bms_sender.send_data()

  def test_configuring_sensors_to_bms(self):
    for test in test_data.sensor_configuration:
      self.bms_sender.configure_sensors(test.get(test_data.SENSORS_INPUT))
      self.assertEqual(self.bms_sender.sensors_supported, test.get(test_data.SENSORS_CONFIGURED))

  def test_reading_sensors(self):
    for test in test_data.validate_read_data:
      self.assertEqual(list(self.bms_sender.read_sensors_data(test.get(test_data.TOTAL_READINGS_TO_READ)).keys()), test.get(test_data.SENSORS_AVAILABLE))
      self.assertEqual(len(list(self.bms_sender.read_sensors_data(test.get(test_data.TOTAL_READINGS_TO_READ)).values())[0]), test.get(test_data.TOTAL_EXPECTED_READINGS))

  def test_output_standardization(self):
    for test in test_data.validate_standardization:
        self.bms_sender.standardize_output(
        test.get(test_data.HEADERS),
        test.get(test_data.SENSOR_READINGS))
        self.assertEqual(self.bms_sender.standard_output, test.get(test_data.STANDARD_OUTPUT))

  def test_preprocessing(self):
    for test in test_data.validate_preprocess:
        self.bms_sender.preprocess(
        test.get(test_data.SENSOR_READINGS))
        self.assertEqual(self.bms_sender.standard_output, test.get(test_data.STANDARD_OUTPUT))

  def test_readings_output(self):
    for test in test_data.validate_output:
        self.bms_sender.standard_output = test.get(test_data.STANDARD_OUTPUT)
        with patch(STD_OUT, new = StringIO()) as fake_out:
            self.bms_sender.output_readings()
            self.assertEqual(fake_out.getvalue(), test.get(test_data.DATA_TO_BE_SENT))

  def test_send_data(self):
    for test in test_data.validate_send_data:
        with patch(STD_OUT, new = StringIO()) as fake_out:
            self.bms_sender.number_of_readings = test.get(test_data.TOTAL_READINGS_TO_READ)
            self.bms_sender.send_data()
            self.assertEqual(len(fake_out.getvalue().strip().split("\n")), test.get(test_data.TOTAL_EXPECTED_READINGS) + 1)

if __name__ == '__main__':
  sys.exit(unittest.main()) # pragma: no cover
