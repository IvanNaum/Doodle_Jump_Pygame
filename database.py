import os
import sqlite3
from pathlib import Path

dir_path = Path(__file__).parent.absolute()

PATH_DB = str(dir_path / 'data/score.db')
PATH_SQL = str(dir_path / 'data/score.sql')


class DataBase(object):
    def __init__(self):

        if not os.path.exists(PATH_DB):
            with open(PATH_SQL, 'rt') as sql_file:
                self.connect = sqlite3.connect(PATH_DB)
                self.cursor = self.connect.cursor()
                for command in sql_file.readlines():
                    self.cursor.execute(command)
                self.connect.commit()
        else:
            self.connect = sqlite3.connect(PATH_DB)
            self.cursor = self.connect.cursor()

    def add_score(self, score):
        marks = list(filter(lambda x: score - 10 < x < score + 10, self.get_all_scores()))
        print(marks)
        if not marks and score != 0:
            print('ok')
            self.cursor.execute('INSERT INTO score (score) VALUES (?)', (score,))
            self.connect.commit()

    def get_max_score(self):
        return self.cursor.execute('SELECT max(score) FROM score').fetchone()[0]

    def get_all_scores(self):
        return tuple(map(lambda x: x[0], self.cursor.execute('SELECT score FROM score').fetchall()))


data_base = DataBase()
