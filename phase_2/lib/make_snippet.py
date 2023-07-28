def make_snippet(str):
    words = str.split()
    if len(words) > 5:
        return " ".join(words[:5]) + '...'
    else:
        return str