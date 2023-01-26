import xml.etree.ElementTree as parser

tree= parser.parse("store.xml")
root= tree.getroot()

for item in root:
    print(item.text)
    for sub_item in item:
        print(sub_item)