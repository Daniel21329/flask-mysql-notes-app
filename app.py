from flask import Flask, request, redirect, render_template_string
import pymysql

app = Flask(__name__)

def get_db_connection():
    return pymysql.connect(
        host="db",
        user="root",
        password="password",
        database="notesdb",
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route("/", methods=["GET", "POST"])
def index():
    conn = get_db_connection()
    cur = conn.cursor()

    # Създаваме таблицата, ако няма такава
    cur.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            content TEXT NOT NULL
        )
    """)
    conn.commit()

    if request.method == "POST":
        note = request.form.get("note")
        if note:
            cur.execute("INSERT INTO notes (content) VALUES (%s)", (note,))
            conn.commit()

    cur.execute("SELECT content FROM notes ORDER BY id DESC")
    notes = cur.fetchall()

    cur.close()
    conn.close()

    return render_template_string("""
    <h1>Записки</h1>
    <form method="post">
      <input type="text" name="note" placeholder="Добави записка" required>
      <button type="submit">Добави</button>
    </form>
    <ul>
    {% for note in notes %}
      <li>{{ note.content }}</li>
    {% endfor %}
    </ul>
    """, notes=notes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
