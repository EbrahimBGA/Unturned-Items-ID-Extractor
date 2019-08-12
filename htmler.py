import os, datetime
import scr_itemz as itz


itz.main()
itemList = itz.itemsList
gen_time = datetime.datetime.now()

note = '''<h3>Unturned items ID</h3>
<h3>game version: %s</h3>
<h5>last database update: %s</h5>
'''%("3.26.4.0 - Oct 27", datetime.datetime.now())

h_style = '''
<style>
table.GeneratedTable {
  width: 100%;
  background-color: #ffffff;
  border-collapse: collapse;
  border-width: 2px;
  border-color: #2e5c5c;
  border-style: solid;
  color: #000000;
}

table.GeneratedTable td, table.GeneratedTable th {
  border-width: 2px;
  border-color: #2e5c5c;
  border-style: solid;
  padding: 3px;
}

table.GeneratedTable thead {
  background-color: #55aaaa;
}
</style>'''

##html ##todo: change out path
outhtml_item = "C:/Users/~~~~/Desktop/U/items.html"
open(outhtml_item,"w+").close()
def pmain():
    file = open(outhtml_item,"w")
    h_head = '''<head><title>Unturned Item IDs</title>'''+h_style+'''</head>'''
    h_body = '''<body>'''+note
    file.write(h_head+h_body)

    h_thead = '''<table class="GeneratedTable"><thead><tr><th>Name</th><th>ID</th><th>Type</th></tr></thead><tbody>'''
    file.write(h_thead)
    for x in itemList:
        idic={}
        idic=x
        c = '''<tr><td>%s</td><td>%s</td> <td>%s</td></tr>''' % (str(idic["Name"]), str(idic["ID"]),str(idic["Type"]))
        q = c.replace("\n","")
        file.write(q)
    file.write('''</tbody></table>''')

    file.write('''</body>''')
    file.close()

pmain()
