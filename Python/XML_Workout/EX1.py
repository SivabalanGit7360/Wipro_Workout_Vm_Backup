import xml.etree.ElementTree as ET

tree = ET.parse('XML_Workout/movies.xml')

root = tree.getroot()

'''
print root.tag

print root.attrib
'''

# print the child of root

#for child in root:
#    print(child.tag,child.attrib)
    
# print all child nodes

#for child in root.iter():
#    print(child.tag, child.attrib)
 
#for child in root.iter('movie'):
#    print(child.tag, child.attrib)
    

for m in root.findall("./genre/decade/movie/[year='1992']"):
    print(m.attrib)
