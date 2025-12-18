import psycopg2

conn = psycopg2.connect(
    dbname = "shopdata",
    user = "admin",
    password = "admin",
    host = "localhost",
    port = 5433
)

cur = conn.cursor()

cur.execute("SELECT u.login, u.password, r.rolename AS Role FROM users u JOIN roles r ON u.roleid = r.id;")

print(cur.fetchone())

cur.close()
conn.close()