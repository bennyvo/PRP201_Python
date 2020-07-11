# Example: Counting Domain in a Database
import sqlite3

# fname = 'regex_sum_581872.txt'
fpath = '/Users/vtt/Desktop/PRP201_Python_MOOC/PRP201/Resources/'
# fhandle = open(fpath+fname)

conn = sqlite3.connect('orgcount.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter File name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fhandle = open(fpath+fname)

for line in fhandle:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    # organization_tmp = email.split('@')
    # organization = organization_tmp[1]
    (mailID, organization) = email.split('@')

    cur.execute('SELECT count FROM Counts WHERE org=?',(organization,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count) VALUES (?,1)''', (organization,))
    else:
        cur.execute('''UPDATE Counts SET count = count+1 WHERE org=?''', (organization,))
    conn.commit()
print('Done List:')

sql_str = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sql_str):
    print(str(row[0]), row[1])
    
cur.close()
print('Done DB')
