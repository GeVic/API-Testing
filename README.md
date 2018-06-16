# API-Testing
This is a sample API showing basics steps in creating API and its testing. Micro web framework written in python called Flask is used

## Type of testing performed
Though there are many frameworks for testing like nose, doctest or unittest2 and others but unittest is the one used in this Flask Application. 

## Reasons for using unittest
It is the built=in module for implementing unit tests in python and is easy to use and powerful at the same time.
See below for a basic structure:

```python
import unittest 

class testClass(unittest.TestCase): 

  # First method to be executed
  @classmethod
  def setUpClass(cls):
       pass 

  # Last method to be executed
  @classmethod
  def tearDownClass(cls):
       pass 

  # initialization logic
  # code that is executed before each test
  def setUp(self):
    pass 

  # clean up logic
  # code that is executed after each test
  def tearDown(self):
    pass 

  # test method
  def test_equality(self):
    self.assertEqual(1, 1) 

# runs the unit tests in the module
if __name__ == '__main__':
  unittest.main()
```
## Instructions 
There are some python libraries that is to be imported before giving the application a run.
List of the libraries required is as follows

|Name   |Version   |
|-------|----------|
click   |6.7
coverage|4.5.1
Flask   |1.0.2
itsdangerous|0.24
Jinja2  |2.10
MarkupSafe|1.0
psycopg2|2.7.4
