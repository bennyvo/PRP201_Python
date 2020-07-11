# Example: Counting Email in a Database
import sqlite3

# fname = 'regex_sum_581872.txt'
fpath = '/Users/vtt/Desktop/PRP201_Python_MOOC/PRP201/Resources/'
# fhandle = open(fpath+fname)

conn = sqlite3.connect('PY4E_C4_W2_EmailCount.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('''CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = input('Enter File name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fhandle = open(fpath+fname)

for line in fhandle:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email=?',(email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count) VALUES (?,1)''', (email,))
    else:
        cur.execute('''UPDATE Counts SET count = count+1 WHERE email=?''', (email,))
    conn.commit()

sql_str = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 20'

for row in cur.execute(sql_str):
    print(str(row[0]), row[1])

cur.close()
