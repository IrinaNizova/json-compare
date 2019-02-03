import unittest
from script import compare_jsons

order = {
  "orderID": 12345,
  "shopperName": "Ваня Иванов",
  "shopperEmail": "ivanov@example.com",
  "contents": [
    {
      "productID": 34,
      "productName": "Супер товар",
      "quantity": [1, 0]
    },
    {
      "productID": 56,
      "productName": "Чудо товар",
      "quantity": 4.12
    }
  ],
  "orderCompleted": True
 }
 
order2 = {
  "orderID": 12345,
  "shopperName": "Ваня Иванов",
  "shopperEmail": "ivanov@example.com",
  "contents": [
    {
      "productID": 34,
      "productName": "Супер товар",
      "quantity": [1, 0]
    },
    {
      "productID": 56,
      "productName": "Чудо товар",
      "quantity": 4.12
    }
  ],
  "orderCompleted": True
 }

class TestJsonMethods(unittest.TestCase):

	def test1_equal(self):
		self.assertTrue(compare_jsons(order, order2))
	  
	def test2_diff_value(self):
		order2["contents"][0]["productID"] = 55
		self.assertFalse(compare_jsons(order, order2))
		
	def test3_diff_float_value(self):
		order["contents"][0]["productID"] = 55.123456789
		order2["contents"][0]["productID"] = 55.123456
		self.assertTrue(compare_jsons(order, order2))
	
	def test4_diff_structure(self):
		del order2["contents"][0]["productID"]
		self.assertFalse(compare_jsons(order, order2))

if __name__ == '__main__':
    unittest.main()