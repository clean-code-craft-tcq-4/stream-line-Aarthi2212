#define CATCH_CONFIG_MAIN
#include "BMS_Receiver.hpp"
#include "test/catch.hpp"
#include <iostream>
#include <vector>
#include <unistd.h>
using namespace std;

ofstream myfile;

TEST_CASE("TestTemperatureSensorValues")
{
  myfile.open ("testFile.txt");
  myfile <<"   49 , 98     "<<endl;
  myfile <<"   81 , 38     "<<endl;
  myfile <<"  -94 , 24     "<<endl;
  myfile <<"  -59 , 35     "<<endl;
  myfile <<"  -65 , 77     "<<endl;
  myfile <<"  -77 , 1      "<<endl;
  myfile <<"  -53 , 13     "<<endl;
  myfile <<"   23 , 24  "<<endl;
  myfile.close();
  BMS_ReadData readSensor; 
  readSensor.BMS_ReadSensorData();

  BMS_SensorStatistics statistics = readSensor.BMS_getSensorStatistics(SENSOR_TEMPERATURE);
  REQUIRE(statistics.min==-94);
  REQUIRE(statistics.max==81);
  REQUIRE(statistics.average==-46);

  statistics = readSensor.BMS_getSensorStatistics(SENSOR_SOC);
  REQUIRE(statistics.min==1);
  REQUIRE(statistics.max==98);
  REQUIRE(statistics.average==30);
}

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