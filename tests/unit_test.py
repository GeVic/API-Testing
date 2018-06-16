import unittest
from application import app

class test(unittest.TestCase): 

    def setUp(self):
      self.app = app.test_client()
    
    def tearDown(self):
      pass

    def post_location(self, pincode, place, city, longitude, latitude):
      response = self.app.post(
        '/location',
        data = dict(pincode=pincode, place=place, city=city, longitude=longitude, latitude=latitude),
        follow_redirects=True
      )
      return response

    def test_commit_location(self):
      response = self.post_location('122549','Budhera','Haryana','76.93','28.49')
      self.assertEqual(response.status_code, 200)

    def test_duplicate_commit(self):
      response = self.post_location('122548','Farrukhnagar','Haryana','77.69','28.45')
      self.assertEqual(response.status_code, 200)
      response = self.post_location('122548','Farrukhnagar','Haryana','77.69','28.45')
      self.assertIn(b'Not added to Database! Pincode already exist in Database.', response.data)

    def test_index_page(self):
      response = self.app.get('/', follow_redirects=True)
      self.assertEqual(response.status_code, 200)
    
        
if __name__ == "__main__":
    unittest.main()