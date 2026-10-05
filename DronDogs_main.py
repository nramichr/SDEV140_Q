import sys

from PySide6.QtWidgets import QApplication, QMainWindow

import DroneDogs_ui


class MyMainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = DroneDogs_ui.Ui_DroneDogs()
		self.ui.setupUi(self)

		self.ui.pushButton_calculate_order.clicked.connect(self.calculate_order)
		self.ui.pushButton_2_Submit_order.clicked.connect(self.submit_order)
		self.ui.pushButton_3_Exit.clicked.connect(self.close)

	def calculate_order(self):
		self.statusBar().showMessage(
			"Set the dog prices and sales-tax rate to calculate the order."
		)

	def submit_order(self):
		self.statusBar().showMessage(
			"Order submission is not configured yet."
		)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MyMainWindow()
	window.show()
	sys.exit(app.exec())
