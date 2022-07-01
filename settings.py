import sqlite3
import sys

from PyQt5 import QtWidgets

import second_window
import window

db = sqlite3.connect("table_db12")
cursor = db.cursor()


class Uploading_W1(QtWidgets.QMainWindow, window.Ui_MainWindow):
    cursor.execute("SELECT ddn, koef, prim, key FROM table1")
    db_data = cursor.fetchall()

    def __init__(self):
        super(Uploading_W1, self).__init__()
        self.setupUi(self)
        self.button()
        self.init_handler()
        self.key_hider()
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
                self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(rows[3])))
                i += 1
        except Exception as e:
            print(f"I got an error {e}")

    def button(self):
        self.pushButton.clicked.connect(self.loaded)

    def init_handler(self):
        self.tableWidget.doubleClicked.connect(
            lambda: (
                self.show_w2(
                    (
                    int(self.tableWidget.item(self.tableWidget.currentRow(), 3).text()), self.is_button_upload_was_used)
                )
            )
        )

    def show_w2(self, data_from_handler):
        print(data_from_handler)
        row_id, is_button_uploaded_was_used = data_from_handler
        if is_button_uploaded_was_used:
            print(f"key is: {row_id}")
            self.window_2 = ViewInformation(row_id)
            self.window_2.show()
        else:
            print("Please upload a data firstly!")

    def key_hider(self):
        self.tableWidget.hideColumn(3)


class ViewInformation(QtWidgets.QMainWindow, second_window.Ui_ClickedData):
    def __init__(self, row_id):
        super(ViewInformation, self).__init__()
        self.setupUi(self)
        self.row_id = row_id
        self.second_window_information()

    def second_window_information(self):
        for item in cursor.execute(
                f"SELECT name, pol FROM table2 WHERE key = {self.row_id}"
        ):
            self.lineEdit.setText(item[0])
            self.lineEdit_2.setText(str(item[1]))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Uploading_W1()
    window.show()
    sys.exit(app.exec())
    db.close()
