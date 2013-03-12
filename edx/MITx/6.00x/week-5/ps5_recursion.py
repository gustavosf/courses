# 6.00x Problem Set 5
#
# Part 2 - RECURSION

#
# Problem 3: Recursive String Reversal
#
def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.

    aStr: a string
    returns: a reversed string
    """
    if not aStr: return ''
    return aStr[-1] + (reverseString(aStr[:-1]) if len(aStr) > 1 else '')

#
# Problem 4: X-ian
#
def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.

    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
    if (x and not word): return False
    if (not x): return True
    return (x[0] in word) and (x_ian(x[1:], word[word.index(x[0])+1:]))

#
# Problem 5: Typewriter
#
def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately.
    """
    ### TODO.



if __name__ == '__main__':
    # tests for part 1
    assert reverseString('string') == 'gnirts'
    assert reverseString('some phrase') == 'esarhp emos'
    assert reverseString('a') == 'a'
    assert reverseString('') == ''
    # tests for part 2
    assert x_ian('eric', 'meritocracy') is True
    assert x_ian('eric', 'cerium') is False
    assert x_ian('john', 'mahjong') is False
