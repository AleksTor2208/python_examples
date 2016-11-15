def validatePassword(password):
    if not password:
      return "Password cannot be empty!"

    if len(password) < 5:
      return "Password has to have 5 characters at least!"

    if (' ' in password):
      return "Password cannot contain spaces!"

    return True
