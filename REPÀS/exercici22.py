import xml.etree.ElementTree as ET

root = ET.Element("students")
for x in range(5):
    sub = ET.SubElement(root, "student")
    for y in range(4):
        subsub1 = ET.SubElement(sub, "name")
        subsub1.set("creador", "Guifre")
        subsub2 = ET.SubElement(sub, "surname")
        subsub2.set("creador", "Guifre")
        subsub3 = ET.SubElement(sub, "email")
        subsub3.set("creador", "Guifre")
        subsub4 = ET.SubElement(sub, "dni")
        subsub4.set("creador", "Guifre")
tree = ET.ElementTree(root)
ET.dump(tree)

tree.write("prova.xml")
