# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-22 20:57:27
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-23 00:13:26
import unittest
from MysqlConnector import SqlQueries

class MySQLConnectorTest(unittest.TestCase):

    def setUp(self):
        self.sqlQueries = SqlQueries()
    def test_getAllLogs(self):
        self.assertEqual(True,self.sqlQueries.getAllLogs())
    def test_printAllEmployees(self):
        self.assertEqual(self.sqlQueries.printAllEmployees(),True)
    def test_insertNewEmployee(self):
        self.assertEqual(self.sqlQueries.insertNewEmployeeinDB(90, 'A', 'B', 2, "1990-12-18", 900.00, 10.00, 1002),True)
    def test_callProcedure(self):
        self.assertEqual(self.sqlQueries.callProcedure(),True)
    def test_findEmployee(self):
        self.assertEqual(self.sqlQueries.findEmployee(2),True)
if __name__ == '__main__':
    unittest.main()