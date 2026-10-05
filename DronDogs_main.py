import sys

from PySide6.QtWidgets import QApplication, QMainWindow

import DroneDogs_ui


class MyMainWindow(QMainWindow):
	TAX_RATE = 0.07
	def __init__(self):
		super().__init__()
		self.ui = DroneDogs_ui.Ui_DroneDogs()
		self.ui.setupUi(self)

		self.ui.pushButton_calculate_order.clicked.connect(self.calculate_order)
		self.ui.pushButton_2_Submit_order.clicked.connect(self.submit_order)
		self.ui.pushButton_3_Exit.clicked.connect(self.close)

	def on_calculate_order_clicked(self):
		a: int = self.ui.Spin_Box_BeefDogs.value()
		b: int = self.ui.Spin_Box_PorkDogs.value()
		c: int = self.ui.Spin_Box_TurkeyDogs.value()
		d: float = (a + b + c) * self.TAX_RATE
		self.ui.lineEdit_2_Sales_Tax.setText(f"${d:.2f}")

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
