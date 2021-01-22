# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-19 15:51:21
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-22 22:04:14

import mysql.connector
from dotenv import load_dotenv
import datetime
import os
from DBConfig import DBConfig

class SqlQueries:

  def __init__(self):
    try:
      dbConfig = DBConfig()
      self.mydb = dbConfig.getDBConfig()
    except Exception:
      print("Error Connecting to DB")
    
  def printAllEmployees(self):
    """
    function to print all the employees
    """
    try:
      mycursor = self.mydb.cursor()
      mycursor.execute("SELECT * FROM Employees")
      myresult = mycursor.fetchall()
      for x in myresult:
        print(x)
      return True
    except Exception:
      print("Error Fetching all the employees")

  def findEmployee(self,employeeId):
    """
    function to search for specific employee using employee_id
    """
    try:  
      mycursor = self.mydb.cursor()
      mycursor.execute("SELECT * FROM Employees WHERE Emp_id = "+str(empId))
      myresult = mycursor.fetchone()
      print(myresult)
      
    except Exception:
      print("Unable to fetch employee")
    return True
  def addNewSalaryGrade(self):
    """
    function to insert a new salary tuple
    """
    try:
      grade = int(input("Enter Grade number"))
      minSalary = int(input("Enter minimum salary"))
      maxSalary = int(input("Enter max salary"))
      mycursor = self.mydb.cursor()
      sql = "INSERT INTO Salary_Grade VALUES (%s,%s,%s)"
      val = (grade,minSalary,maxSalary)
      mycursor.execute(sql, val)
      self.mydb.commit()
      print(mycursor.rowcount, "record inserted.")
    except Exception:
      print("Error adding salary grade ")

  def insertNewEmployeeinDB(self,empId,empName,jobName,managerId,hireDate,salary,commission,deptId):
      sql = "INSERT INTO Employees VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
      val = (empId,empName,jobName,managerId,hireDate,salary,commission,deptId)
      mycursor = self.mydb.cursor()
      mycursor.execute(sql, val)
      self.mydb.commit()
      print(mycursor.rowcount, "record inserted.")
      return True
  def insertNewEmployee(self):
    """
    function to insert new employee tuple
    """
    try:
      self.takeUserInput()
      self.insertNewEmployeeinDB(self.empId,self.empName,self.jobName,self.managerId,self.hireDate,self.salary,self.commission,self.deptId)
    except Exception as e:
      print("Error inserting New Employee,", e)

  def takeUserInput(self):
    """
    function to take user input for inserting a tuple.
    """
    self.empId = int(input("Input Employee ID: "))
    self.empName = input("Enter Employee Name: ")
    self.jobName = input("Enter job name: ")
    self.managerId = int(input("Enter Manager Id: "))
    self.hireDate = input("Enter Hire Date(YYYY-MM-DD): ")
    self.salary = float(input("Enter salary(900.92): "))
    self.commission = float(input("Enter commision(10.98): "))
    self.deptId = int(input("Enter Dept Id: "))

  def createView(self, MngrId):
    """
    function to create a view and print it
    """
    try: 
      mycursor = self.mydb.cursor()
      mycursor.execute("CREATE OR REPLACE VIEW Employee_With_Same_Manager AS SELECT Emp_name, Manager_id FROM Employees WHERE Manager_id = "+str(MngrId))
      self.mydb.commit()
      mycursor.execute("SELECT * FROM Employee_With_Same_Manager")
      result = mycursor.fetchall()
      for x in result:
        print(x)
      print("View is created.")
    except Exception as e:
      print("Error",  e)
  
  def createProcedure(self):
    """
    function to create procedure
    """
    try:
      mycursor = self.mydb.cursor()
      mycursor.execute("DROP PROCEDURE IF EXISTS EmpDep;")
      mycursor.execute("CREATE PROCEDURE EmpDep() BEGIN select * from Employees JOIN Department where Department.Dept_id=Employees.Dept_id; END")
      self.mydb.commit()
    except Exception as e:
      print("Error",  e)
    
  def callProcedure(self):
    """
    function to call procedure
    """
    try: 
      mycursor = self.mydb.cursor()
      mycursor.execute("CALL EmpDep")
      result = mycursor.fetchall()
      for x in result:
        print(x)
      return True
    except Exception as e:
      print("Error",  e)
    
  def getAllLogs(self):
    """
    function to get all logs
    """
    try:
      mycursor = self.mydb.cursor()
      mycursor.execute("SELECT * FROM Log_Table")
      myresult = mycursor.fetchall()
      for x in myresult:
        print(x)
      return True
    except Exception:
      print("Error getting logs")
      
if __name__ == "__main__":
    sqlQueries = SqlQueries()
    while True:
      choice = int(input("Enter your choice \n 1. Print all employees. \n 2. Find a specific employee \n 3. Add a new Salary grade \n 4. Add a new employee\n 5. Create a View\n 6. Create Procedure \n 7. Call Procedure\n 8. Get Logs\n"))
      if choice == 1:
        sqlQueries.printAllEmployees()
      elif choice == 2:
        empId = int(input("Enter employee Id: \n"))
        sqlQueries.findEmployee(empId)
      elif choice == 3:
        sqlQueries.addNewSalaryGrade()
      elif choice == 4 :
        sqlQueries.insertNewEmployee()
      elif choice == 5 :
        MngrId = int(input("Enter manager Id: \n"))
        sqlQueries.createView(MngrId)
      elif choice == 6 :
        sqlQueries.createProcedure()
      elif choice == 7 :
        sqlQueries.callProcedure()
      elif choice == 8 :
        sqlQueries.getAllLogs()
      else:
        print("Error choice")
        break
    