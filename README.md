# Tests Orientation
This repository contains a simple test suite implemented using pytest, a popular testing framework for Python.

## Project Structure
The project is structured with folders to simulate a real-world project, showcasing good organization practices. The structure may include directories such as tests, src, and others, depending on your project's complexity.


project-root/ \n
| \n
├── tests/

project-root/ 
| 
├── tests/ 
│   ├── test_module1.py 
│   ├── test_module2.py 
│   └── ... 
│  
├── src/ 
|   ├── __init__.py 
│   ├── module1.py 
│   ├── module2.py 
│   └── ... 
│ 
└── ... 


## Mock Data
Mocks within the tests can be created using either static or dynamic data. This flexibility allows you to simulate different scenarios and test your code under various conditions.

## Static Data
In some cases, it might be appropriate to use static data, such as predefined values or fixtures, to create mock scenarios.

## Dynamic Data
For more dynamic tests, consider generating mock data during runtime. This can be achieved using libraries like Faker or by dynamically creating test data based on your project's requirements.

Running Tests
To run the tests, ensure you have pytest installed. If not, you can install it using:

-> *pip install pytest*

Afterwards, execute the tests using the following command in the project root directory:

-> *pytest*

This will discover and run all the tests in the tests directory.
