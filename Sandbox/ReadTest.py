from Indexer.ReadModule.XMLReader import XMLReader

def main():
    myReader = XMLReader("Reactions.xml")
    reactions = myReader.read()

    for reaction in reactions:
        print("id: ", reaction.id)
        print("participants: ", ", ".join(reaction.participants))
        print("results: ", ", ".join(reaction.results))

if __name__ == "__main__":
    main()