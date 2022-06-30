import sqlite3
import sys

from PyQt5 import QtWidgets

import second_window
import window

db = sqlite3.connect("table_db12")
cursor = db.cursor()


# cursor.execute('''DROP TABLE IF EXISTS table1''')
# cursor.execute('''CREATE TABLE table1(
#     key INTEGER PRIMARY KEY AUTOINCREMENT,
#     ddn DATETIME,
#     koef FLOAT,
#     prim VARCHAR(100))''')
# cursor.execute('''DROP TABLE IF EXISTS table2''')
# cursor.execute('''CREATE TABLE table2(
#     key INTEGER PRIMARY KEY AUTOINCREMENT,
#     name VARCHAR(100),
#     pol BOOL,
#     FOREIGN KEY (key) REFERENCES table1(key))''')
# db.commit()


class Uploading_W1(QtWidgets.QMainWindow, window.Ui_MainWindow):
    cursor.execute("SELECT ddn, koef, prim FROM table1")
    db_data = cursor.fetchall()

    def __init__(self):
        super(Uploading_W1, self).__init__()
        self.setupUi(self)
        self.button()
        self.init_handler()
        self.window_2 = None
        self.is_button_upload_was_used = False

    def loaded(self):
        try:
            self.is_button_upload_was_used = True
            i = 0
            self.tableWidget.setRowCount(len(self.db_data))
            for rows in self.db_data:
                self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(rows[0])))
                self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(rows[1])))
                self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(rows[2])))
                i += 1
        except Exception as e:
            print(f"I got an error {e}")

    def button(self):
        self.pushButton.clicked.connect(self.loaded)

    def init_handler(self):
        self.tableWidget.doubleClicked.connect(
            lambda: (
                self.show_w2(
                    (1 + self.tableWidget.currentRow(), self.is_button_upload_was_used)
                )
            )
        )

    def show_w2(self, data_from_handler):
        print(data_from_handler)
        row_id, is_button_uploaded_was_used = data_from_handler
        print(is_button_uploaded_was_used)
        if is_button_uploaded_was_used:
            cursor.execute(
                f"select key from (select row_number() over (order by key) as row_num, key, ddn, koef, prim from table1) where row_num = {row_id}"
            )
            key_with_current_row_id = cursor.fetchone()[0]
            print(f"key is: {key_with_current_row_id}")
            self.window_2 = ViewInformation(row_id)
            self.window_2.show()
        else:
            print("Please upload a data firstly!")


class ViewInformation(QtWidgets.QMainWindow, second_window.Ui_ClickedData):
    def __init__(self, key_with_current_row_id):
        super(ViewInformation, self).__init__()
        self.setupUi(self)
        self.key_with_current_row_id = key_with_current_row_id
        self.second_window_information()

    def second_window_information(self):
        for item in cursor.execute(
            f"SELECT name, pol FROM table2 WHERE key = {self.key_with_current_row_id}"
        ):
            self.lineEdit.setText(item[0])
            self.lineEdit_2.setText(str(item[1]))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Uploading_W1()
    window.show()
    sys.exit(app.exec())
    db.close()
