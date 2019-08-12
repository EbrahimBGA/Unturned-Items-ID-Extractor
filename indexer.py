import os, json
outjson_item = "C:/Users/~~~~/Desktop/U/items.json"
open(outjson_item,"w+").close()

import scr_itemz as itz

itemList = {}

def pmain():
    itz.main()
    itemList = itz.itemsList
    file = open(outjson_item,"a")
    c = json.dumps(itemList, indent=4)
    file.write(c)
    file.close()


pmain()