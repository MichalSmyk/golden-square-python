def todo_checker(text):
    if text.upper().find("#TODO") != -1:
        return True
    else: 
        return False
    