import re
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


if __name__ == '__main__':
    # Test Case 1
    story = 'The ravenous zombies started attacking yesterday'
    listOfAdjs = ['ravenous']
    listOfNouns = ['zombies', 'humans', 'yesterday']
    listOfVerbs = ['attacking', 'attacks']
    assert generateForm(story, listOfAdjs, listOfNouns, listOfVerbs) == 'The [ADJ] [NOUN] started [VERB] [NOUN]'

    # Test Case 2
    story = 'At the creepy thrift store I found a pair of plaid pants that looked like something your grandpa might wear'
    listOfAdjs = ['creepy', 'plaid']
    listOfNouns = ['store', 'pants', 'something', 'grandpa']
    listOfVerbs = ['found', 'looked']
    assert generateForm(story, listOfAdjs, listOfNouns, listOfVerbs) == 'At the [ADJ] thrift [NOUN] I [VERB] a pair of [ADJ] [NOUN] that [VERB] like [NOUN] your [NOUN] might wear'