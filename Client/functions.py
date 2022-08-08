import re, protocol

""" https://www.c-sharpcorner.com/article/how-to-validate-an-email-address-in-python/ """
def check_email(email):
    if len(email) > 30: return protocol.TOO_LONG
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    return protocol.VALID_INPUT if re.search(regex, email) else protocol.INVALID_INPUT

""" https://stackoverflow.com/questions/89909/how-do-i-verify-that-a-string-only-contains-letters-numbers-underscores-and-da """
def check_password(password):
    if len(password) > 30: return "Password is too long!"
    regex = "^[A-Za-z0-9!@#$%&]+$"
    return protocol.VALID_INPUT if re.search(regex, password) else protocol.INVALID_INPUT