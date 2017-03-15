import sqlite3, time
from task import Task


class Storage():
    conn = 0

    def __init__(self):
        self.conn = sqlite3.connect("tasks.db")
        self.create_if_not_existing()

    def create_if_not_existing(self):
        c = self.conn.cursor()
        c.execute(
            "CREATE TABLE IF NOT EXISTS tasks (name VARCHAR,duration INT,cycle_time INT, long_break  INT,short_break INT, day DATE,alarm VARCHAR, status VARCHAR);")

    def open(self):
        pass

    def get(self):
        c = self.conn.cursor()
        tasks = []
        for row in c.execute('SELECT name,duration,cycle_time,short_break,long_break,day,alarm, status FROM tasks'):
            t = Task(row[0], row[1], row[2], row[3], bool(row[4]) ,row[5],row[6])
            tasks.append(t)
        return tasks

    def save(self, task):
        c = self.conn.cursor()
        today = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        fields = [task.name, task.duration, task.cycle_time, task.long_break, task.short_break, today, alarm ,task.status]

        sql = "INSERT into tasks (`name`,duration,cycle_time,long_break,short_break,`day`,status)" \
              " VALUES(?,?,?,?,?,?,?,?)"
        c.execute(sql, fields)
        self.conn.commit()

    def close(self):
        self.conn.close()