import psycopg2


conn = psycopg2.connect(
    dbname="phonebook",
    user="postgres",
    password="Nba.230507",
    host="localhost",
    port=5432
)
cur = conn.cursor()
print("=== Pattern search ===")
cur.execute("SELECT * FROM search_phonebook(%s);", ("an",))
rows = cur.fetchall()
for r in rows:
    print(r)


print("\n=== Add or Update User ===")
cur.execute("CALL add_or_update_user(%s, %s);", ("Nari", "777123123"))
conn.commit()
print("✔ User added/updated: Nari")

print("\n=== Add Many Users ===")
usernames = ["Eldar", "Zhansaya", "Tom i Jerry"]
phones = ["87012345678", "87072935711", "87072935710"]


cur.execute("CALL add_many_users(%s, %s);", (usernames, phones))
conn.commit()
print("✔ Many users added/updated. Wrong phones are shown as NOTICE in PostgreSQL console.")


print("\n=== Pagination ===")
cur.execute("SELECT * FROM get_phonebook_page(%s, %s);", (5, 0))
rows = cur.fetchall()
for r in rows:
    print(r)


print("\n=== Delete User ===")
cur.execute("CALL delete_user(%s);", ("Tom i Jerry",))
conn.commit()
print("✔ User deleted: Tom i Jerry")


cur.close()
conn.close()
