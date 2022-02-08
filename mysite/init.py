import os
import sqlite3

DB = './storages/blog.db'
schema_filename = './storages/blog_schema.sql'

with sqlite3.connect(DB) as conn:
   print('Creating schema')

   with open(schema_filename, 'rt') as f:
       schema = f.read()
   conn.executescript(schema)
   print('Schema Created Successfully')
