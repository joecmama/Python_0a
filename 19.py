#!/usr/bin/env python

# wrapping C code, graphical user interface

import sys, pyqtgraph, numpy, math
from PyQt4 import QtCore, QtGui
from myimage import MyImage

class MyWindow(QtGui.QWidget):

    def __init__(self):

        super(MyWindow, self).__init__()

        # buttons and box to put them in
        s = QtGui.QPushButton('Save', self)
        s.clicked.connect(self.save)
        p = QtGui.QPushButton('Play', self)
        p.clicked.connect(self.play)
        q = QtGui.QPushButton('Quit', self)
        q.clicked.connect(QtCore.QCoreApplication.instance().quit)
        button_box = QtGui.QVBoxLayout()
        button_box.addWidget(s)
        button_box.addWidget(p)
        button_box.addWidget(q)
        button_box.addStretch(1)

        # PyQt graph image view
        self.image = MyImage()
        self.image_view = pyqtgraph.ImageView(self)
        self.image_view.setFixedSize(self.image.nrows, self.image.ncols)

        # table of parameters
        self.params = ['# frames','channel','etc']
        self.nparam = len(self.params)
        
        self.table = QtGui.QTableWidget(self)
        self.table.setRowCount(self.nparam)
        self.table.setColumnCount(1)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setHorizontalHeaderLabels([''])
        self.table.setVerticalHeaderLabels(self.params)

        # put button box, image view, table in horizontal box
        hbox = QtGui.QHBoxLayout()
        hbox.addLayout(button_box)
        hbox.addStretch(1)
        hbox.addWidget(self.image_view)
        hbox.addStretch(1)
        hbox.addWidget(self.table)

        self.setLayout(hbox)
        self.show()

    def table_item(self, i):
        item = self.table.item(0,i)
        return str(item.text()) if item else ''

    def param_dict(self):
        return dict(zip(self.params,[self.table_item(i) for i in range(0,self.nparam)]))

    def play(self):
        self.image.get()
	self.image_view.setImage(self.image.data)

    def save(self):
        with open(QtGui.QFileDialog.getSaveFileName(self, 'Save file', ''), 'w') as f:
            f.write(str(self.param_dict()))

if __name__ == '__main__':        
    # run app
    app = QtGui.QApplication(sys.argv)
    win = MyWindow()
    sys.exit(app.exec_())
