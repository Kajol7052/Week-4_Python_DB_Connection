# -*- coding: utf-8 -*-
# @Author: Kajol.Patira
# @Date:   2021-01-20 22:53:33
# @Last Modified by:   Kajol.Patira
# @Last Modified time: 2021-01-21 10:20:58

import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

class DBConfig:
    def __init__(self):
        self.host=os.getenv("host")
        self.user=os.getenv("user")
        self.password=os.getenv("password")
        self.database=os.getenv("database")

    def getDBConfig(self):
        self.mydb = mysql.connector.connect(
        host=self.host,
        user=self.user,
        password=self.password,
        database=self.database
        )
        return self.mydb
