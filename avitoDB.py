import sqlite3

def create_table():
    con = sqlite3.connect('db.sqlite')
    cur = con.cursor()
    sql = """CREATE TABLE IF NOT EXISTS Avito(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        keyword TEXT NOT NULL,
        region TEXT,
        title TEXT NOT NULL,
        price INTEGER,
        description TEXT,
        url TEXT NOT NULL UNIQUE
    );"""
    cur.executescript(sql)
    cur.close()
    con.close()

def insert(data):
    create_table()  # Удостоверьтесь, что функциия create_table() корректно определяет структуру вашей таблицы.
    con = sqlite3.connect('db.sqlite')
    cur = con.cursor()

    sql = """
    INSERT INTO Avito (keyword, region, title, price, description, url)
    VALUES (?, ?, ?, ?, ?, ?)
    ON CONFLICT(url) DO UPDATE SET
        keyword = EXCLUDED.keyword,
        region = EXCLUDED.region,
        title = EXCLUDED.title,
        price = EXCLUDED.price,
        description = EXCLUDED.description;
    """

    try:
        cur.execute(sql, data)
        con.commit()
        print('Data inserted')
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    finally:
        cur.close()
        con.close()
        