import csv
from dataclasses import dataclass

@dataclass
class Vote:
    blockId: str

    def __hash__(self):
        return hash(self.blockId) 

    def __eq__(self, other):
        if not isinstance(other, Vote):
            return False
        return self.blockId == other.blockId

@dataclass
class Block:
    id: str
    view: int

class Check_hex:
    def __init__(self, line_id: str):
        if not line_id.startswith('0x'):
            raise ValueError("not hex format")
        if not all(c in '0123456789abcdefABCDEF' for c in line_id[2:]):
            raise ValueError("invalid hex chars")
        self.hexStr = line_id

blocks_list = []
votes_unique = set() 
added_blocks = set()

with open('lab2.csv', 'r', encoding='utf-8') as file:
    table_data = csv.reader(file)
    
    for line in table_data:
        if not line: continue
        line_type = line[0].strip().lower()
        
        try:
            if line_type == 'block':
                line_id = line[1].strip()
                hex_id = Check_hex(line_id).hexStr
                
                if hex_id not in added_blocks:
                    view_val = int(line[3].strip())
                    blocks_list.append(Block(id=hex_id, view=view_val))
                    added_blocks.add(hex_id)  
                
            elif line_type == 'vote':
                line_id = line[2].strip() 
                votes_unique.add(Vote(blockId=Check_hex(line_id).hexStr))
                
        except (ValueError, IndexError) as e:
            print(f"⚠️ Рядок пропущено: {line} (Помилка: {e})")

sorted_blocks = sorted(blocks_list, key=lambda b: b.view)

print(f"\nГолосів (унікальних ID): {len(votes_unique)}")
print("-" * 35)

for b in sorted_blocks:
    count = sum(1 for v in votes_unique if v.blockId == b.id)
    print(f"Block {b.id} (view: {b.view}) -> votes: {count}")
