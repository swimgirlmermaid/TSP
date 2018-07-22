#!/usr/bin/python

# Rosemarie Day 
# 22 July 2018 
from timeit import Timer
from graph_tsp import graph_tsp

def runCode():
    var = str(input("Enter filename (with no extension): "))
    T = graph_tsp(var)

t1 = Timer("""runCode()""", """from __main__ import runCode""")
print("Time to Run Application (seconds): " '{0:.1f}'.format(t1.timeit(1)))  