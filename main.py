# Built-in imports

def reverse(text):
    """
    reverses text

    Parameter
    ---------
    text : str
        string to reverse

    Returns
    ---------
    str
        reversed string of text inputed
    
    """
    if(len(text) == 0):
        return ""
    else:
        return reverse(text[1:]) + text[0]

def is_palindrome(text):
    """
    checks if text is a palindrome

    Parameter
    ---------
    text : str
        string to check whether it is a palindrome

    Returns
    ---------
    boolean
        whether string is palindrome

    """
    text = text.upper().replace(" ", "")
    punc = '''!()-[]{};:'"<>./?@#$%^&*_~\,'''
    for i in text:
        if(i in punc):
            text = text.replace(i, "")

    if(len(text) <= 1):
        return True
    elif(text[0] == text[len(text) - 1]):
        return is_palindrome(text[1:len(text) - 1])
    else:
        return False
