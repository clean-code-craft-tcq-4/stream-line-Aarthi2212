#include "BMS_Receiver.hpp"

#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <numeric>

using namespace std;

BMS_ReadData::BMS_ReadData()
{
}
BMS_ReadData::~BMS_ReadData(){};

void BMS_ReadData::BMS_ReadSensorData(void)
{
    int temperature, soc;
    ifstream file("testFile.txt", ios::in);
    if (file.good())
    {
        string data = "";
        // while(getline(file, data,','))
        while (getline(file, data))
        {
            data.erase(std::remove(data.begin(), data.end(), ','), data.end());
            istringstream ss(data);
            while (ss >> temperature >> soc)
            {
                cout << "Temp: " << temperature << " Soc: " << soc << endl;
                SensorValues[SENSOR_TEMPERATURE].push_back(temperature);
                SensorValues[SENSOR_SOC].push_back(soc);
            }
            calculateSensorStatistics();
        }
    }
}

void BMS_ReadData::calculateSensorStatistics()
{
    for (int index = 0; index < (int)SensorValues[SENSOR_TEMPERATURE].size(); index++)
    {
        for (int sensor = 0; sensor < SENSOR_MAX; sensor++)
        {

            sensorStatistics[sensor].max = *max_element(SensorValues[sensor].begin(), SensorValues[sensor].end());
            sensorStatistics[sensor].min = *min_element(SensorValues[sensor].begin(), SensorValues[sensor].end());
            if (SensorValues[SENSOR_TEMPERATURE].size() <= RUNNING_AVERAGE_COUNT)
            {
                sensorStatistics[sensor].average = accumulate(SensorValues[sensor].begin(), SensorValues[sensor].end(), 0) / SensorValues[SENSOR_TEMPERATURE].size();
            }
            else
            {
                sensorStatistics[sensor].average = accumulate(SensorValues[sensor].end() - RUNNING_AVERAGE_COUNT, SensorValues[sensor].end(), 0) / RUNNING_AVERAGE_COUNT;
            }
        }
    }
}

BMS_SensorStatistics BMS_ReadData::BMS_getSensorStatistics(BMS_Sensors sensor)
{
    return sensorStatistics[sensor];
}
