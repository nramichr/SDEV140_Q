import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from dialog_2_ui import Ui_Dialog

import DroneDogs_ui

first_name: str = ""
last_name: str = ""
email: str = ""

customer_list: list = []
customer_list.append({"first_name": 'Barney', "last_name": 'Rubble', "email": 'barney.rubble@bedrock.com'})
customer_list.append({"first_name": 'Fred', "last_name": 'Flintstone', "email": 'fred.flintstone@bedrock.com'})

class Mydialog2(QDialog):
	def __init__(self):
		super().__init__()
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)

		self.customer_list = self.ui.listWidget
		self.first_name = self.ui.lineEdit_firstname
		self.last_name = self.ui.lineEdit_lastname
		self.email = self.ui.lineEdit_email

		self.add_customer_button = self.ui.pushButton_addcustomer
		self.add_customer_button.clicked.connect(self.add_customer)
		self.select_customer_button = self.ui.pushButton_2
		self.select_customer_button.clicked.connect(self.on_select_customer_button_clicked)
		self.load_customer_list()

	def add_customer(self):
		global customer_list
		new_customer = {
			"first_name": self.first_name.text(),
			"last_name": self.last_name.text(),
			"email": self.email.text()
		}
		customer_list.append(new_customer)
		self.load_customer_list()

	def on_select_customer_button_clicked(self):
		selected_items = self.customer_list.selectedItems()
		if not selected_items:
			return
		
		selected_text = selected_items[0].text()
		for customer in customer_list:
			if f"{customer['first_name']} {customer['last_name']}  ({customer['email']})" == selected_text:
				global first_name, last_name, email
				first_name = customer['first_name']
				last_name = customer['last_name']
				email = customer['email']
				self.accept()
				break

	def load_customer_list(self):
		self.customer_list.clear()
		for customer in customer_list:
			self.customer_list.addItem(f"{customer['first_name']} {customer['last_name']}  ({customer['email']})")
class MyMainWindow(QMainWindow):
	TAX_RATE = 0.07
	def __init__(self):
		super().__init__()
		self.ui = DroneDogs_ui.Ui_DroneDogs()
		self.ui.setupUi(self)

		self.calc_button = self.ui.pushButton_calculate_order
		self.submit_button = self.ui.pushButton_2_Submit_order
		self.exit_button = self.ui.pushButton_3_Exit
		self.customer_dialogbutton = self.ui.Pushbutton_CustomerInfor
		self.customer_dialogbutton.clicked.connect(self.on_customer_dialog_button_clicked)
		self.clear_form_button = self.ui.Pushbutton_ClearForm
		self.clear_form_button.clicked.connect(self.on_clear_form_button_clicked)
		self.ui.checkBox_permission.toggled.connect(self.give_permission)

		self.calc_button.clicked.connect(self.calculate_order)
		self.submit_button.clicked.connect(self.submit_order)
		self.exit_button.clicked.connect(self.close)

	def on_give_permission_buton_clicked(self):
		print("Permission granted.")

	def give_permission(self, granted: bool):
		message = "Permission granted." if granted else "Permission not granted."
		self.statusBar().showMessage(message)

	def on_clear_form_button_clicked(self):
		self.ui.Spin_Box__BeefDogs.setValue(0)
		self.ui.Spin_Box__PorkDogs.setValue(0)
		self.ui.Spin_Box__TurkeyDogs.setValue(0)
		self.ui.lineEdit_Subtotal.clear()
		self.ui.lineEdit_2_Sales_Tax.clear()
		self.ui.lineEdit_3_Total_cost.clear()
		self.ui.lineEdit_firstname.clear()
		self.ui.lineEdit_lastname.clear()
		self.ui.lineEdit_Email.clear()
		self.ui.checkBox_permission.setChecked(False)

	def on_customer_dialog_button_clicked(self):
		dialog = Mydialog2()
		re_val: int = dialog.exec()
		if re_val == QDialog.DialogCode.Accepted:
			self.ui.lineEdit_firstname.setText(first_name)
			self.ui.lineEdit_lastname.setText(last_name)
			self.ui.lineEdit_Email.setText(email)

	def on_calculate_order_clicked(self):
		a: int = self.ui.Spin_Box__BeefDogs.value()
		b: int = self.ui.Spin_Box__PorkDogs.value()
		c: int = self.ui.Spin_Box__TurkeyDogs.value()
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
