#!/usr/bin/python3
import pandas as pd
import sys
from pathlib import Path

my_file = Path("/tmp/public_data/.loaded")
if my_file.is_file():
  sys.exit(0)

df = pd.read_csv('/tmp/public_data/student-por.csv')
df.columns = [c.lower() for c in df.columns] #postgres doesn't like capitals or spaces

from sqlalchemy import create_engine
engine = create_engine('postgresql://pd_user:MonkeysAreCool@localhost:5432/public_data')

df.to_sql("student_por", engine)

df1 = pd.read_csv('/tmp/public_data/student-mat.csv')
df1.columns = [c.lower() for c in df1.columns] #postgres doesn't like capitals or spaces

df1.to_sql("student_mat", engine)
f = open("/tmp/public_data/.loaded","w+")
