from Constants import INVALID_SENSOR, TOTAL_READINGS_TO_READ
SENSOR_TYPE = "SENSOR_TYPE"
TEMPERATURE = "TEMPERATURE"
SOC = "SOC"
ROC = "ROC"
RANGE = "RANGE"
EXCEPTION = "EXCEPTION"
TOTAL_EXPECTED_READINGS = "TOTAL_EXPECTED_READINGS"

sensor_ranges = [
    {
        SENSOR_TYPE : TEMPERATURE,
        RANGE: (-100, 100)
    },
    {
        SENSOR_TYPE : SOC,
        RANGE: (0, 100)
    }
]

invalid_sensor = [
    {
        SENSOR_TYPE : ROC,
        RANGE: (None, None),
        EXCEPTION: INVALID_SENSOR
    }
]

validate_readings = [
    {
        SENSOR_TYPE : TEMPERATURE,
        TOTAL_EXPECTED_READINGS : TOTAL_READINGS_TO_READ,
        RANGE : range(-100, 100)
    },
    {
        SENSOR_TYPE : SOC,
        TOTAL_EXPECTED_READINGS : TOTAL_READINGS_TO_READ,
        RANGE : range(0, 100)
    }
]