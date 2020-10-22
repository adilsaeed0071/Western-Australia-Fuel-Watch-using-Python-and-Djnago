import requests
import feedparser
import pprint
response = requests.get('https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS')



feed = feedparser.parse(response.content)
#pprint.pprint(feed, indent=4)

list1= feed['entries']
print(list1[0].keys())
pprint.pprint(list1[0]['price'])
pprint.pprint(list1[0]['trading-name'])
pprint.pprint(list1[0]['location'])
length=len(list1)
print(length)
fuelprice=[]
location=[]
fuellist = []
a=[]
fullist=[]
for i in range(5):
    a.append(i)
#print(a)

for x in range(0,5):
    fullist.append([])
    fullist.append(list1[x]['price'])

#pprint.pprint(list1[x]['price'])
 #  pprint.pprint(list1[x]['location'])


for i in range(0,length):
    fuellist.append([])
    fuellist[i].append(list1[i]['price'])
    fuellist[i].append(list1[i]['location'])
    fuellist[i].append(list1[i]['brand'])
    fuellist[i].append(list1[i]['summary'])
print(fuellist)
c=fuellist[1][2]
print(c)

f = open('table.html', 'w')
var = 124
"""
body = '''
    <h1>Heading.</h1>
    <p> {}.</p>
    <table>
     <thead>
        <tr>
            <th colspan="2">Fuel prices</th>
        </tr>
     </thead>
    <tbody>
        <tr>
            <td>The table body</td>
            <td>with two columns</td>
        </tr>
    </tbody>
     </table>
'''.format(fuellist)

line = 'Heading. Paragraph {}.'.format(fuellist)
f.write(body)
f.close()
"""



# building the auxiliary string list
items = ["\n    <li>{}</li>".format(s) for s in fuellist]
items = "".join(items)
# insert in the html

body = '''
    <h1>Heading.</h1>
    <p> {}.</p>
    <table>
     <thead>
        <tr>
            <th colspan="2">Fuel prices</th>
        </tr>
     </thead>
    <tbody>
        <tr>
            <td>The table body</td>
            <td>with two columns</td>
        </tr>
    </tbody>
     </table>
'''.format(items)

line = 'Heading. Paragraph {}.'.format(items)
f.write(body)
f.close()
