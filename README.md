# CO2 Emission by vehicles Prediction

This is ML-based web app which uses multi-variant linear regression model to predict CO2 emitted by vehicles using various parameters like engine size, cylinders, fuel type, etc.

## UI

### Initial Homepage
![Screenshot (60)](https://github.com/dipanshu18/co2_emission_prediction/assets/88198352/a5941330-8074-4768-92f4-2d39559b129c)

### Prediction page
![Screenshot (61)](https://github.com/dipanshu18/co2_emission_prediction/assets/88198352/6b22dd49-5388-4b36-b969-40a529ad4cff)


## Dataset used
The dataset contains the details of how CO2 emissions by a vehicle can vary with the different features. 

There are few abbreviations that has been used to describe the features. I am listing them out here.

### Model

4WD/4X4 = Four-wheel drive
AWD = All-wheel drive
FFV = Flexible-fuel vehicle
SWB = Short wheelbase
LWB = Long wheelbase
EWB = Extended wheelbase

### Transmission

A = Automatic
AM = Automated manual
AS = Automatic with select shift
AV = Continuously variable
M = Manual
3 - 10 = Number of gears

### Fuel type

X = Regular gasoline
Z = Premium gasoline
D = Diesel
E = Ethanol (E85)
N = Natural gas

### Fuel Consumption

City and highway fuel consumption ratings are shown in litres per 100 kilometres (L/100 km) - the combined rating (55% city, 45% hwy) is shown in L/100 km and in miles per gallon (mpg)

**To convert mpg to kmpl**, divide the fuel economy value by **2.352**

### CO2 Emissions

The tailpipe emissions of carbon dioxide (in grams per kilometre) for combined city and highway driving
