from ..Utils.Tokenizer import Tokenizer
from xml.dom.minidom import Document

class LetterIndexer:
    def __init__(self, reactions, outFile, includeDigits = False, caseSensity = False):
        self.reactions = reactions
        self.outFile = outFile
        self.includeDigits = includeDigits
        self.caseSensity = caseSensity

    def index(self, verbose):
        doc = Document()
        tknr = Tokenizer(self.includeDigits, self.caseSensity)

        root = doc.createElement("Index")
        doc.appendChild(root)

        tkEleLut = {}
        rctLen = len(self.reactions)
        for rctIdx in range(0, rctLen):
            rct = self.reactions[rctIdx]
            tokens = []
            for ptcp in rct.participants:
                tokens += tknr.Tokenize(ptcp)
            for rs in rct.results:
                tokens += tknr.Tokenize(rs)

            if verbose: print("Indexing reaction [%s -> %s]." % (" + ".join(rct.participants), " + ".join(rct.results)), 
                            "Reaction [%d] out of [%d]" % (rctIdx + 1, rctLen))

            for tkIdx in range(0, len(tokens)):
                token = tokens[tkIdx]
                tkEle = tkEleLut.get(token, None)
                if not tkEle:
                    tkEle = doc.createElement("Token")
                    root.appendChild(tkEle)
                    tkEleLut[token] = tkEle

                rctEle = doc.createElement("Reaction")
                rctEle.setAttribute("id", rct.id)
                rctEle.setAttribute("Position", tkIdx)
                tkEle.appendChild(rctEle)

        of = open('%s.xml' % self.outFile, 'w')
        doc.writexml( of,
            indent="  ",
            addindent="  ",
            newl='\n')
        doc.unlink()
        of.close()
