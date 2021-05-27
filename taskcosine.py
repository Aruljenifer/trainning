from cosinesim import cosine_distance_countvectorizer_method
import json
b=input("enter title")

f= open('/home/jenifer/Documents/marlin (1)/small_number/absolute.txt')
data = json.load(f)


for i in data['hits']:
    p=(i['doc']['title'])
    x=json.dumps(p)
    print(x,cosine_distance_countvectorizer_method(b,x),"%")