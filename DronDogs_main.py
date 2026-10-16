"""
DroneDogs Final Project (Part 4)

This program is the DroneDogs ordering system. It lets the user pick how many
beef, pork, and turkey hot dogs they want, calculates the subtotal, sales tax,
and total cost, and submits the order for drone delivery.

The main Order Input form connects to a Customer Information form where the
user can view saved customers, add new ones, and pick a customer for the order.
The selected customer's first name, last name, and email are sent back to the
Order Input form. Customers are saved in a customers.json file so they stay
saved after the program closes.

Before an order is submitted, the program checks that location permission is
given, the order has been calculated, and a customer email is filled in.

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
	"""Customer Information form. Shows saved customers and lets the user add or select one."""
	def __init__(self):
		"""Sets up the customer form, links the buttons to their functions, and loads the customer list."""
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
		"""Takes the name and email typed in, adds them to the customer list, saves it to customers.json, and refreshes the list."""
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
		"""Finds the customer the user clicked on, stores their info in the global variables, and closes the form."""
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
		"""Clears the list box and fills it with every customer's name and email."""
		self.customer_list.clear()
		for customer in customer_list:
			self.customer_list.addItem(f"{customer['first_name']} {customer['last_name']}  ({customer['email']})")
	
	def give_permission(self, granted: bool):
		"""Shows a permission message in the status bar. Not used by the dialog, since only the main window has a status bar."""
		message = "Permission granted." if granted else "Permission not granted."
		self.statusBar().showMessage(message)

class MyMainWindow(QMainWindow):
	"""Main Order Input form where the user builds, calculates, and submits an order."""
	def __init__(self):
		"""Sets up the order form, connects all the buttons and the check box, and makes the customer fields read-only."""
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
		"""Shows in the status bar whether location permission was checked or unchecked."""
		message = "Permission granted." if granted else "Permission not granted."
		self.statusBar().showMessage(message)

	def on_clear_form_button_clicked(self):
		"""Resets the spin boxes to 0, clears all text boxes, and unchecks the permission box for a new order."""
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
		"""Opens the Customer Information form and fills in the customer fields if a customer was selected."""
		dialog = Mydialog2()
		re_val: int = dialog.exec()
		if re_val == QDialog.DialogCode.Accepted:
			self.ui.lineEdit_firstname.setText(first_name)
			self.ui.lineEdit_lastname.setText(last_name)
			self.ui.lineEdit_Email.setText(email)

	# Gets the number of hot dogs from the spin boxes and works out the order
	def calculate_order(self):
		"""Adds up the hot dogs, works out subtotal, tax, and total, and shows them as money. Warns the user if no hot dogs were picked."""
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

	# checks if the permission check box is checked, if there is something in the total cost text box, and if there is something in the customer email text box. If any of these are not filled in, the program displays an appropriate error message. If they are all OK, a message box is displayed thanking the user for placing the order.
	def submit_order(self):
		"""Checks for location permission, a calculated total, and a customer email. Shows an error if any are missing, or a thank you message if everything is good."""
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