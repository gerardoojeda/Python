from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page
#CONSIDER A HTML FILE:
html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"
soup=BeautifulSoup(html,features="html.parser")
print(soup.prettify())#prettify() to display the HTML in the nested structure:
#----------------------
#TAGS
tag_object=soup.title
print("tag object:",tag_object)
print("tag object type:",type(tag_object))#WE CAN SEE THE TYPE of object
#h one Tag with the same name, the first element with that Tag name is called
#for example
tag_object=soup.h3
print("tag of player at h3: ",tag_object)#this is the first one h3 that apears
#------------------------------------
#Children, Parents, and Siblings
tag_child=tag_object.b
print(tag_child)#as you can see b is the child qutations in html
parent_tag=tag_child.parent#parent would be go back to h3
print(parent_tag)
#check the parent for the tag_object and you will see its body
print(tag_object.parent)
#sibling would be the paragraph agrument p
sibling_1=tag_object.next_sibling
print(sibling_1)
#the sibling for sbling 1 would be the next so steve curry
sibling_2=sibling_1.next_sibling
print(sibling_2)
#---------------------------------------------------
#HTML ATRIBUTTES
#If the tag has attributes, the tag id="boldest" has an attribute id whose value is boldes
print(tag_child['id'])
#You can access that dictionary directly as attrs
print(tag_child.attrs)
#We can also obtain the content if the attribute of the tag using the Python get() method.
print(tag_child.get('id'))
#---------------------------------------------
#NAVIGABLE STRINGS
#A string corresponds to a bit of text or content within a ta
tag_string=tag_child.string
tag_string
type(tag_string)
unicode_string = str(tag_string)
unicode_string
#---------------------------------------------------------------
#FILTERING
table="<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"
table_bs = BeautifulSoup(table,features="html.parser")
#The find_all() method looks through a tag’s descendants and retrieves all descendants that match your filters.
#The Method signature for find_all(name, attrs, recursive, string, limit, **kwargs)
table_rows=table_bs.find_all('tr')
print(table_rows)
#The result is a Python Iterable just like a list, each element is a tag object:
first_row =table_rows[0]
print(first_row)
print(type(first_row))
#we can obtain the child
print(first_row.td)
#we can iterate from the list
for i,row in enumerate(table_rows):
    print("row",i,"is",row)


