import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
from datetime import datetime, timedelta
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import requests
import mysql.connector
import pymysql


conn=pymysql.connect(host='localhost',user='root',password='Saurabh@123',database='saurabhdb1')
check=pd.read_sql_query("SELECT * FROM employee",conn)
print(check)