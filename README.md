CPU Scheduling & Banker's Algorithm Lab Exam
Author: Al-abass

OVERVIEW
========
This project implements two important OS concepts:
1. CPU Scheduling Algorithms (FCFS and Round Robin)
2. Banker's Algorithm (Deadlock Avoidance)

FILES
=====
- scheduling.py: CPU scheduling simulation with First Come First Serve (FCFS) and Round Robin algorithms
- banker.py: Banker's algorithm implementation for deadlock avoidance
- scheduling_input.txt: Sample input for scheduling algorithms
- scheduling_output.txt: Output results from scheduling simulation
- banker_output.txt: Output results from banker's algorithm

HOW TO RUN
==========

SETUP:
   1. Navigate to the project directory:
      cd path\to\Ibrahim_LabExam2
   
   2. Ensure all files are in the same directory

1. CPU Scheduling Program:
   Command: python scheduling.py
   
   Input Required:
   - Number of processes
   - Arrival time for each process
   - Burst time for each process
   - Time quantum for Round Robin
   
   This will simulate:
   - FCFS (First-Come-First-Served) scheduling
   - Round Robin scheduling with user-specified quantum
   
   Output includes:
   - Gantt Chart (execution timeline)
   - Average Waiting Time
   - Average Turnaround Time

2. Banker's Algorithm Program:
   Command: python banker.py
   
   This will check system safety by:
   - Calculating the Need matrix
   - Finding a safe sequence of process execution
   - Determining if deadlock is possible
   
   Output includes:
   - Need Matrix for each process
   - Safety status (Safe State or NOT Safe)
   - Safe sequence (if exists)

REQUIREMENTS
============
- Python 3.x

SAMPLE INPUT/OUTPUT
===================
See scheduling_input.txt, scheduling_output.txt, and banker_output.txt for examples.
