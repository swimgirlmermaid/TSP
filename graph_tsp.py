#!/usr/bin/python

# Rosemarie Day 
# 22 July 2018 

from itertools import permutations
import csv
import logging
from colorama import Fore, Back, Style
import matplotlib.pyplot as plt

class graph_tsp(): 
    """
    Summary line
    ----------

    Traveling Salesman Problem to calculate shortest distance for travel. 
    """

    def __init__(self, filename):   
        """
        Summary line
        ----------

        Initilize the TSP graph. 

        Parameters
        ----------
        self : instance attribute 
            Allows for reference to instance attributes in the class. 

        filename : string 
            String of the file that is located in data/ subdirectory. 
            This file ends in csv but csv does not need to be specified in user input.
        """

        try:
            self.logger = self.setupLogger() 
            self.filename = filename

            # Open CSV file and read each row into a list of lists 
            with open('data/' + self.filename + '.csv', newline='') as file:
                reader = csv.reader(file)
                points_original = list(map(list, reader))

            # Remove header column 
            del points_original[0]

            # Remove city index from the points 
            cities = [] 
            for point in points_original: 
                cities.append(point.pop(0)) 

            # Convert string values to float 
            points = []
            for item in points_original:
                point = []
                for values in item:  
                    point.append(float(values)) 
                points.append(point) 
            
            self.logger.info('CSV file data/' + self.filename + '.csv was read...')

            # Print distance 
            print("""Route: {} \nMinimum distance: {}""".format(
                tuple(points),
                '{0:.1f}'.format(self.total_distance(self.calculate_TSP(points)))))

        except Exception as e: 
            self.logger.error(Fore.RED + 'Error reading CSV  data/' + self.filename + '.csv  file... %s' % str(e) + Style.RESET_ALL)
    
    def setupLogger(self):
        """
        Summary line
        ----------

        Set up logger for TSP. 

        Parameters
        ----------
        self : instance attribute 
            Allows for reference to instance attributes in the class. 

        Returns
        -------
        logger
            Logger for use elsewhere in the code to log data. 
        """
        logfile = 'logs/app_log.txt'
        # Format log to add time, level and message 
        logging.basicConfig(level=logging.WARNING)
        logFormatter = logging.Formatter('%(asctime)s - %(levelname)s --: %(message)s')
        logger = logging.getLogger(__name__) 
        # Add handler to send logs to log file 
        handler = logging.FileHandler(logfile)
        handler.setFormatter(logFormatter)
        handler.setLevel(logging.INFO)
        logger.addHandler(handler)
        logger.info('Logs written in %s' % logfile)
        return logger

    def distance(self, point_one, point_two):
        """
        Summary line
        ----------

        Calculate distance between two points.  

        Parameters
        ----------
        self : instance attribute 
            Allows for reference to instance attributes in the class. 

        point1 and point2: list of two elements longitude and latitude 
            Points to calculate the distance between that each contain a longitude and latitude.  

        Returns
        -------
        distance
            Calculated Euclidean distance of the two points.    
        """
        complete = False 
        try:
            distance = ( (point_one[0] - point_two[0]) ** 2 + (point_one[1] - point_two[1]) ** 2) ** 0.5
            complete = True 
            return distance 
        except Exception as e: 
            self.logger.error(Fore.RED + 'Error calculating distance between points... %s' % str(e) + Style.RESET_ALL)
        finally:
            if complete: 
                self.logger.info('Distance between all points has been calculated...')

    def total_distance(self, points):
        """
        Summary line
        ----------

        Calculate the total distance between points.  

        Parameters
        ----------
        self : instance attribute 
            Allows for reference to instance attributes in the class. 

        points: list of points with longitude and latitude 
            Points to calculate the total distance.  

        Returns
        -------
        total_distance
            Calculated total distance between the points.    
        """  
        complete = False  
        try:      
            total_distance = sum([self.distance(p, points[value + 1]) for value, p in enumerate(points[:-1])])
            complete = True 
            return total_distance
        except Exception as e: 
            self.logger.error(Fore.RED + 'Error calculating total distance between points... %s' % str(e) + Style.RESET_ALL)
        finally:
            if complete: 
                self.logger.info('Total distance between all points has been calculated...')

    def calculate_TSP(self, points):
        """
        Summary line
        ----------
        
        Uses distances to find shortest distance to travel.    

        Parameters
        ----------
        self : instance attribute 
            Allows for reference to instance attributes in the class. 

        Returns
        -------
        tour: path  
            Shortest path found for all cities.  
        """
        complete = False 
        # Starting position 
        start_position = points[0]
        # Places to visit 
        visit_list = points
        # Set tour to starting position 
        tour = [start_position]
        # Remove the starting position 
        visit_list.remove(start_position)
        try: 
            # Loop through places to visit to find min distance 
            while visit_list:
                key_value = lambda y: self.distance(tour[-1], y)
                # Find nearest city 
                nearest_city = min(visit_list, key = key_value)
                # Append nearest city to the tour and remove it from the visit list  
                tour.append(nearest_city)
                visit_list.remove(nearest_city)
            complete = True 

            # Show Plot 
            self.plotIt(tour)

            return tour
        except Exception as e: 
            self.logger.error(Fore.RED + 'Error calculating minimum distance between points and finding total path... %s' % str(e) + Style.RESET_ALL)
        finally:
            if complete: 
                self.logger.info('Minimum distance between all points and path have been calculated...')

    def plotIt(self, tour_points):
        """
        Summary line
        ----------
        
        Plot the found shortest distance to travel.    

        Parameters
        ----------
        self : instance attribute 
            Allows for reference to instance attributes in the class. 

        Returns
        -------
        pyplot 
            Plot of the shortest distance.  
        """
        try:
            # Grab X and Y values of points  
            x = []
            y = [] 
            for values in tour_points:
                x.append(values[0]) 
                y.append(values[1])

            # Append the first item to the end to complete the loop 
            x.append(x[0])
            y.append(y[0])

            # Setup plot 
            plt.plot(x, y, 'b--')
            plt.xlabel('Longitude (X)')
            plt.ylabel('Latitude (Y)')
            plt.title('The TSP Calculated Minimum Route')
            plt.grid(True)

            # Plot TSP route 
            plt.show()

            self.logger.info('Final plot created of route... ')
        except Exception as e: 
            self.logger.error(Fore.RED + 'Error plotting final route. Check data provided... %s' % str(e) + Style.RESET_ALL)
