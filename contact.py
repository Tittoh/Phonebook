class Contact(object):
	def __init__(self):
		self.contact = {}

	def add_contact(self, name, number):
		self.contact[name] = number
		return {"message": "Contact added successfully"}


	def update_contact(self, name, number, new_number):
		self.number = new_number
		self.contact[name] = new_number
		return {"message": "Contact updated successfully"}


	def delete_contact(self, name, number):
		self.contact[name] = number
		return {"message": "Contact deleted successfully"}


	def view_contact(self, name, number):
		self.contact[name] = number
		return "Contact for {} is {}".format(name, number)
