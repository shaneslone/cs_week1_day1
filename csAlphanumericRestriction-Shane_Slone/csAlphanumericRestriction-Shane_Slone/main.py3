def csAlphanumericRestriction(input_str):
    if input_str.isdigit():
        return True
    elif input_str.isalpha():
        return True
    else:
        return False        

