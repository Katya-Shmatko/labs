import sqlite3
con = sqlite3.connect('BlockProcessor.db') 
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS event_stream(type TEXT, id TEXT, processed INTEGER DEFAULT 1)")
con.commit()

cur.execute("SELECT id FROM BLOCKS")
existing_ids = {row[0] for row in cur.fetchall()}

def Check_hex(line_id: str):
        if not line_id.startswith('0x'):
            raise ValueError("not hex format")
        if not all(c in '0123456789abcdefABCDEF' for c in line_id[2:]):
            raise ValueError("invalid hex chars")
        

        
        
valid_blocks = []
event_stream_list = []

print(f"--- В базі вже є блоків: {len(existing_ids)} ---")
print("--- Введіть дані блоків (для виходу напишіть 'exit') ---")

while True:
    blocks_id = input('Введіть id блоку який хочете додати:').strip()

    if blocks_id.lower() == 'exit':
        break
    
    if blocks_id in existing_ids:
        print(f"Помилка: ID {blocks_id} вже існує!")
        continue

    try:
        Check_hex(blocks_id)
    except ValueError as e:
        print(f"Помилка формату: {e}")
        continue

    while True:
        try:
            blocks_view = int(input(f'Введіть view (ціле число) для блоку з таким id {blocks_id}:'))
            break
        except ValueError:
            print("Не ціле число, введіть ще раз.")

    blocks_desc = str(blocks_view) + " view"

    check = input(f'Перевірте ваш блок: {blocks_id}, {blocks_view}, "{blocks_desc}", None. Якщо все вірно натисніть ENTER, якщо ні - напишіть будь-що для повтору:')
    if check == "":
        valid_blocks.append((blocks_id, blocks_view, blocks_desc, None))
        event_stream_list.append(('block', blocks_id, 1))
        existing_ids.add(blocks_id)
        print(f" Блок {blocks_id} готовий до запису.")
    else:
        print("Повторне введення даних для цього блоку...")
    


if valid_blocks:
    cur.executemany("INSERT OR IGNORE INTO BLOCKS (id, view, desc, img) VALUES (?, ?, ?, ?)", valid_blocks)
    cur.executemany("INSERT OR IGNORE INTO event_stream (type, id, processed) VALUES (?, ?, ?)", event_stream_list)
    con.commit()
    print(f"\n Успішно додано {len(valid_blocks)} нових записів.")
else:
    print("\nНових блоків не додано.")

con.close()