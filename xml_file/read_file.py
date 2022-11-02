import xml.dom.minidom as xmldom
import re

xml_file = xmldom.parse('./chtb_0001.xml')

Relation = xml_file.getElementsByTagName("R")
Paragraph = xml_file.getElementsByTagName("P")

#Relations
for item in Relation:
    center=int(item.getAttribute('Center'))
    print(center)
#Paragraphs
for para in Paragraph:
    print(para.getAttribute('Function'))
    print(para.childNodes[0].data)