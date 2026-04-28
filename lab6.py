from pydantic import BaseModel, Field
import sqlite3
from datetime import datetime


class Person(BaseModel):
    id: str = Field(min_length=1)  
    name: str = Field(min_length=1) 
    addr: str = Field(min_length=3)
    
    @classmethod
    def get_from_db(cls, cursor):
        cursor.execute('SELECT * FROM PERSONS')
        rows = cursor.fetchall()

        person_list = []

        for row in rows:
            person = cls(id = str(row[0]), name = str(row[1]), addr = str(row[2]))
            person_list.append(person)
        return person_list


class Sources(BaseModel):
    id: str
    ip_addr: str = Field(min_length=7)
    country_code: str = Field(min_length=2, max_length=2)

    @classmethod
    def get_from_db(cls, cursor):
        cursor.execute('SELECT * FROM SOURCES')
        rows = cursor.fetchall()

        sources_list = []

        for row in rows:
                source = cls(id = row[0], ip_addr = row[1], country_code = row[2])
                sources_list.append(source)

        return sources_list

class Vote(BaseModel):
    blockId: str = Field(pattern=r"^[0-9a-fA-F]{8}$")
    timestamp: datetime
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
   

class Block(BaseModel):
    id: str = Field(pattern=r"^[0-9a-fA-F]{8}$")
    view: int = Field(ge=0)
    desc: str = Field(min_length=1)
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

if __name__ == "__main__":
    conn = sqlite3.connect('BlockProcessor.db') 
    cursor = conn.cursor()

    my_persons = Person.get_from_db(cursor)
    my_sources = Sources.get_from_db(cursor)
    my_votes = Vote.get_from_db(cursor)
    my_blocks = Block.get_from_db(cursor)
    
    print("Дані успішно завантажено!")

    conn.close()
