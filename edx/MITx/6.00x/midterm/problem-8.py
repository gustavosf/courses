import re

# part of problem-5
def generateForm(story, listOfAdjs, listOfNouns, listOfVerbs):
    """
    story: a string containing sentences
    listOfAdjs: a list of valid adjectives
    listOfNouns: a list of valid nouns
    listOfVerbs: a list of valid verbs

    For each word in story that is in one of the lists,
    * replace it with the string '[ADJ]' if the word is in listOfAdjs
    * replace it with the string '[VERB]' if the word is in listOfVerbs
    * replace it with the string '[NOUN]' if the word is in listOfNouns

    returns: string, A Mad-Libs form of the story.
    """
    for word in re.findall(r"[\w]+", story):
        if (word in listOfNouns): story = story.replace(word, '[NOUN]')
        if (word in listOfAdjs): story = story.replace(word, '[ADJ]')
        if (word in listOfVerbs): story = story.replace(word, '[VERB]')
    return story

# part of problem-7
def generateTemplates(madLibsForm):
    """
    madLibsForm: string, in a Mad-Lib form. See output of `generateForm`

    returns: a list of '[ADJ]', '[VERB]', and '[NOUN]' strings, in
    the order they appear in the madLibsForm.
    """
    return re.findall(r'(\[ADJ\]|\[NOUN\]|\[VERB\])', madLibsForm)

# part of problem-8
def verifyWord(userWord, madTemplate, listOfAdjs, listOfNouns, listOfVerbs):
    """
    userWord: a string, the word the user inputted
    madTemplate: string, the type of word the user was supposed to input
    listOfAdjs: a list of valid adjectives
    listOfNouns: a list of valid nouns
    listOfVerbs: a list of valid verbs):

    returns: Boolean, whether or not the word is valid
    """
    if madTemplate == '[ADJ]' and userWord in listOfAdjs: return True
    elif madTemplate == '[NOUN]' and userWord in listOfNouns: return True
    elif madTemplate == '[VERB]' and userWord in listOfVerbs: return True
    return False

# Test cases
if __name__ == '__main__':
    story = 'The ravenous zombies started attacking yesterday'
    listOfAdjs = ['ravenous']
    listOfNouns = ['zombies', 'humans', 'yesterday']
    listOfVerbs = ['attacking', 'attacks']
    form = generateForm(story, listOfAdjs, listOfNouns, listOfVerbs)
    assert form == 'The [ADJ] [NOUN] started [VERB] [NOUN]'
    assert generateTemplates(form) == ['[ADJ]', '[NOUN]', '[VERB]', '[NOUN]']
    assert verifyWord('ravenous', '[ADJ]', listOfAdjs, listOfNouns, listOfVerbs) is True
    assert verifyWord('rave', '[ADJ]', listOfAdjs, listOfNouns, listOfVerbs) is False
    assert verifyWord('ravenous', '[VERB]', listOfAdjs, listOfNouns, listOfVerbs) is False
    assert verifyWord('ravenous', '[NOUN]', listOfAdjs, listOfNouns, listOfVerbs) is False
    assert verifyWord('humans', '[NOUN]', listOfAdjs, listOfNouns, listOfVerbs) is True
    assert verifyWord('attacks', '[VERB]', listOfAdjs, listOfNouns, listOfVerbs) is True
    assert verifyWord('attacks', '[NOUN]', listOfAdjs, listOfNouns, listOfVerbs) is False

    story = 'At the creepy thrift store I found a pair of plaid pants that looked like something your grandpa might wear'
    listOfAdjs = ['creepy', 'plaid']
    listOfNouns = ['store', 'pants', 'something', 'grandpa']
    listOfVerbs = ['found', 'looked']
    form = generateForm(story, listOfAdjs, listOfNouns, listOfVerbs)
    assert form == 'At the [ADJ] thrift [NOUN] I [VERB] a pair of [ADJ] [NOUN] that [VERB] like [NOUN] your [NOUN] might wear'
    assert generateTemplates(form) == ['[ADJ]', '[NOUN]', '[VERB]', '[ADJ]', '[NOUN]', '[VERB]', '[NOUN]', '[NOUN]']