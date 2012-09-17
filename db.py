import sqlite3
DB = os.path.join(os.path.dirname(__file__), 'db')
DB = os.path.join(DB, 'braveirc.db')
DB = os.path.abspath(DB)
if not os.path.isfile(DB):
    open(DB, 'a')

digest = lambda password: hashlib.md5(password).hexdigest()

conn = sqlite3.connect(DB, check_same_thread=False)
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, '
        'username VARCHAR(255), password VARCHAR(255))')

conn.commit()


def addUser(username, password):
    password = digest(password)
    cur.execute('insert into users (username, password) values (?, ?)',
            (username, password))
    conn.commit()


def showUsers():
    for row in cur.execute('select * from users'):
        print row


