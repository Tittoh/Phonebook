import unittest

from contact import Contact

class TestContact(unittest.TestCase):
	def setUp(self):
		self.contact = Contact()

	def test_add_contact(self):
		result = self.contact.add_contact("Tittoh", "0729261228")
		self.assertEqual(result["message"], "Contact added successfully")

	def test_update_contact(self):
		result =self.contact.update_contact("Tittoh", "0729261228", "0736197716")
		self.assertEqual(result["message"], "Contact updated successfully")

	def test_delete_contact(self):
		result = self.contact.delete_contact("Ken", "0734123456")
		self.assertEqual(result["message"], "Contact deleted successfully")

	def test_view_contact(self):
		result = self.contact.view_contact("Emmy", "099345667")
		self.assertEqual(result, "Contact for Emmy is 099345667")
