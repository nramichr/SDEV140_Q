"""
Part 3 DroneDogs Final Project

We love the new ordering system and the operation of the Order Input form, but would now like to add a
Customer Information form to the system. The Customer Information form will display existing customers
(first name, last name, and email address) and allow the user to add new customers. Users can select a
new or existing customer, and the first name, last name and email address of the selected customer will be
automatically transferred back to the Order Input form before the order is submitted.

In specific, we are requesting that you (see figures below for visual details):

1. Add a Get Customer Info button to the Order Input form. Clicking that button should open the new
Customer Information form.

2. Add the fields from the Customer Information form to the Order Input form, so that the information can
be transferred there after a customer is selected from the Customer Information form.

3. Add a Clear Form button to the Order Input form, which will clear all the text boxes when the user is
ready to add a new order.

4. Add a check box to the Order Input form, allowing DroneDogs to use location services to determine
where the drone will deliver the order.

5. Modify the code for the Submit Order button. When the user clicks this button, the program will check to
see if:

a) the permission check box is checked,
b) there is something in the total cost text box, and
c) there is something in the customer email text box.

If any of these are not filled in, the program displays an appropriate error message. If they are all
OK, a message box is displayed thanking the user for placing the order.

Christian Ramirez-Flores
"""
import json
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from dialog_2_ui import Ui_Dialog

import DroneDogs_ui

first_name: str = ""
last_name: str = ""
email: str = ""

# Constants: these values don't change while the program runs
SALES_TAX_RATE: float = 0.07
HOT_DOG_PRICE: float = 1.99


customer_list: list = []
customer_list.append({"first_name": 'Barney', "last_name": 'Rubble', "email": 'barney.rubble@bedrock.com'})
customer_list.append({"first_name": 'Fred', "last_name": 'Flintstone', "email": 'fred.flintstone@bedrock.com'})

# Try to load the customer list from a JSON file, if it exists
try:
	 with open('customers.json', 'r') as customer_file:
		 customer_list = json.load(customer_file)
except FileNotFoundError:
	print("customers.json file not found. Starting with an empty customer list.")
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
	
	# Adds the customer typed into the text boxes to the list of customers and saves it to the JSON file
	def add_customer(self):
		global customer_list
		new_customer = {
			"first_name": self.first_name.text(),
			"last_name": self.last_name.text(),
			"email": self.email.text()
		}
		customer_list.append(new_customer)
		with open('customers.json', 'w') as customer_file:
			json.dump(customer_list, customer_file)
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
	
	def give_permission(self, granted: bool):
		message = "Permission granted." if granted else "Permission not granted."
		self.statusBar().showMessage(message)

class MyMainWindow(QMainWindow):
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

		self.ui.lineEdit_firstname.setReadOnly(True)
		self.ui.lineEdit_lastname.setReadOnly(True)
		self.ui.lineEdit_Email.setReadOnly(True)

	# Shows in the status bar whether location permission was given
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

	# Gets the number of hot dogs from the spin boxes and works out the order
	def calculate_order(self):
		num_beef_dogs: int = self.ui.Spin_Box__BeefDogs.value()
		num_pork_dogs: int = self.ui.Spin_Box__PorkDogs.value()
		num_turkey_dogs: int = self.ui.Spin_Box__TurkeyDogs.value()
		total_dogs: int = num_beef_dogs + num_pork_dogs + num_turkey_dogs

		if total_dogs == 0:
			self.ui.lineEdit_Subtotal.setText("$0.00")
			self.ui.lineEdit_2_Sales_Tax.setText("$0.00")
			self.ui.lineEdit_3_Total_cost.setText("$0.00")
			QMessageBox.warning(self, "No Dogs Selected", "Please select at least one hot dog to calculate the order.")
			return

		# All hot dogs are the same price, so subtotal is total dogs x price
		subtotal: float = total_dogs * HOT_DOG_PRICE
		sales_tax: float = subtotal * SALES_TAX_RATE
		total_cost: float = subtotal + sales_tax

		# Show the amounts as money with two decimal places
		self.ui.lineEdit_Subtotal.setText(f"${subtotal:.2f}")
		self.ui.lineEdit_2_Sales_Tax.setText(f"${sales_tax:.2f}")
		self.ui.lineEdit_3_Total_cost.setText(f"${total_cost:.2f}")
		self.statusBar().showMessage("Order calculated")

	# Makes sure the order was calculated
	def submit_order(self):
		if not self.ui.checkBox_permission.isChecked():
			QMessageBox.warning(self, "No Permission", "You must give permission for location services before submitting the order.")
			return
		elif self.ui.lineEdit_3_Total_cost.text() in ("", "$0.00"):
			QMessageBox.warning(self, "No Order", "You must calculate the order before submitting.")
			return
		elif self.ui.lineEdit_Email.text() == "":
			QMessageBox.warning(self, "No Email", "You must select a customer before submitting the order.")
			return
		else:
			QMessageBox.information(self, "DroneDogs", "Thank you for ordering your meal from DroneDogs!")
			self.statusBar().showMessage("Your order has been submitted!")




if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MyMainWindow()
	window.show()
	sys.exit(app.exec())