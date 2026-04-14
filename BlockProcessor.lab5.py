import time
import sqlite3

def run_processor():
    con = sqlite3.connect('BlockProcessor.db') 
    cur = con.cursor()

    print('BlockProsessor started...')

    try:
         while True:
            cur.execute('SELECT type, id FROM event_stream WHERE processed = 1')
            row = cur.fetchone()

            if row:
                  e_type, e_id = row
                  print(f'New block: type "{e_type}", id {e_id}')

                  if e_type == 'block':
                    cur.execute('SELECT view, desc FROM BLOCKS WHERE id = ?', (e_id,))
                    block_data = cur.fetchone()
                    if block_data:
                        print(f'Дані блоку: view - {block_data[0]}, desc - {block_data[1]}')

                  cur.execute('UPDATE event_stream SET processed = 0 WHERE id = ?', (e_id,))
                  con.commit()
                  print('Already done!!!')
            else:
                  time.sleep(1)
    except KeyboardInterrupt:
        print("\n Процесор зупинено вручну.")
    finally:
        con.close()

if __name__ == "__main__":
    run_processor()
            
                