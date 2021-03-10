-------------------------------------------------------------
# maps_calculator
Bot to calculate normal and custom trip conditions
-------------------------------------------------------------

<p align="center">
  <img src=".//gif/maps_calculator.gif" alt="Size Limit CLI" width="400">
</p>



# Table of Contents

- [Foundations](#Foundations)
- [Installation](#installation)
- [Dependencies](#Dependencies)
- [User Guide](#User-Guide)
- [TODO](#TODO)
- [Disclaimer](#Disclaimer)
- [Author](#Author)



## Foundations

Using Google Maps data, this bot calculates normal trip conditions (distance, time and mean speed). Also, this bot calculates time constrain trips (time defined by the user). Finally, the bot suggests the type of trip and a means of transportation other than car, if applicable.

The user should pass the starting point (current place), the destination and the time she/he allocates for this trip.


## Installation

Download from [here](https://github.com/fermendi/maps_calculator/archive/main.zip) or using git clone:

```
$ git clone https://github.com/fermendi/maps_calculator.git
```

Install `Python 3.6.9` (Jan 26 2021) or later (In Linux it is already installed in `/usr/bin/python3` or `/usr/bin/python3.6`).


## Dependencies

Install `pip`, the package-management system used to install and manage software packages for Python. For more details, click [here](https://pypi.org/project/pip/) 

```
$ sudo apt-get update
$ sudo apt-get install python3-pip
```

Install the `Selenium` package, a free and open-source automated testing framework used in this project as a scraping tool, but it is also used for validating web applications across different browsers. 

```
$ pip3 install selenium
```

Selenium requires a driver to interface with the chosen browser. Google Chrome driver is available [here](https://sites.google.com/a/chromium.org/chromedriver/downloads). See the version of your Google Chrome browser before download the driver. See this [explanation](https://selenium-python.readthedocs.io/installation.html) for more details.


## User Guide

The command to execute the program has the following form:

```
$ maps_calculator.py
```

Then the program will ask you to fill the following parameters using the terminal:

```
Define current place: CURRENT_PLACE
Define destination place: DESTINATION_PLACE
Define your allocated time (ex. 1 hr 10 min, 2.5 hr, 45 min): ALLOCATED_TIME
```

Likewise, you can fill them in the command line:

```
$ maps_calculator.py -c CURRENT_PLACE -d DESTINATION_PLACE -t ALLOCATED_TIME
```

Please see the description of the parameters below:

- `CURRENT_PLACE`: The starting point of the trip. The format of this variable is a string.

- `DESTINATION_PLACE`: The destination place of the trip. The format of this variable is a string.

- `ALLOCATED_TIME`: The duration of the trip according the user needs. The format of this variable is a string that uses `hr` and/or `min` as units. For example, `1 hr 10 min`, `2.5 hr`, `45 min`, etc. The allocate time does not consider stops in the trip.


#### Examples

##### Example 1: The user would like to go from `Lisbon` to `Moscow`, in `30 hr`:

```
$ maps_calculator.py -c "Lisbon" -d "Moscow" -t "30 hr"
```

A similar result of this command can be found below:

```
----------------------------------------------------------------------
maps_calculator: Bot to calculate normal and custom trip conditions.
Fernando Mendiburu - 2021
----------------------------------------------------------------------
Init driver...
Load Google Maps ...
Defining language: English ...
Load Google Maps ...
Defining language: English ...
Set navigational function ...
Defining transport: Car ...
Defining place: lisbon ...
Defining place: moscow ...
Getting the trip description ...

----------------------------------------------------------------------
Normal conditions:
Lisbon Portugal -> Moscow Russia
Transport: Car
Normal duration: 46.0 hr. Distance: 4563.0 km
Normal conditions: Stops are not considered. It will take you more time!
Mean speed: 99.2 km/h.
----------------------------------------------------------------------

----------------------------------------------------------------------
Your conditions:
Lisbon Portugal -> Moscow Russia
Transport: Car
Your duration: 30.0 hr. Distance: 4563.0 km
Your conditions: Stops are not considered. It will take you more time!
Mean speed: 152.1 km/h.
----------------------------------------------------------------------

----------------------------------------------------------------------
Observations:
You should go faster (dangerously?) than normal trip.
A suggested transport could be: Tesla Roadster!
----------------------------------------------------------------------
End program successfully!
Exit program!
```

##### Example 2: The user would like to go from `olinda, pe` to `açude velho campina grande`, in `4 hr`:

```
$ maps_calculator.py 
```

After filling the parameters, you will have a similar result to the result below:

```
----------------------------------------------------------------------
maps_calculator: Bot to calculate normal and custom trip conditions.
Fernando Mendiburu - 2021
----------------------------------------------------------------------
Define current place: olinda, pe
Define destination place: açude velho campina grande
Define your allocated time (ex. 1 hr 10 min, 2.5 hr, 45 min): 4 hr
Init driver...
Load Google Maps ...
Defining language: English ...

Error getting the information from Google maps!:
Problem to define the language!, Increase delay and reloading ...
Set new time step: 5s!
Load Google Maps ...
Defining language: English ...
Set navigational function ...
Defining transport: Car ...
Defining place: olinda, pe ...
Defining place: açude velho campina grande ...
Getting the trip description ...

----------------------------------------------------------------------
Normal conditions:
Olinda PE, Brazil -> Açude Velho Centro, Campina Grande - State of Paraíba, Brazil
Transport: Car
Normal duration: 3.15 hr. Distance: 226.0 km
Mean speed: 71.75 km/h.
----------------------------------------------------------------------

----------------------------------------------------------------------
Your conditions:
Olinda PE, Brazil -> Açude Velho Centro, Campina Grande - State of Paraíba, Brazil
Transport: Car
Your duration: 4.0 hr. Distance: 226.0 km
Mean speed: 56.5 km/h.
----------------------------------------------------------------------

----------------------------------------------------------------------
Observations:
Enjoy the trip and be careful!
----------------------------------------------------------------------
End program successfully!
Exit program!
```

Using this command you will have the same result as the above result:

```
$ maps_calculator.py -c "olinda, pe" -d "açude velho campina grande" -t "4 hr"
```

Please note that when there are problems to get the information from Google maps, a new time step is applied.

## TODO

Using this base program it is possible to add the same functionalities of Google Maps and work on top of it. For example:

- Choosing between several means of transport, such as bus, plane, walk, among others. 
- Including stops in the duration of the trip.
- Choosing among all the place suggestion given by Google Maps.
- Selecting among all the possible routes for the trip.
- Adding decision making capabilities to recommend realistic trips, stops when neccesary, places to stay ...
- Etc. 

## Disclaimer

The main purpose of this repository is to produce a simple calculator and show how to collect data from websites for research and personal projects. Google Maps data may be subject to copyright and should not be used for commercial purposes. This program should not be considered an advisory bot to produce a reliable trip.

## Author

Fernando Mendiburu - 2021

fernando.mendiburu@ee.ufcg.edu.br






