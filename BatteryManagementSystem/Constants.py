MAX = "Maximum"
MIN = "Minimum"
TEMPERATURE = "TEMPERATURE"
SOC = "SOC"
INVALID_SENSOR = "Given Sensor not supported"
WIDTH = 11

SENSOR_RANGES = {
    TEMPERATURE: {
        MAX: 100,
        MIN: -100
    },
    SOC: {
        MAX: 100,
        MIN: 0
    }
}

STANDARD_FORMAT = '{:>{width}} , {:<{width}}'

