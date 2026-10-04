Artificial Intelligence - Lab Task 2

Assignment Overview
This repository contains the Python implementation and supporting report for Lab Task 2.
Task 1: PEAS Specifications
PEAS specifications are provided for:
Delivery Robot
LLM-Based Student Support Agent
Each specification describes Performance Measure, Environment, Actuators, and Sensors.
Task 2: Environment Classification
The assignment discusses:
Partially observable environments
Stochastic environments
Observable and hidden variables
Predictable actions and uncertain outcomes
Differences between a simplified simulator and a real environment
Task 3: Stateful Mode Control Agent
The Python program demonstrates an agent that:
Selects a mode using room temperature and occupancy.
Remembers its previous mode.
Avoids sending a repeated command when the target mode has not changed.
Checks exact temperature boundaries.
Handles an empty-room situation.
Records mode transitions.
Repository Files
lab2_assignment.py — combined Python implementation of Tasks 1, 2, and 3.
Lab2_Report.docx — written assignment report.
README.md — project overview and run instructions.
test_output.txt — captured program output, if included.
Requirements
Python 3.8 or newer
No external Python packages are required.
How to Run
Download or clone this repository.
Open a terminal in the repository folder.
Run:
python lab2_assignment.py
On some systems, use:
python3 lab2_assignment.py
Test Scenarios
Repeated percepts: checks that identical target modes do not generate duplicate commands.
Exact threshold boundaries: checks the lower and upper temperature limits.
Empty room: checks that the target mode becomes OFF when the room is unoccupied.
Assumptions
The example controller uses these assumed rules:
Temperature is measured in degrees Celsius.
If the room is empty, the target mode is OFF.
If occupied and temperature is 18°C or lower, the target mode is HEAT.
If occupied and temperature is 28°C or higher, the target mode is COOL.
If occupied and temperature is strictly between 18°C and 28°C, the target mode is IDLE.
A command is sent only when the target mode differs from the previously remembered mode.
If the instructor's previous lab specifies different thresholds or control rules, update the implementation to match those instructions before submission.
Author
Student: ____________________ Course: Artificial Intelligence
