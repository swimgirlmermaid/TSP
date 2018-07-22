# Traveling Salesman Problem (TSP)

A salesman who wishes to travel around is given set of cities. He wishes to travel around and return to the beginning, covering the smallest total distance while only passing through each city once. 

## Getting Started

These instructions will get your project up and running on your local machine for development and testing purposes. 

### Data File Structure 
All datafiles accepted for this application are in  CSV format. The datafiles are structured as follows: 

Name | Long | Lat  
------------ | ------------- | -------------
Albany | 43 | 25
Athens | 23 | 3
Chicago | 16 | 22

This example, from data_0.csv shows each file contains a header column with Name, Long, and Lat followed by the data. The first column is the name of the city, the second column is the longitude, and the third column is the latitude. 

### Data Cleaning
When importing the data provided, there were some rows that were shifted improperly due to an added string value, as seen in the image below. This was manually by moving the longitude and latitude values over and removing the added string. For larger datasets, this should be done programmically.  

![data cleaning](/images/cleaned_data.jpg)

### Prerequisites

This project runs on Python 3 and pip3 for installs. The code requires the following dependencies to be installed: 

```
pip3 install colorama 
pip3 install matplotlib
```

### Installing

To run the code below, download the zipfile and open it up. Using command line on Mac, navigate to the project directory. Run the following command and specify the file when prompted: 

```
python3 Main.py
```

**Example:** 

```
$ python3 Main.py
Enter filename (with no extension): data_0
```

The following image will appear as the graphed tour route. Once closed the progarm will finish by printing the route and calculated distance on screen. 

![sample tour result](/images/sample.jpg)

```
Route: ([43.0, 25.0], [23.0, 3.0], [16.0, 22.s0]) 
Minimum distance: 47.4
```

### Application Logs 
Application logs are sent to `logs/app_log.txt` when the program runs. The default for application logging in this app is WARNING level logs but this can be changed. This means INFO logs will not be seen but ERROR logs will be when produced.  

This can be changed on Line 88 of graph_tsp.py in the line  `logging.basicConfig(level=logging.WARNING)`. 

Logging options are as follows: 

Level | Numeric value
------------ | ------------- 
CRITICAL | 50
ERROR | 40
WARNING	| 30
INFO | 20
DEBUG | 10
NOTSET | 0

### Future Work 
After completing this problem, some future work that could be done to further improve the output is: 
1. Evaluating for lines that do not cross over one another. 
2. Applying real-world data to the graphing problem and displaying this on a world map.  
3. Evaluate methods to optimize the solution.
4. Introduce a data cleaning method that will clean and format the data in a programmic way. 