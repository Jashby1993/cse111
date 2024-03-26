import random   

quantity = random.randint(1,2)
quantity_2 = random.randint(1,2) 
tenses = ["past","present","future"]
tense = random.choice (tenses)
prepositional_quantity = random.randint(1,2)
prepositional_quantity_2 = random.randint(1,2)

def main():
    complex_sentence = make_complex_sentence(quantity, prepositional_quantity, prepositional_quantity_2, quantity_2, tense).capitalize()
    single_past = make_sentence(1,prepositional_quantity, prepositional_quantity_2, "past")
    single_present = make_sentence(1,prepositional_quantity, prepositional_quantity_2, "present")
    single_future = make_sentence(1,prepositional_quantity, prepositional_quantity_2, "future")
    plural_past = make_sentence(2,prepositional_quantity_2, prepositional_quantity, "past")
    plural_present = make_sentence(2,prepositional_quantity_2,prepositional_quantity, "past")
    plural_future = make_sentence(2,prepositional_quantity_2,prepositional_quantity ,"future")

    print(single_past)
    print(single_present)
    print(single_future)
    print(plural_past)
    print(plural_present)
    print(plural_future)
    print(complex_sentence)
    
#pick a determiner
def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    determiner = random.choice(words)
    return determiner
#pick a noun
def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child","dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children","dogs", "girls", "men", "rabbits", "women"]

    noun = random.choice(words)
    return noun
#pick a verb
def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    
    elif tense == "present" and quantity == 1:
        words = ["drinks", "eats", "grows", "laughs", "thinks","runs", "sleeps", "talks", "walks", "writes"]
    
    elif tense == "present" and quantity != 1:
        words = ["drink", "eat", "grow", "laugh", "think","run", "sleep", "talk", "walk", "write"]
    
    else:
        words = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    
    verb = random.choice(words)

    return verb
#put em together
#stretch requirements: two prepositional phrases in each sentence and added adjectives and adverbs

def make_sentence(quantity,prepositional_quantity,prepositional_quantity_2, tense):
    """Build and return a sentence with three words:
    a determiner, a noun, and a verb. The grammatical
    quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.
    """
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    adjective = get_adjective()
    adverb = get_adverb()
    prepositional_phrase = get_prepositional_phrase(prepositional_quantity)
    prepositional_phrase_2 = get_prepositional_phrase(prepositional_quantity_2)

    sentence = str(f"{determiner} {adjective} {noun} {verb} {adverb} {prepositional_phrase} {prepositional_phrase_2}.").capitalize()

  
    return sentence
    #put em together
#stretch requirements: acheived the sentence structure mentioned in the ponder section
def make_complex_sentence(quantity, prepositional_quantity, prepositional_quantity_2, quantity_2, tense):
    
    determiner = get_determiner(quantity)
    adjective_1 = get_adjective()
    noun = get_noun(quantity)
    verb = get_verb(quantity,tense)
    prepositional_phrase= get_prepositional_phrase(prepositional_quantity)
    adverb_1 = get_adverb()
    determiner_2 = get_determiner(quantity_2)
    adjective_2 = get_adjective()
    noun_2 = get_noun(quantity_2)
    prepositional_phrase_2 = get_prepositional_phrase(prepositional_quantity_2)
    #sentence = str(determiner + " " + adjective_1 + " " + noun + " " + verb +" " + prepositional_phrase+ " "+ adverb_1 + " " + prepositional_phrase_2 + ".").capitalize()
    sentence = str(f"{determiner} {adjective_1} {noun} {prepositional_phrase} {adverb_1} {verb} {determiner_2} {adjective_2} {noun_2} {prepositional_phrase_2}.")
    return sentence 

#choose a preposition
def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
    "about", "above", "across", "after", "along",
    "around", "at", "before", "behind", "below",
    "beyond", "by", "despite", "except", "for",
    "from", "in", "into", "near", "of",
    "off", "on", "onto", "out", "over",
    "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    prepositions = ["about", "above", "across", "after", "along","around", "at", "before", "behind", "below","beyond", "by", "despite", "except", "for","from", "in", "into", "near", "of","off", "on", "onto", "out", "over","past", "to", "under", "with", "without"]
    preposition = random.choice(prepositions)
    return preposition

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or pluaral.
    Return: a prepositional phrase.
    """
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    prepositional_phrase = str(preposition + " " + determiner + " " + noun)
    return prepositional_phrase

def get_adjective():
    adjectives = ["beautiful", "brave", "clever", "delightful", "elegant", "friendly", "graceful", "handsome", "intelligent", "joyful", "kind", "lovely", "magnificent", "noble", "optimistic"]
    adjective = random.choice(adjectives)
    return adjective

def get_adverb():
    adverbs = ["quickly", "happily", "carefully", "patiently", "gently", "quietly", "eagerly", "gracefully", "honestly", "kindly", "loudly", "politely", "suddenly", "wisely", "warmly"]
    adverb = random.choice(adverbs)
    return adverb


main()