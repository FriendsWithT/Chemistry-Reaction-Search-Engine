from .BaseReader import Reader
from xml.dom.minidom import parse
from Indexer.Utils.Text import Trim
from Indexer.Model.Reaction import Reaction

class XMLReader(Reader):
    def __init__(self, sourceFile):
        super().__init__(sourceFile)

    def read(self):
        reactions = []

        dom = parse(self.dataSource)
        rctDoms = dom.getElementsByTagName("reaction")

        for rctDom in rctDoms:
            id = self.getValuesFromTag(rctDom, "id")[0]
            ptcps = self.getValuesFromTag(rctDom, "participant")
            rslts = self.getValuesFromTag(rctDom, "result")

            reaction = Reaction(id, ptcps, rslts)
            reactions.append(reaction)

        return reactions

    def getValuesFromTag(self, dom, tagName):
        values = []

        chldDoms = dom.getElementsByTagName(tagName)
        for chldDom in chldDoms:
            value = chldDom.firstChild.nodeValue
            value = Trim(value)
            values.append(value)

        return values