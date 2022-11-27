from ..Utils.Tokenizer import Tokenizer

class LetterIndexer:
    def __init__(self, reactions, outFile):
        self.reactions = reactions
        self.outFile = outFile