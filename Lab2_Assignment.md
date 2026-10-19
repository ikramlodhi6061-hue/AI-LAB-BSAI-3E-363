# **Artificial Intelligence – Lab Task 2**

## **Assignment Overview**
This repository contains the Python implementation and supporting report for Artificial Intelligence Lab Task 2. It brings together the PEAS specifications, environment classification, and a stateful mode control agent in one assignment.

## **Task 1: PEAS Specifications**
PEAS specifications are provided for a Delivery Robot and an LLM-Based Student Support Agent. Each specification explains the agent’s **Performance Measure, Environment, Actuators, and Sensors**, helping describe what the agent should achieve and how it interacts with its surroundings.

## **Task 2: Environment Classification**
This task discusses partially observable and stochastic environments, including the difference between observable and hidden variables. It also explains how actions may be predictable while outcomes remain uncertain, and how a simplified simulator can differ from a real-world environment.

## **Task 3: Stateful Mode Control Agent**
The Python program demonstrates an agent that chooses a mode based on room temperature and occupancy. It remembers the previous mode, avoids sending duplicate commands when the target mode has not changed, checks exact temperature boundaries, handles an empty room, and records mode transitions.

## **Repository Files**
The repository includes `lab2_assignment.py` for the combined implementation of Tasks 1, 2, and 3, `Lab2_Report.docx` for the written report, `README.md` for the project overview and run instructions, and `test_output.txt` for captured program output if included.

## **Requirements**
Python **3.8 or newer** is required to run the program. No external Python packages are needed, so the assignment can be executed using a standard Python installation.

## **How to Run**
Download or clone the repository, open a terminal in the project folder, and run the command below. On some systems, use `python3` instead of `python`.

```bash
python lab2_assignment.py
```

Alternative command:

```bash
python3 lab2_assignment.py
```

## **Test Scenarios**
The program tests repeated percepts to ensure identical target modes do not generate duplicate commands. It also checks the exact lower and upper temperature boundaries and confirms that the target mode changes to **OFF** when the room is unoccupied.

## **Assumptions**
The controller assumes that temperature is measured in degrees Celsius. If the room is empty, the mode is **OFF**; if occupied and the temperature is **18°C or lower**, it is **HEAT**; if the temperature is **28°C or higher**, it is **COOL**; and if the temperature is strictly between **18°C and 28°C**, it is **IDLE**. A command is sent only when the target mode differs from the previously remembered mode.

## **Important Note**
If the instructor’s previous lab specifies different temperature thresholds or control rules, update the implementation to match those instructions before submission. This helps ensure that the program follows the required assignment specifications.

## **Author**
**Student:** **Zill Hasnain**  
**Course:** Artificial Intelligence
