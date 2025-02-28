import sqlite3
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox


class MyWidget(QMainWindow, QComboBox):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.sorts_of_coffee()
        self.print_data()
        self.coffee_sorts_comboBox.currentIndexChanged.connect(self.print_data)

    def sorts_of_coffee(self):
        con = sqlite3.connect("coffee.db")
        cur = con.cursor()
        result = cur.execute("""SELECT sort_name FROM coffee""").fetchall()
        con.close()
        for i in result:
            self.coffee_sorts_comboBox.addItem(i[0])

    def print_data(self):
        sort = self.coffee_sorts_comboBox.currentText()
        con = sqlite3.connect("coffee.db")
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM coffee WHERE sort_name = ?""", (sort,)).fetchall()[0]
        con.close()
        self.ID_put.setText(str(result[0]))
        self.name_put.setText(result[1])
        self.roast_greed_put.setText(result[2])
        self.consistation_put.setText(result[3])
        self.describtion_put.setText(result[4])
        self.price_put.setText(result[5])
        self.volume_put.setText(result[6])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
