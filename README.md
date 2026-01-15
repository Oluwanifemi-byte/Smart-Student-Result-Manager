Name: Jigan Oluwanifemi Semilore

Matric number: 24/13623

URL: https://github.com/Oluwanifemi-byte/Smart-Student-Result-Manager


Software Development Life Cycle (SDLC)
Project: Smart Student Result Manager
1. Planning Phase
Objective

To build a command-line Python application called Smart Student Result Manager that helps manage student results.

Problems Identified

Manual result calculation is slow and error-prone

Student records are not well organized

Searching and editing results is difficult

Goals

Store student data digitally

Automatically calculate total, average, grade, and remark

Allow admin to add, view, search, edit, and delete records

Save data using a file named: students.json

2. Requirement Analysis
Functional Requirements

The system must be able to:

Add student records using add_student()

View all records using view_all()

Search student using search()

Edit student scores using edit()

Delete student record using delete()

Calculate grade using get_grade()

Load data using load_data()

Save data using save_data()

Non-Functional Requirements

Easy to use (menu-driven)

Fast for small to medium data

Data should persist using students.json

Runs on any system with Python installed

3. System Design
Architecture

Single-file Python program: result_manager.py

Data file: students.json

Menu-driven Command Line Interface

Data Structure

Each student record is stored as a dictionary:

student = {
    "name": name,
    "matric": matric,
    "course": course,
    "scores": scores,
    "total": total,
    "average": avg,
    "grade": grade,
    "remark": remark
}


All students are stored inside a list:

data = [student1, student2, student3, ...]

4. Implementation
Main Functions Used
Function Name	Purpose
load_data()	Reads student data from students.json
save_data(data)	Saves student data into students.json
get_grade(avg)	Returns grade and remark
add_student(data)	Adds new student record
view_all(data)	Displays all records
search(data)	Finds a student by name or matric
edit(data)	Updates student scores
delete(data)	Removes a student
main()	Controls the menu and flow
Flow

Program starts at main()

Loads existing data using load_data()

Displays menu

User selects option

Corresponding function runs

Changes saved using save_data()

5. Testing
Test Cases
Feature	Test	Expected Result
Add Student	Input valid data	Student saved
View All	No data	"No records found"
Search	Existing matric	Student displayed
Search	Wrong matric	"Student not found"
Edit	Valid matric	Record updated
Delete	Valid matric	Record removed
Grade	Avg = 75	Grade A, Remark Excellent
File Load	No file	Empty list returned

Testing was done manually by running result_manager.py and checking outputs.

6. Deployment
Steps

Save file as result_manager.py

Install Python

Run:

python result_manager.py


System automatically creates students.json when saving first record.

7. Maintenance
Possible Future Updates

Add login system

Add GUI using Tkinter

Export to Excel

Add subject-wise results

Improve search filters

Bug Fixing

Fix wrong inputs

Improve validation

Prevent duplicate matric numbers

Summary

The Smart Student Result Manager followed all SDLC stages:

Planning – Identified problem and goals

Requirement Analysis – Defined system features

Design – Planned structure and data format

Implementation – Coded using Python functions

Testing – Verified each feature

Deployment – Ran as CLI application

Maintenance – Planned upgrades and fixes
