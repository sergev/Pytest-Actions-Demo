![Python package](https://github.com/sergev/Pytest-Actions-Demo/workflows/Python%20package/badge.svg)

Here you can find a demo of a Python application with an automated testing using Github Actions service.

Anytime you want to start a new project in Python, feel free to use this code as a skeleton.
Copy the contents to your repository and build your code upon it.

File demo.py contains a code for factorial() function.

File test_demo.py has a few tests to make sure the factorial() function works correctly.

To test the code from command line, run:

    pytest -v

After every commit, visit the Actions tab and review the results of automated linting and testing.

Prerequisites:

    pip3 install pytest flake8

Links:

 * https://realpython.com/pytest-python-testing/
 * https://docs.github.com/en/actions/language-and-framework-guides/using-python-with-github-actions
 * https://flake8.pycqa.org/en/latest/
