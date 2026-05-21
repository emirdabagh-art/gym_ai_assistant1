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

---

# Journal by Submission Stage

## Step 1 – 24.04

At the first stage, the planned system was defined as an AI-assisted gym and nutrition assistant. The main goal was to create a Python-based software system that receives user information and returns useful fitness-related recommendations.

The planned AI-assisted approach was based on a single intelligent assistant workflow. The system would take user input, process it, use internal tools, and generate a meaningful result.

Planned tools:
- BMI calculator
- daily calorie calculator
- workout recommendation tool

Preliminary programming concepts:
- functions
- conditional statements
- user input handling
- calculations
- basic testing
- project documentation

---

## Step 2 – 08.05

At the second stage, the system was implemented as a working Python application. The main workflow was created, and the assistant was able to receive user input, process it, and return recommendations.

The programming concepts actually used in the project were:
- Python functions for tool-based calculations
- conditional logic for goal-based decisions
- input and output handling
- numerical calculations
- simple testing structure
- GitHub version control

The tools were integrated directly into the system logic. The BMI calculator processes height and weight, the calorie calculator estimates daily needs, and the workout recommendation tool selects a plan based on the user’s goal.

---

## Step 3 – 15.05

At the third stage, testing and deployment preparation were added.

Testing included:
- BMI calculation test
- fat loss goal test
- muscle gain goal test
- basic workflow validation

The deployment preparation included:
- README file
- requirements.txt file
- startup instructions
- GitHub repository

Data conversion was also considered. User input such as age, weight, height, and goal is collected from the terminal, converted into suitable numerical or text values, and passed into the calculation and recommendation functions.

---

## Final Submission – 22.05

The final version of the project is a working Python-based AI-assisted gym and nutrition assistant.

The system receives user input, processes the data, uses calculation and recommendation tools, and returns a meaningful personalized result.

Final tools:
- BMI calculator tool
- daily calorie calculator tool
- workout recommendation tool

Final testing showed that the main functions work correctly for the selected scenarios. The project is prepared for local deployment using Python and Visual Studio 2022.

The chosen deployment strategy is a local desktop Python application. In future development, the system could be expanded into a web application or API-based assistant.
