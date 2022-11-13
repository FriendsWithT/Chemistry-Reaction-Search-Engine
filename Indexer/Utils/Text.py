def Trim(text):
    result = text
    badChars = [' ', '\n']

    for char in badChars:
        result = result.replace(char, "")

    return result
