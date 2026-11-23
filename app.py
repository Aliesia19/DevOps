
import os

import psycopg2
from flask import Flask, request, redirect, url_for

app = Flask(__name__)


def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        database=os.getenv("DB_NAME", "devops_notes"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", "postgres"),
        port=os.getenv("DB_PORT", "5432")
    )


@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>DevOps Notes</title>
        </head>
        <body>
            <h1>Hello, DevOps!</h1>
            <p>Welcome to DevOps Notes application.</p>
            <a href="/notes">View notes</a>
        </body>
    </html>
    """


@app.route("/notes", methods=["GET", "POST"])
def notes():
    connection = get_db_connection()

    try:
        with connection:
            with connection.cursor() as cursor:

                if request.method == "POST":
                    content = request.form.get("content", "").strip()

                    if content:
                        cursor.execute(
                            "INSERT INTO notes (content) VALUES (%s)",
                            (content,)
                        )

                    return redirect(url_for("notes"))

                cursor.execute(
                    "SELECT id, content, created_at FROM notes ORDER BY id DESC"
                )

                notes_list = cursor.fetchall()

        html = """
        <html>
            <head>
                <title>DevOps Notes</title>
            </head>
            <body>
                <h1>My Notes</h1>

                <form method="POST">
                    <input
                        type="text"
                        name="content"
                        placeholder="Enter a note"
                        required
                    >
                    <button type="submit">Add note</button>
                </form>

                <h2>Saved notes</h2>
                <ul>
        """

        for note in notes_list:
            html += f"<li>{note[0]}: {note[1]}</li>"

        html += """
                </ul>
                <a href="/">Home</a>
            </body>
        </html>
        """

        return html

    finally:
        connection.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)

