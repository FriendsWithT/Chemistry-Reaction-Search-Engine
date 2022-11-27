from xml.dom.minidom import Document

XMLvalues = { 'a':'1', 'b':'2' }
doc = Document()

root = doc.createElement("User")
root.setAttribute( "id", 'myIdvalue' )
root.setAttribute( "email", 'blabla@bblabla.com' )

doc.appendChild(root)

for value in XMLvalues:
    # Create Element
    tempChild = doc.createElement(value)
    root.appendChild(tempChild)

# Write Text
nodeText = doc.createTextNode( XMLvalues[value].strip() )
tempChild.appendChild(nodeText)

doc.writexml( open('data.xml', 'w'),
            indent="  ",
            addindent="  ",
            newl='\n')
 
doc.unlink()