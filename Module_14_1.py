import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()


# cursor.execute('''
#  CREATE TABLE IF NOT EXISTS Users(
#  id INTEGER PRIMARY KEY,
#  username TEXT NOT NULL,
#  email TEXT NOT NULL,
#  age INTEGER,
#  balance INTEGER NOT NULL
#  )
#  ''')
# cursor.execute("CREATE INDEX idx_email ON Users(email)")
#
# for i in range(1,11):
#     cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)",
#                    (f"user{i}", f"example{i}@gmail.com", f"{i}0", "1000"))

# for i in range(1, 11, 2):
#     cursor.execute("UPDATE Users SET balance = ? WHERE id%2!=0 ", (500,))

# for i in range(1,11,3):
#     cursor.execute("DELETE FROM Users WHERE id=?", (f"{i}",))

cursor.execute('SELECT * FROM Users')
users = cursor.fetchall()
for user in users:
    if user[3] != 60:
        print(f'Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]} | Баланс: {user[4]}')


connection.commit()
connection.close()



