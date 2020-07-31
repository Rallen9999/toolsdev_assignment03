import maya.OpenMayaUI as omui
from PySide2 import QtWidgets, QtCore
from PySide2.QtCore import Slot
from shiboken2 import wrapInstance

import sys

import assetutils


def maya_main_window():
    main_window = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window), QtWidgets.QWidget)


class SmartSaveUI(QtWidgets.QDialog):

    def __init__(self):
        super(SmartSaveUI, self).__init__(parent=maya_main_window())
        self.scene = mayautils.SceneFile()
        print(self.scene.dir)
        self.setWindowTitle("Assets")
        self.resize(300, 300)
        self.setWindowFlags(self.windowFlags() ^
                            QtCore.Qt.WindowContextHelpButtonHint)
        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):
        self.title_lbl = QtWidgets.QLabel("Assets")
        self.title_lbl.setStyleSheet("font: bold 20px")

        self.dir_lbl = QtWidgets.QLabel("Directory")
        self.dir_le = QtWidgets.QLineEdit()
        self.dir_le.setText(self.scene.dir)

        self.image1_lbl = QtWidgets.QLabel("Image 1")
        self.image2_lbl = QtWidgets.QLabel("Image 2")
        self.image3_lbl = QtWidgets.QLabel("Image 3")
        self.image4_lbl = QtWidgets.QLabel("Image 4")


        self.browse_btn = QtWidgets.QPushButton("Browse...")

        self.cancel_btn = QtWidgets.QPushButton("Cancel")

    def create_layout(self):
        self.directory_lay = QtWidgets.QHBoxLayout()
        self.directory_lay.addWidget(self.dir_lbl)
        self.directory_lay.addWidget(self.dir_le)
        self.directory_lay.addWidget(self.browse_btn)

        self.mid_layout = QtWidgets.QHBoxLayout()
        self.mid_layout.addWidget(self.image1_lbl)
        self.mid_layout.addWidget(self.image2_lbl)
        self.mid_layout.addWidget(self.image3_lbl)
        self.mid_layout.addWidget(self.image4_lbl)

        self.bottom_btn_lay = QtWidgets.QHBoxLayout()
        self.bottom_btn_lay.addWidget(self.cancel_btn)

        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addWidget(self.title_lbl)
        self.main_layout.addLayout(self.directory_lay)
        self.main_layout.addLayout(self.mid_layout)

        self.main_layout.addStretch()
        self.main_layout.addLayout(self.bottom_btn_lay)
        self.setLayout(self.main_layout)

    def create_connections(self):
        self.cancel_btn.clicked.connect(self.cancel)
        self.browse_btn.clicked.connect(self.browse)

    def _populate_scenefile_properties(self):
        self.scene.dir = self.dir_le.text()

    @QtCore.Slot()
    def cancel(self):
        self.close()

    @QtCore.Slot()
    def browse(self):
        NewDirectory = QtWidgets.QFileDialog.getExistingDirectory()
        self.scene.dir = NewDirectory
        self.dir_le.setText(self.scene.dir)
