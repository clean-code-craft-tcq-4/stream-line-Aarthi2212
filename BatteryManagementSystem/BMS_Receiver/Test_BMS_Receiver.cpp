#define CATCH_CONFIG_MAIN
#include "BMS_Receiver.hpp"
#include "test/catch.hpp"
#include <iostream>
#include <vector>
#include <unistd.h>
using namespace std;

ofstream myfile;

TEST_CASE("TestTemperatureSensorValues_rangeIncreased")
{
  myfile.open ("testFile.txt");

  myfile<<"  -96 , 40    "<<endl;     
  myfile<<"   35 , 23    "<<endl;     
  myfile<<"   -3 , 100   "<<endl;     
  myfile<<"  -18 , 50    "<<endl;     
  myfile<<"  -77 , 96    "<<endl;     
  myfile<<"  -71 , 89    "<<endl;     
  myfile<<"   65 , 58    "<<endl;     
  myfile<<"  -29 , 32    "<<endl;     
  myfile<<"   13 , 61    "<<endl;     
  myfile<<"  -70 , 36    "<<endl;     
  myfile<<"   47 , 24    "<<endl;     
  myfile<<"   -5 , 39    "<<endl;     
  myfile<<"  -60 , 91    "<<endl;     
  myfile<<"  -19 , 22    "<<endl;     
  myfile<<"  -38 , 81    "<<endl;     
  myfile<<"   77 , 59    "<<endl;     
  myfile<<"  -37 , 24    "<<endl;     
  myfile<<"   75 , 60    "<<endl;     
  myfile<<"    0 , 9     "<<endl;     
  myfile<<"   77 , 20    "<<endl;     
  myfile<<"   29 , 3     "<<endl;     

  myfile.close();
  BMS_ReadData readSensor; 
  readSensor.BMS_ReadSensorData();

  BMS_SensorStatistics statistics = readSensor.BMS_getSensorStatistics(SENSOR_TEMPERATURE);
  REQUIRE(statistics.min==-96);
  REQUIRE(statistics.max==77);
  REQUIRE(statistics.average==28);

  statistics = readSensor.BMS_getSensorStatistics(SENSOR_SOC);
  REQUIRE(statistics.min==3);
  REQUIRE(statistics.max==100);
  REQUIRE(statistics.average==23);
}