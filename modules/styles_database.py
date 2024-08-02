import sqlite3


class DatabaseManager:
    def __init__(self, db_name='styles.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS styles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                font_face TEXT,
                font_size INTEGER,
                font_weight INTEGER,
                font_italic BOOLEAN,
                color TEXT
            )
        ''')
        self.connection.commit()

    def add_style(self, name, font_face, font_size, font_weight, font_italic, color):
        self.cursor.execute('''
            INSERT INTO styles (name, font_face, font_size, font_weight, font_italic, color)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (name, font_face, font_size, font_weight, font_italic, color))
        self.connection.commit()

    def get_styles(self):
        self.cursor.execute('SELECT * FROM styles')
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()

    def remove_style(self, style_id):
        query = "DELETE FROM styles WHERE id = ?"
        self.connection.execute(query, (style_id,))
        self.connection.commit()
