from Constants import INVALID_SENSOR, STANDARD_FORMAT, WIDTH
SENSOR_TYPE = "SENSOR_TYPE"
TEMPERATURE = "TEMPERATURE"
SOC = "SOC"
ROC = "ROC"
RANGE = "RANGE"
EXCEPTION = "EXCEPTION"
TOTAL_EXPECTED_READINGS = "TOTAL_EXPECTED_READINGS"
TOTAL_READINGS_TO_READ = "TOTAL_READINGS_TO_READ"
SENSORS_INPUT = "SENSORS_INPUT"
HEADERS = "HEADERS"
SENSOR_READINGS = "SENSOR_READINGS"
SENSORS_CONFIGURED = "SENSORS_CONFIGURED"
SENSORS_AVAILABLE = "SENSORS_AVAILABLE"
SENSORS = [TEMPERATURE, SOC]
READING1 = (-10, 30)
READING2 = (100, 50)
STANDARD_OUTPUT = "STANDARD_OUTPUT"
DATA_TO_BE_SENT = "DATA_TO_BE_SENT"
STANDARD_OUTPUT_READINGS = [STANDARD_FORMAT.format(*SENSORS, width=WIDTH),
                          STANDARD_FORMAT.format(*READING1, width=WIDTH),
                          STANDARD_FORMAT.format(*READING2, width=WIDTH)]
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
        TOTAL_READINGS_TO_READ : 40,
        TOTAL_EXPECTED_READINGS : 40,
        RANGE : range(-100, 101) # excludes upper limit
    },
    {
        SENSOR_TYPE : SOC,
        TOTAL_READINGS_TO_READ : 25,
        TOTAL_EXPECTED_READINGS : 25,
        RANGE : range(0, 101) # excludes upper limit
    }
]

sensor_configuration = [
    {
        SENSORS_INPUT : SENSORS,
        SENSORS_CONFIGURED : SENSORS
    }
]

validate_read_data = [
    {
        SENSORS_AVAILABLE: SENSORS,
        TOTAL_READINGS_TO_READ: 60,
        TOTAL_EXPECTED_READINGS: 60
    }
]

validate_standardization = [
    {
        HEADERS : SENSORS,
        SENSOR_READINGS : [READING1, READING2],
        STANDARD_OUTPUT: STANDARD_OUTPUT_READINGS
    }
]

validate_preprocess = [
    {
        SENSOR_READINGS : {TEMPERATURE:[-10, 100], SOC: [30, 50]},
        STANDARD_OUTPUT: STANDARD_OUTPUT_READINGS
    }
]

validate_output = [
    {
        STANDARD_OUTPUT: STANDARD_OUTPUT_READINGS,
        DATA_TO_BE_SENT: "\n".join(STANDARD_OUTPUT_READINGS) +"\n"
    }
]

validate_send_data = [
    {
        TOTAL_READINGS_TO_READ: 50,
        TOTAL_EXPECTED_READINGS: 50
    },
    {
        TOTAL_READINGS_TO_READ: 100,
        TOTAL_EXPECTED_READINGS: 100
    }
]