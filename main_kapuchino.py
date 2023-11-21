import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.con = sqlite3.connect('coffee.sqlite')
        self.cur = self.con.cursor()
        self.add.clicked.connect(self.add_elem)
        self.update.clicked.connect(self.update_elem)

    def add_elem(self):
        self.cur.execute(
            f"""INSERT INTO Data(name, degree, type, taste, price, volume) VALUES (?, ?, ?, ?, ?, ?)""",
            (self.name.text(), self.degree.text(),
             self.ground.text(), self.taste.text(), self.price.text(), self.volume.text())).fetchall()
        self.con.commit()

    def update_elem(self):
        if self.name.text():
            self.cur.execute(f"""UPDATE Data SET name = ? WHERE id = ?""", (self.name.text(),
                                                                            self.id_line.text())).fetchall()
            self.con.commit()
        if self.degree.text():
            self.cur.execute(f"""UPDATE Data SET degree = ? WHERE id = ?""", (self.degree.text(),
                                                                              self.id_line.text())).fetchall()
            self.con.commit()
        if self.ground.text():
            self.cur.execute(f"""UPDATE Data SET type = ? WHERE id = ?""", (self.ground.text(),
                                                                            self.id_line.text())).fetchall()
            self.con.commit()
        if self.taste.text():
            self.cur.execute(f"""UPDATE Data SET taste = ? WHERE id = ?""", (self.taste.text(),
                                                                             self.id_line.text())).fetchall()
            self.con.commit()
        if self.price.text():
            self.cur.execute(f"""UPDATE Data SET price = ? WHERE id = ?""", (self.price.text(),
                                                                             self.id_line.text())).fetchall()
            self.con.commit()
        if self.volume.text():
            self.cur.execute(f"""UPDATE Data SET volume = ? WHERE id = ?""", (self.volume.text(),
                                                                              self.id_line.text())).fetchall()
            self.con.commit()

    def closeEvent(self, event):
        self.con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
