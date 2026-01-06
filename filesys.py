import sqlite3 #nativo
import json #nativo
import csv #nativo

con = sqlite3.connect('database.db')
cur = con.cursor()




cur.close()
con.close()