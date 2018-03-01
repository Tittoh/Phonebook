class Contact:
	def __init__(self):
		self.contact = {}

	def add_contact(self, name, number):
		self.contact["name"] = name
		self.contact["number"] = number
		return {"message": "Contact added successfully"}


	def update_contact(current_number, new_number):
		self.contact["name"] = name
		self.contact["number"] = number
		return {"message": "Contact updated successfully"}


	def delete_contact(self, neme, number):
		self.contact["name"] = name
		self.contact["number"] = number
		return {"message": "Contact deleted successfully"}


	def view_contact(self, name, number):
		self.contact["name"] = name
		self.contact["number"] = number
		return {"message": "Contact found successfully"}
