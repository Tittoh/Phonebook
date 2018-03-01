import unittest

from contact import Contact

class TestContact(unittest.TestCase):
    def test_add_contact(self):
        contact = Contact()
        response = contact.add_contact("Tittoh", "0729261228")
        self.assertEqual(response["message"], "Contact added successfully")

	def test_update_contact(self):
		contact = Contact()
		response = contact.update_contact({"Tittoh", "0729261228"},{"Tittoh", "0736197716"})
		self.assertEqual(response["message"], "Contact updated successfully")

	def test_delete_contact(self):
		contact = Contact()
		response = contact.delete_contact("Ken", "0734123456")
		self.assertEqual(response["message"], "Contact deleted successfully")

	def test_view_contact(self):
		contact = Contact()
		response = contact.view_contact()
		self.assertEqual(response["message"], "All contacts displayed")

if __name__ == '__main__':
	unittest.main()
