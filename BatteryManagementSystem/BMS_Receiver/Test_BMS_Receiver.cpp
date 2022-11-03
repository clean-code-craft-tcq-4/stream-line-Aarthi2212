#define CATCH_CONFIG_MAIN
#include "BMS_Receiver.hpp"
#include "test/catch.hpp"
#include <iostream>
#include <vector>
#include <unistd.h>
using namespace std;

TEST_CASE("TestTemperatureSensorValues")
{
  BMS_ReadData readSensor; 
  readSensor.BMS_ReadSensorData();

}
