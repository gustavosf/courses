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
    i = text[lineLength-1:].find(' ')
    if i < 0: return text
    return text[:lineLength+i-1] + '\n' + insertNewlines(text[i+lineLength:], lineLength)



if __name__ == '__main__':
    # tests for part 1 - reverse string
    assert reverseString('string') == 'gnirts'
    assert reverseString('some phrase') == 'esarhp emos'
    assert reverseString('a') == 'a'
    assert reverseString('') == ''
    # tests for part 2 - x-ian
    assert x_ian('eric', 'meritocracy') is True
    assert x_ian('eric', 'cerium') is False
    assert x_ian('john', 'mahjong') is False
    #tests for part 3 - typewriter
    assert insertNewlines('While I expect new intellectual adventures ahead, nothing will compare to the exhilaration of the world-changing accomplishments that we produced together.', 15) == "While I expect\nnew intellectual\nadventures ahead,\nnothing will compare\nto the exhilaration\nof the world-changing\naccomplishments\nthat we produced\ntogether."
    assert insertNewlines('Nuh-uh! We let users vote on comments and display them by number of votes. Everyone knows that makes it impossible for a few persistent voices to dominate the discussion.', 20) == "Nuh-uh! We let users\nvote on comments and\ndisplay them by number\nof votes. Everyone knows\nthat makes it impossible\nfor a few persistent\nvoices to dominate the\ndiscussion."