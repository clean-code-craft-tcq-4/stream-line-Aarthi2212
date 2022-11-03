#pragma once

#include <vector>
#include <stdio.h>
using namespace std;

#define RUNNING_AVERAGE_COUNT    5

typedef enum
{
    SENSOR_TEMPERATURE,
    SENSOR_SOC,
    SENSOR_MAX
} BMS_Sensors;

typedef struct
{
    int min;
    int max;
    int average;
} BMS_SensorStatistics;

class BMS_ReadData
{
    vector<int> SensorValues[SENSOR_MAX];
    vector<int> socSensor;
    BMS_SensorStatistics sensorStatistics[SENSOR_MAX];
    void calculateSensorStatistics(void);

public:
    BMS_ReadData();
    ~BMS_ReadData();
    void BMS_ReadSensorData(void);
};
