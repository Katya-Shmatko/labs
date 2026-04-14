from datetime import datetime
import sqlite3
con = sqlite3.connect("BlockProcessor.db")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS BLOCKS(id TEXT PRIMARY KEY, ""view"" INTEGER, ""desc"" TEXT, img BLOB)")
cur.execute("CREATE TABLE IF NOT EXISTS SOURCES(id TEXT PRIMARY KEY, ip_addr TEXT, country_code TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS VOTES (block_id TEXT, voter_id INTEGER, timestamp DATETIME, source_id INTEGER)")
cur.execute("CREATE TABLE IF NOT EXISTS PERSON (id INTEGER PRIMARY KEY, name TEXT, addr TEXT)")

con.commit()

persons = [(1, 'Jane', '15 Maple Avenue, New York'), 
           (2, 'Sandy', '42 Highland Road, Edinburgh'), 
           (3, 'Bob', '88 Sunset Boulevard, Los Angeles'), 
           (4, 'Bill', '12 Victoria Street, Manchester')
           ]
cur.executemany("INSERT OR IGNORE INTO PERSONS (id, name, addr) VALUES (?, ?, ?)", persons)
con.commit()

sources = [
    ('SRV-01', '192.168.1.1', 'US'),
    ('SRV-02', '185.25.12.3', 'UK'),
    ('SRV-03', '91.192.10.5', 'UA')
]
cur.executemany("INSERT OR IGNORE INTO SOURCES (id, ip_addr, country_code) VALUES (?, ?, ?)", sources)
con.commit()

blocks = [
    ('0xABC123', 10, '10 views', None),
    ('0xDEF456', 5, '5 views', None),
    ('0xGHI789', 100, '100 views', None)
]
cur.executemany("INSERT OR IGNORE INTO BLOCKS (id, view, desc, img) VALUES (?, ?, ?, ?)", blocks)
con.commit()

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

votes = [
    ('0xABC123', 1, now, 'SRV-01'), 
    ('0xABC123', 2, now, 'SRV-01'), 
    ('0xDEF456', 3, now, 'SRV-03')  
]
cur.executemany("INSERT OR IGNORE INTO VOTES (block_id, voter_id, timestamp, source_id) VALUES (?, ?, ?, ?)", votes)

con.commit()
con.close()