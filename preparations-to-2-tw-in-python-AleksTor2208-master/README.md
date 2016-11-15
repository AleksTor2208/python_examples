# Preparations to 2 TW in Python

## Objective of this assignment

Objective of this assignment is to show to you and explain what is Github for Education (Classrom) and how it will be used to submit next assignments.

This time we'll make this assignment together. You can treat it as tutorial of how to use Github Classroom and submit your assignment. Pay attention!

By this tutorial you will get to know how to:

* join to assignment on Github Classroom,
* clone assignment repository,
* write code and run it against tests,
* commit and submit (push) your code to assignment.

### Functional Requirements

Before we start lets focus what your program should do.

You will have to write body of `validatePassword` function that lives in `main.py` file of your repository. It has to have valid if given password is valid with the following criteria:

* Password cannot be empty. If password is empty function should return string `Password cannot be empty!`,
* Password has to contain 5 characters at least. If password is shorter function should return string `Password has to have 5 characters at least!`
* Password cannot contain spaces. If password contains spaces it should return string `Password cannot contain spaces!`.
* __If password is valid function should return `True`.__

## Getting started

__Before you start make sure you have an account on Github. If no, create new one on https://github.com.__

_From now any assignment, that require from you to submit code, will be published on Github Classroom. You will get specific link everytime you have to start new assignment._

1. Accept assignment

  This assignment is available under https://classroom.github.com/assignment-invitations/d871d71341f1dda19ac0fc8c0ebc75dc. Open this link and click _Accept this assignment_. It creates new repository that name looks like `preparations-to-2-tw-in-python-USERNAME`, where `USERNAME` is your Github username, e.g. `preparations-to-2-tw-in-python-kacperix` is assignment owned by Przemek Ciacka Mentor (his Github username is kacperix).

2. Navigate to newly created repository on Github

  Navigate to newly created repository (you can find link to it on page after you accepted assignment). Page should looks like following:

  ![alt text](https://lh5.googleusercontent.com/ojVk7McNf9KguuQs1xjN4-L8Zo5J1TmeiOIAK3cLQrhcQuplMF57kUgkP-GI_IWNDNvfovZgdS7zL9s=w3360-h1924)

3. Clone repository

  Click _"Clone or download"_ green button and copy URL of your repository. Then clone repository to your local computer by executing following command. __Keep in mind your URL will differ.__

  ```
  $ git clone git@github.com:CodecoolKrakow20161/preparations-to-2-tw-in-python-kacperix.git
  ```

4. Go to newly created directory

  ```
  $ cd preparations-to-2-tw-in-python-kacperix
  ```

5. Take a look around

  You can list directory content by `ls -l`. As you can see you cloned repository from Github. This is your working copy of this assignment. Any changes you make to this code you gonna publish to THAT specific repository.

  File you SHOULD be interested with is `main.py`. You can find there `validatePassword` function. This function's body you will work on.

  There's also `test.py` file that contains code with tests that run against `validatePassword` function from `main.py`. __Do NOT change that file__. Try to run tests and see what happen.

  ```
  $ python tests.py
  ```

  In result you should see some like following:

  ```
  FFFF
  ======================================================================
  FAIL: test_password_has_less_then_5_chars (__main__.AddTwoNumbersTest)
  ----------------------------------------------------------------------
  Traceback (most recent call last):
    File "tests.py", line 14, in test_password_has_less_then_5_chars
      "Password has to have 5 characters at least!")
  AssertionError: None != 'Password has to have 5 characters at least!'

  ======================================================================
  FAIL: test_password_has_spaces (__main__.AddTwoNumbersTest)
  ----------------------------------------------------------------------
  Traceback (most recent call last):
    File "tests.py", line 18, in test_password_has_spaces
      "Password cannot contain spaces!")
  AssertionError: None != 'Password cannot contain spaces!'

  ======================================================================
  FAIL: test_password_is_empty (__main__.AddTwoNumbersTest)
  ----------------------------------------------------------------------
  Traceback (most recent call last):
    File "tests.py", line 10, in test_password_is_empty
      "Password cannot be empty!")
  AssertionError: None != 'Password cannot be empty!'

  ======================================================================
  FAIL: test_password_is_valid (__main__.AddTwoNumbersTest)
  ----------------------------------------------------------------------
  Traceback (most recent call last):
    File "tests.py", line 21, in test_password_is_valid
      self.assertTrue(app.validatePassword("Password"))
  AssertionError: None is not true

  ----------------------------------------------------------------------
  Ran 4 tests in 0.001s

  FAILED (failures=4)
  ```

  You might think _"What the f-word is that?"_. Easy! This output gives you information that your program doesn't work as expected. Have a look on last line of output: `FAILED (failures=4)`. It means there are 4 checks (because you have defined 4 requirements) and all of them failed.

  Running tests help you to check if your program works as it is defined in requirements.

  Let start implementing these requirements.

6. Implement defined requirements

  First requirement is that password cannot be empty otherwise it should return `Password cannot be empty!`.   
  Open `main.py` and put following code:

  ```
  def validatePassword(password):
    if not password:
      return "Password cannot be empty!"
  ```

  Try to run tests again (`python tests.py`). You can notice  that last line of output shows there're only 3 failures now.

  ```
  FF.F
  ======================================================================
  FAIL: test_password_has_less_then_5_chars (__main__.AddTwoNumbersTest)
  ----------------------------------------------------------------------
  Traceback (most recent call last):
    File "tests.py", line 14, in test_password_has_less_then_5_chars
      "Password has to have 5 characters at least!")
  AssertionError: None != 'Password has to have 5 characters at least!'

  ======================================================================
  FAIL: test_password_has_spaces (__main__.AddTwoNumbersTest)
  ----------------------------------------------------------------------
  Traceback (most recent call last):
    File "tests.py", line 18, in test_password_has_spaces
      "Password cannot contain spaces!")
  AssertionError: None != 'Password cannot contain spaces!'

  ======================================================================
  FAIL: test_password_is_valid (__main__.AddTwoNumbersTest)
  ----------------------------------------------------------------------
  Traceback (most recent call last):
    File "tests.py", line 21, in test_password_is_valid
      self.assertTrue(app.validatePassword("Password"))
  AssertionError: None is not true

  ----------------------------------------------------------------------
  Ran 4 tests in 0.001s

  FAILED (failures=3)
  ```

  That means one of requirement has been passed. Great! Let's move on to conform other 3 requirements.

  ```
  def validatePassword(password):
    if not password:
      return "Password cannot be empty!"

    if len(password) < 5:
      return "Password has to have 5 characters at least!"

    if (' ' in password):
      return "Password cannot contain spaces!"

    return True
  ```

  And try to run tests now:


  ```
  $ python tests.py

  ....
  ----------------------------------------------------------------------
  Ran 4 tests in 0.000s

  OK
  ```

  Yay! All tests are passed now. That means your program works as expected.

7. Commit your changes and push code to Github

  After you've implemented your code you can commit it

  ```
  $ git add main.py
  ```

  ```
  $ git commit -m "Working program"
  ```

  and push to Github

  ```
  $ git push origin master
  ```

  And that's all. You make your first assignment using Github Classrom and automatic tests.
