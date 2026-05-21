# AI Gym & Nutrition Assistant Report

## Final System Description

The project is an AI-assisted fitness and nutrition recommendation system developed in Python.

The system receives user input including:
- age
- weight
- height
- fitness goal

Based on this information, the system calculates BMI, estimates daily calorie needs, and recommends a workout plan.

The purpose of the system is to demonstrate an AI-assisted software solution that uses tools and decision-making logic to solve a practical user problem.

---

# AI and Agent-Based Approach

The system follows a simple intelligent assistant workflow.

The program:
1. receives user input,
2. processes the information,
3. uses internal tools for calculations,
4. generates personalized recommendations.

The assistant simulates an AI-supported recommendation system.

---

# Tools Used in the System

## BMI Calculator Tool
Calculates the Body Mass Index using height and weight.

## Daily Calorie Calculator Tool
Estimates calorie requirements based on user data and goals.

## Workout Recommendation Tool
Selects a suitable workout strategy according to the user goal.

---

# Programming Concepts Used

The project uses several Python programming concepts:

- functions
- conditional statements
- user input handling
- modular logic
- calculations
- testing
- file structure organization

---

# Testing Process

Several tests were performed during development.

## Test Scenario 1
Input:
- weight = 95
- height = 184

Expected Result:
- BMI value greater than 0

Result:
- Passed

## Test Scenario 2
Goal = fat loss

Expected Result:
- calorie reduction
- cardio workout recommendation

Result:
- Passed

## Test Scenario 3
Goal = muscle gain

Expected Result:
- increased calorie recommendation
- Push Pull Legs recommendation

Result:
- Passed

---

# Deployment Preparation

The system can be executed locally using Python and Visual Studio 2022.

Requirements:
- Python
- pytest

The user launches the application and enters the requested information in the terminal window.

---

# Data Conversion and Processing

User input is converted into numerical values and processed by calculation functions.

The system transforms:
- text input
- numeric input
- goal selection

into structured recommendation results.

---

# Deployment Strategy

The project is designed as a local desktop application.

In future development, the system could also be deployed as:
- a web application,
- a cloud API service,
- a mobile assistant backend.

---

# Conclusion

The developed system successfully demonstrates an AI-assisted software solution with tool integration, testing, deployment preparation, and structured project organization.
