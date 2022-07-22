from PyQt5 import QtWidgets
import second_window
import sql_connection


class ViewInformation(QtWidgets.QMainWindow, second_window.Ui_ClickedData, sql_connection.Connection):
    def __init__(self, row_id, cur):
        super(ViewInformation, self).__init__()
        self.setupUi(self)
        self.cur = cur
        self.row_id = row_id
        self.second_window_information()

    def second_window_information(self):
        cur = self.cur.execute(f"SELECT name, pol FROM table2 WHERE key = {self.row_id}")
        self.data = cur.fetchall()
        self.lineEdit.setText(str(self.data[0][0]))
        self.lineEdit_2.setText(str(self.data[0][1]))
