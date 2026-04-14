from dataclasses import dataclass
import sqlite3

conn = sqlite3.connect('BlockProcessor.db') 
cursor = conn.cursor()

@dataclass
class Person:
    id: str
    name: str
    addr: str

    @classmethod
    def get_from_db(cls, cursor):
        cursor.execute('SELECT * FROM PERSONS')
        rows = cursor.fetchall()

        person_list = []

        for row in rows:
            person = cls(id = row[0], name = row[1], addr = row[2])
            person_list.append(person)
        # [cls(id = row[0], name = row[1], addr = row[2]) for row in rows]
        return person_list


@dataclass
class Sources:
    id: str
    ip_addr: str
    country_code: str

    @classmethod
    def get_from_db(cls, cursor):
        cursor.execute('SELECT * FROM SOURCES')
        rows = cursor.fetchall()

        sources_list = []

        for row in rows:
                source = cls(id = row[0], ip_addr = row[1], country_code = row[2])
                sources_list.append(source)

        return sources_list

@dataclass
class Vote:
    blockId: str
    timestamp: str
    source_id: str

    @classmethod
    def get_from_db(cls, cursor):
        cursor.execute('SELECT * FROM VOTES')
        rows = cursor.fetchall()

        vote_list = []

        for row in rows:
                vote = cls(blockId = row[0], timestamp = row[1], source_id = row[2])
                vote_list.append(vote)

        return vote_list
   

@dataclass
class Block:
    id: str
    view: int
    desc: str
    img: bytes

    @classmethod
    def get_from_db(cls, cursor):
        cursor.execute('SELECT * FROM BLOCKS')
        rows = cursor.fetchall()

        block_list = []

        for row in rows:
                block = cls(id = row[0], view = row[1], desc = row[2], img = row[3])
                block_list.append(block)

        return block_list

my_persons = Person.get_from_db(cursor)
my_sources = Sources.get_from_db(cursor)
my_votes = Vote.get_from_db(cursor)
my_blocks = Block.get_from_db(cursor)

conn.close()