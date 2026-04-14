from dataclasses import dataclass
import sqlite3
con = sqlite3.connect('BlockProcessor.db') 
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS event_stream(type TEXT, id TEXT, processed DEFAULT 0)")
con.commit()