# Databricks notebook source
print("Hello world")

# COMMAND ----------

import os
os.getcwd()

# COMMAND ----------

from shared import draft_utility

var = draft_utility()
print(var)


# COMMAND ----------

from utils.printers import printer_basic

a = printer_basic()
print(a)
