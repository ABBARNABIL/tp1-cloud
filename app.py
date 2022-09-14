from flask import Flask
import os
import psycopg2

app = Flask(__name__)


DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')


@app.route('/')
def visit():  # put application's code here
    cur = conn.cursor()
    cur.execute("SELECT count FROM visits")
    count = cur.fetchone()
    if count is None:
        count = 0
    else:
        count = count[0]
    cur.execute("UPDATE visits SET count = %s", (count + 1,))
    conn.commit()
    return 'Hello World! I have been seen {} times.'.format(count)


if __name__ == '__main__':
    app.run()
