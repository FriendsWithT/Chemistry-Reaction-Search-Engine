from Indexer.ReadModule.XMLReader import XMLReader
from Indexer.IndexModule.LetterIndexer import LetterIndexer

def main():
    myReader = XMLReader("Reactions.xml")
    reactions = myReader.read()

    myIndexer = LetterIndexer(reactions, outFile = "rctIdx")
    myIndexer.index(verbose = True)

if __name__ == "__main__":
    main()