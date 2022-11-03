from enum import Enum, auto
from typing import Tuple, Optional


class EnglishWordClass(Enum):

    def __init__(self, description: str, alias: Optional[str] = None):
        self.description = description
        if alias:
            self.alias = alias
        else:
            self.alias = description


class WordClass(EnglishWordClass):
    NOUN = ("noun", "n")
    VERB = ("verb", "v")
    ADJECTIVE = ("adjective", "adj")
    ADVERB = ("adverb", "adv")
    PREPOSITION = ("preposition")
    PRONOUN = ("pronoun")
    DETERMINER = ("determiner")
    CONJUNCTION = ("conjunction")
    INTERJECTION = ("interjection")


class PhraseClass(EnglishWordClass):
    NOUN = "noun phrases"
    VERB = "verb phrases"
    ADJECTIVE = "adjective phrases"
    ADVERB = "adverb phrases"
    PREPOISITION = "prepositional phrases"
