import sys
from PySide6.QtCore import Signal, QObject
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton


class Counter(QObject):
  changed = Signal()

  def __init__(self):
    super().__init__()

    self.value = 0

  def setValue(self, value):
    if value < 0 or value > 5:
      return

    self.value = value
    self.changed.emit()

  def increment(self):
    self.setValue(self.value + 1)

  def decrement(self):
    self.setValue(self.value - 1)


class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.counter = Counter()
    self.counter.changed.connect(self.updateLabel)

    self.setWindowTitle('PySide6 App')
    self.setMinimumSize(480, 270)
    self.setMaximumSize(480, 270)
    self.setGeometry(320, 240, 480, 270)
    self.setWindowIcon(QIcon('resources\\app.ico'))

    self.label = QLabel(self)
    self.label.setGeometry(16, 16, 448, 32)
    self.updateLabel()

    button1 = QPushButton('increment', self)
    button1.setGeometry(16, 206, 216, 48)
    button1.clicked.connect(self.onclick1)

    button2 = QPushButton('decrement', self)
    button2.setGeometry(248, 206, 216, 48)
    button2.clicked.connect(self.onclick2)

  def updateLabel(self):
    self.label.setText('Counter: ' + str(self.counter.value))

  def onclick1(self):
    self.counter.increment()

  def onclick2(self):
    self.counter.decrement()


if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  app.exec()
