import sys
import sql_connection
import settings_window_2

from PyQt5 import QtWidgets
from PyQt5 import QtGui

import styleMain_ui


class Settings(QtWidgets.QMainWindow, styleMain_ui.Ui_MainWindow, sql_connection.Connection):
    def __init__(self):
        super(Settings, self).__init__()
        self.setupUi(self)
        self._data = []
        self.get_values_from_the_table()
        self.button()
        self.init_handler()
        self.key_value_hider()
        self.window_2 = None
        self.is_button_upload_was_used = False

    def get_values_from_the_table(self):
        cur = self.cur.execute("SELECT ddn, koef, prim, key FROM table1")
        self._data = cur.fetchall()

    def button(self):
        self.pushButton.clicked.connect(self.loaded)

    def loaded(self):
        self.is_button_upload_was_used = True
        print(self._data)
        for i in self._data:
            self.model.appendRow([
                QtGui.QStandardItem(i[0]),
                QtGui.QStandardItem(str(i[1])),
                QtGui.QStandardItem(str(i[2])),
                QtGui.QStandardItem(str(i[3]))])

    def key_value_hider(self):
        self.tableView.hideColumn(3)

    def init_handler(self):
        self.tableView.doubleClicked.connect(self.show_w2)

    def show_w2(self, data_from_handler):
        print(data_from_handler.row(3))
        row_id = data_from_handler.row()
        self.window_2 = settings_window_2.ViewInformation(row_id, self.cur)
        self.window_2.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    table = Settings()
    table.show()
    sys.exit(app.exec_())
