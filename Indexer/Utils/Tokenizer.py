class Tokenizer:
    def __init__(self, includeDigits, caseSensitive):
        self.includeDigits = includeDigits
        self.caseSensitive = caseSensitive

    def Tokenize(self, str):
        tokens = []

        for c in str:
            ascii = ord(c)
            if (ascii >= ord('1') and ascii <= ord('9')):
                if (not self.includeDigits):
                    continue
            else:
                if (not self.caseSensitive):
                    c = c.lower()

            if c not in tokens:
                tokens.append(c)

        return tokens

            
