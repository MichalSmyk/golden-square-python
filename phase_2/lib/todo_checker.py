def todo_checker(text):
    if text == None:
        raise Exception("Please provide a string")
    elif text.upper().find("#TODO") != -1:
        return True
    else: 
        return False
    