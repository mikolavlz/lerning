
import xml.etree.cElementTree as tree
root = tree.Element('goods') #корневой элемент
good1 = tree.SubElement(root,'good',id='1') # первы потомок
tree.SubElement(good1,'title').text = 'Audi' #вложеные элементы
tree.SubElement(good1,'price').text = '1000'

good2 = tree.SubElement(root,'good',id='2') # первы потомок
tree.SubElement(good2,'title').text = 'BMW' #вложеные элементы
tree.SubElement(good2,'price').text = '1200'

good3 = tree.SubElement(root,'good',id='3') # первы потомок
tree.SubElement(good3,'title').text = 'VW' #вложеные элементы
tree.SubElement(good3,'price').text = '1300'

my_tree = tree.ElementTree(root) #получим древо элементов
my_tree.write('test.xml')