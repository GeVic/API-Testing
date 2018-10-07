# API-Testing
This is a API sample/tutorial showing basics steps to create an API and test it. `Flask`, a micro web framework written in python has been used.

## Getting Started
These instructions will get a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Type of testing performed
Unit testing library `unittest` is being used to test this Flask application. There are many other frameworks for testing like nose, doctest or unittest2 that can also be easily used.

### Reasons for using unittest
It is the built-in module for implementing unit tests in python and is easy to use and powerful at the same time.
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
### Installation
Although the project doesn't require virtualenv but I would recommend using it.

-  First fork the project and clone it through the termianal:

   ```git clone https://github.com/<your username>/API-Testing.git```

-  If you want to use virtualenv, then follow these steps. Otherwise jump to step 5.

   ```pip install virtualenv```

-  Then change directory and get to the project folder, then type:

   ```virtualenv venv```

-   Activate the enviroment

    Windows:
    ```venv\Scripts\activate```
   
    Unix:
    ```venv/bin/activate```

-  Install the requirements

   ```pip install -r rquirements.txt```

-  All set, run the application with

   ```python application.py```


### Instructions
A few libraries must be `import`ed before running the application.
The required libraries are:


|Name   |Version   |
|-------|----------|
click   |6.7
coverage|4.5.1
Flask   |1.0.2
itsdangerous|0.24
Jinja2  |2.10
MarkupSafe|1.0
psycopg2|2.7.4
