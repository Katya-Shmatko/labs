import pytest
from pydantic import ValidationError
from datetime import datetime
from lab6 import Person, Sources, Vote, Block

#class Block(BaseModel):
#    id: str = Field(pattern=r"^[0-9a-fA-F]{8}$")
#    view: int = Field(ge=0)
#    desc: str = Field(min_length=1)
#    img: bytes

def test_block():
    block = Block(id = 'ADC143B2', view = 20, desc = '20 views', img = b"test")
    assert block.id == 'ADC143B2'
    assert block.view == 20
    assert block.desc == '20 views'

def test_block_id_len():
    with pytest.raises(ValidationError):
        Block(id = 'ADC143B', view = 100, desc = '20 views', img = b"test")

def test_block_id_symbols():
    with pytest.raises(ValidationError):
        Block(id = 'ADC143z2', view = 100, desc = '20 views', img = b"test")

def test_block_view():
    with pytest.raises(ValidationError):
        Block(id = 'ADC143B2', view = -1, desc = '20 views', img = b"test")

def test_block_desc():
    with pytest.raises(ValidationError):
        Block(id = 'ADC143B2', view = 20, desc = '20 views', img = b"test")


#class Vote(BaseModel):
#    blockId: str = Field(pattern=r"^[0-9a-fA-F]{8}$")
#    timestamp: datetime
#    source_id: str

def test_vote():
    vote = Vote(blockId = 'ADC143B2', timestamp = '2026-04-14 12:00', source_id = '1')
    assert vote.blockId == 'ADC143B2'
    assert vote.timestamp == datetime(2026, 4, 14, 12, 0)
    assert vote.source_id == '1'

def test_vote_blockId_len():
    with pytest.raises(ValidationError):
        Vote(blockId = 'ADC1432', timestamp = '2026-04-14 12:00', source_id = '1')

def test_vote_blockid_symbols():
    with pytest.raises(ValidationError):
        Vote(blockId = 'ADz143B2', timestamp = '2026-04-14 12:00', source_id = '1')

def test_vote_timestamp():
    with pytest.raises(ValidationError):
        Vote(blockId = 'ADC143B2', timestamp = '2026-04-14 42:00', source_id = '1')


#class Sources(BaseModel):
#    id: str
#    ip_addr: str = Field(min_length=7)
#    country_code: str = Field(min_length=2, max_length=2)

def test_sources():
    source = Sources(id = 'ADC143B2', ip_addr = '192.168.1.1', country_code = 'UA')
    assert source.id == 'ADC143B2'
    assert source.ip_addr == '192.168.1.1'
    assert source.country_code == 'UA'

def test_sources_ip():
    with pytest.raises(ValidationError):
        Sources(id = 'ADC143B2', ip_addr = '8.1.1', country_code = 'UA')

def test_sources_country_code():
    with pytest.raises(ValidationError):
        Sources(id = 'ADC143B2', ip_addr = '192.168.1.1', country_code = 'U')

def test_sources_country_code_too_long():
    with pytest.raises(ValidationError):
        Sources(id = 'ADC143B2', ip_addr = '192.168.1.1', country_code = 'UKR')


#class Person(BaseModel):
#    id: str = Field(min_length=1)  
#    name: str = Field(min_length=1) 
#    addr: str = Field(min_length=3)

def test_person():
    person = Person(id = 'ADC143B2', name = 'Mike', addr ='456 Oak Avenue, New York, NY 10001')
    assert person.id == 'ADC143B2'
    assert person.name == 'Mike'
    assert person.addr == '456 Oak Avenue, New York, NY 10001'

def test_person_id():
    with pytest.raises(ValidationError):
        Person(id = '', name = 'Mike', addr ='456 Oak Avenue, New York, NY 10001')

def test_person_name():
    with pytest.raises(ValidationError):
        Person(id = 'ADC143B2', name = '', addr ='456 Oak Avenue, New York, NY 10001')

def test_person_addr():
    with pytest.raises(ValidationError):
        Person(id = 'ADC143B2', name = 'Mike', addr ='45')














    



    