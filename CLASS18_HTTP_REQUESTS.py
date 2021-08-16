import requests
import os
from PIL import Image
from IPython.display import IFrame
url='https://www.aeriak.com/'
r=requests.get(url)

#check the status
print(r.status_code)
print(r.request.headers)
print("request body:", r.request.body)
header=r.headers
print(r.headers)
print(header['date'])
print(header['Content-Type'])
print( r.encoding)
print(r.text[0:100])
#---------------------------------------------------------------------------------
#another type of data
# Use single quotation marks for defining string
url='https://gitlab.com/ibm/skills-network/courses/placeholder101/-/raw/master/labs/module%201/images/IDSNlogo.png'
r=requests.get(url)
print(r.headers)
print(r.headers['Content-Type'])
path=os.path.join(os.getcwd(),'image.png')
path
with open(path,'wb') as f:
    f.write(r.content)
Image.open(path)
#-----------------------------------------------------------------------------------
#another excersie
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'
path=os.path.join(os.getcwd(),'example10.txt')#will save the data ina txt file
r=requests.get(url)
with open(path,'wb') as f:
    f.write(r.content)
#-----------------------------------------------------------------------------------
#Get Request with URL Parameters
url_get='http://httpbin.org/get'
#To create a Query string, add a dictionary. The keys are the parameter names and the values are the value of the Query string.
payload={"name":"Joseph","ID":"123"}
#we then pass the dictonary and call the url
r=requests.get(url_get,params=payload)
print(r.url)
#we also see there is no body
print("request body:", r.request.body)
print(r.status_code)
print(r.headers['Content-Type'])
#As the content 'Content-Type' is in the JSON format we can use the method json(), it returns a Python dict:
print(r.json())
#The key args has the name and values:
print(r.json()['args'])
#---------------------------------------------------------------------------------------
#POST REQUESTS
url_post='http://httpbin.org/post'
r_post=requests.post(url_post,data=payload)
#lest compare the post and get
print("POST request URL:",r_post.url )
print("GET request URL:",r.url)
#We can compare the POST and GET request body, we see only the POST request has a body:
print("POST request body:",r_post.request.body)
print("GET request body:",r.request.body)
print(r_post.json()['form'])