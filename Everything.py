import os
import re
import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import (
    QApplication, QDialog, QFileDialog, QListWidgetItem)

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
        # 清空
        self.ui.pushButton_select.clicked.connect(
            self.ui.listWidget_result.clear)
        self.ui.lineEdit_dir.textChanged.connect(
            self.ui.listWidget_result.clear)
        self.ui.lineEdit_filePattern.textChanged.connect(
            self.ui.listWidget_result.clear)

    def dir_select(self):
        """
        select directory
        """
        chosen_dir: str = QFileDialog.getExistingDirectory(
            self, "选择查找路径", EverythingDialog.initial_path, QFileDialog.ShowDirsOnly)
        self.ui.lineEdit_dir.setText(chosen_dir)

    def find_file(self):
        """将查询结果直接输出
        """
        path = self.ui.lineEdit_dir.text()
        self.search_pattern = self.ui.lineEdit_filePattern.text().lower()
        if self.search_pattern is None:
            return
        self.ui.pushButton_find.setEnabled(False)
        self.ui.pushButton_find.repaint()
        i = 0
        for root, dirnames, filenames in os.walk(path):
            # 遍历目录
            i = self.traverse_objs(i, root, dirnames, 'd')
            # 遍历文件
            i = self.traverse_objs(i, root, filenames, 'a')

        self.ui.pushButton_find.setEnabled(True)

    def traverse_objs(self, i: int, root: str, filenames: list, file_type: str) -> int:
        """遍历文件或目录

        Parameters
        ----------
        i : int
            计数值
        root : str

        filenames : list
            文件或目录的集合
        file_type : str
            文件还是目录

        Returns
        -------
        int
            更新后的计数值
        """
        for filename in filenames:
            filename = filename.lower()
            if self.search_pattern in filename:
                i += 1
                display_text = '{0:<3} {file_type}  {1}'.format(
                    i, os.path.join(root, filename), file_type=file_type)
                item = QListWidgetItem(display_text, self.ui.listWidget_result)
                if file_type == 'd':
                    item.setForeground(QtGui.QColor("darkBlue"))
                    item.setBackground(QtGui.QColor("lightGray"))
        return i

    def show_in_explorer(self, item: QListWidgetItem):
        """
        在资源管理器中显示
        """
        filepath = os.path.abspath(
            re.sub(r'^\d+\s+[ad]  ', "", item.text()))  # 用abspath将路径中所有的/转换成\
        command = "explorer.exe /select,{}".format(filepath)
        # os.startfile(re.sub(r'^\d+ [ad]  ', "", item.text()),"explore")
        os.system(command)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EverythingDialog()

    window.show()
    sys.exit(app.exec_())
