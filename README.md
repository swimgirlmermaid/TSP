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

### Installing and Running Code 

To run the code below, download the zipfile and open it up. Using command line on Mac, navigate to the project directory. Run the following command and specify the file when prompted: 

```
python3 Main.py
```

**Example:** 

```
Roses-MBP-2:TSP Rosie$ python3 Main.py 
Enter filename (with no extension): data_3
```

The first image that appears is the data in its original order. 

![original tour result](/images/original.jpg)

The following image will appear as the graphed tour route. Once closed the progarm will finish by printing the route and calculated distance on screen. 

![sample tour result](/images/sample.jpg)

```
Original Distance: 867.1 
Recommended Tour Route: ([43.0, 25.0], [23.0, 3.0], [22.0, 3.0], [25.0, 3.0], [37.0, 18.0], [18.0, 18.0], [47.0, 24.0], [30.0, 10.0], [16.0, 22.0], [22.0, 19.0], [29.0, 21.0], [29.0, 9.0], [0.0, 7.0], [6.0, 23.0], [30.0, 24.0], [21.0, 18.0], [27.0, 10.0], [9.0, 21.0], [19.0, 19.0], [5.0, 9.0], [31.0, 2.0], [17.0, 27.0], [9.0, 10.0], [21.0, 24.0], [19.0, 16.0], [20.0, 16.0], [19.0, 9.0], [10.0, 10.0], [19.0, 22.0], [42.0, 30.0], [34.0, 7.0], [18.0, 13.0], [42.0, 20.0], [17.0, 40.0], [0.0, 10.0], [40.0, 30.0], [40.0, 19.0], [32.0, 20.0], [46.0, 22.0], [44.0, 31.0], [36.0, 15.0], [21.0, 27.0], [4.0, 29.0], [41.0, 27.0], [1.0, 19.0], [29.0, 25.0], [37.0, 17.0], [45.0, 23.0]) 
Minimum distance: 210.9
Time to Run Application (seconds): 3.6
```

### Application Timing 
In Main.py, the application is timed as it runs once. To change how many runs should be made for timing purposes change Line 13 for `t1.timeit(1)`. This will run the program X amount of times before completing and showing the time for completion.   

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