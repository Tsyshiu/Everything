import os
import sys
import re
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QListWidgetItem
from ui_everything import Ui_Dialog


class EverythingDialog(QDialog):

    initial_path: str = os.getenv("USERPROFILE") if os.getenv(
        "USERPROFILE") is not None else "C:"

    def __init__(self):
        super().__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Connect up the buttons.
        self.ui.pushButton_select.clicked.connect(self.dir_select)
        self.ui.pushButton_find.clicked.connect(self.find_file)
        self.ui.listWidget_result.itemClicked.connect(self.show_in_explorer)
        # self.ui.listWidget_result.itemDoubleClicked.connect(self.show_in_explorer)

        # 清空
        self.ui.pushButton_select.clicked.connect(
            self.ui.listWidget_result.clear)
        self.ui.textEdit_dir.textChanged.connect(
            self.ui.listWidget_result.clear)
        self.ui.textEdit_filePattern.textChanged.connect(
            self.ui.listWidget_result.clear)

    def dir_select(self):
        """
        select directory
        """
        chosen_dir: str = QFileDialog.getExistingDirectory(
            self, "选择查找路径", EverythingDialog.initial_path, QFileDialog.ShowDirsOnly)
        self.ui.textEdit_dir.setText(chosen_dir)

    def find_file(self):
        """将查询结果直接输出
        """
        self.ui.pushButton_find.setEnabled(False)
        self.ui.pushButton_find.repaint()
        path = self.ui.textEdit_dir.toPlainText()
        filename = self.ui.textEdit_filePattern.toPlainText().lower()
        i = 0
        for root, dirnames, filenames in os.walk(path):
            for dirname in dirnames:
                if filename in dirname.lower():
                    i += 1
                    write = os.path.join(root, dirname)
                    self.ui.listWidget_result.addItem(
                        '{0} d  {1}'.format(i, write))
                    # result.append(write)
            for file in filenames:
                if filename in file.lower():
                    i += 1
                    write = os.path.join(root, file)
                    self.ui.listWidget_result.addItem(
                        '{0} a  {1}'.format(i, write))
                    # result.append(write)
        self.ui.pushButton_find.setEnabled(True)

    def show_in_explorer(self, item: QListWidgetItem):
        """
        在资源管理器中显示
        """
        filepath = os.path.abspath(
            re.sub(r'^\d+ [ad]  ', "", item.text()))  # 用abspath将路径中所有的/转换成\
        command = "explorer.exe /select,{}".format(filepath)
        # os.startfile(re.sub(r'^\d+ [ad]  ', "", item.text()),"explore")
        os.system(command)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EverythingDialog()

    window.show()
    sys.exit(app.exec_())
