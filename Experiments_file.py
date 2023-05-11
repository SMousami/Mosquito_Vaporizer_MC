"""
IS 597 PR Spring 2023
Project
Title: Monte Carlo simulation of the effectiveness of vaporizers in killing mosquitoes
Submitted by: Mousami Shinde
Date: April 2023
IDE: Pycharm 2022.3.1 Professional Edition
Python version 3.10.11
-------------------------------------------------------------
This project is a Monte Carlo simulation that studies how vaporizers are effective in killing mosquitoes.
File: Experiment Results
Purpose: To demonstrate the results
"""
import functions_file as sim

#To run the class in which all the functions are stored:
s = sim.VaporizerSimulation(size=10, time=180, vaporizer_locations=[0,9], fan_speed=0.3, threshold=100, emission_rate=100)

#The first experiment will be conducted using the function experiment. Feel free to comment out the codes below as per usage.
s.experiment(runs=100)
#s.experiment_2(runs=100)
#s.experiment_3(runs=100)



