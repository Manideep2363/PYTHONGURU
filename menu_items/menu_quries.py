from pprint import pprint
import json
with open("/mnt/c/Users/HP/Downloads/menu_items.json", "r") as f:
    data=json.load(f)
    
# 1
# for i in data:
#    print(i.get("name"))

#2 . Find All Appetizers
# for i in data:
#     if i.get("name") == "Appetizers":
#             for j in i.get("menuItems",[]):
#                 print(j.get("name"))

#3.Calculate the Average Price of a Beverage
# non_alcoholic =[]
# for i in data:
#     if i.get("name") == "Beverages":
#         for j in i.get("subCategories",[]):
#             if j.get('name') == 'Non Alcoholic Beverages':
#                 for k in j.get('menuItems',[]):
#                     for cfg in k.get("customConfigs",[]):
#                         non_alcoholic.append(cfg.get("itemPrice",0))

# avg = sum(non_alcoholic)/len(non_alcoholic)

# pprint(avg)

#4
# sizes=[]
# for i in data:
#     for j in i.get("menuItems") or []:
#         if len(j.get("customConfigs",[]) or []) > 1:
#             sizes.append(j.get('name'))
#     for k in i.get("subCategories",[]) or []:
#         for l in k.get("menuItems",[]) or []:
#             if len(l.get("customConfigs",[]) or []) >1:
#                 sizes.append(l.get("name"))
# print("Items with multiple sizes options:")
# for n in set(sizes):
#     print(n)

#5
# wings = []
# for i in data:
#     for j in (i.get("menuItems") or []):
#         if j.get('name') == "Chicken Wings":
#             for cfg in j.get("customConfigs") or []:
#                 for m in cfg.get("mandatoryModifiers") or []:
#                     if m.get("name") == "Wing Flavor":
#                         for mo in m.get("modifiers") or []:
#                             wings.append(mo.get("name"))
# print("Available wing Flavors:")
# for f in wings:
#     pprint(f)

#6
# for i in data:
#     for j in i.get("menuItems") or []:
#         for cfg in j.get("customConfigs") or []:
#             if len(cfg.get("mandatoryModifiers") or [])>0:
#                 print(j.get("name"))
#                 break

#7
# sal=set()
# for i in data:
#     if i.get("name") == "Salads & Soups":
#         for j in i.get("menuItems") or []:
#             sal.add(j.get("name"))

#         for j in i.get("subCategories") or []:
#             for k in j.get("menuItems") or []:
#                 sal.add(k.get("name"))
# print(len(sal))

#8
# max_price = 0
# item = None
# for i in data:
#     for j in i.get("menuItems") or []:
#         for cfg in j.get("customConfigs") or []:
#             price=cfg.get("itemPrice",0)
#             if price > max_price:
#                 max_price = price
#                 item = j.get("name")

#     for j in i.get("subCategories") or []:
#         for k in j.get("menuItems") or []:
#             for cfg in j.get("customConfigs") or []:
#                 price=cfg.get("itemPrice",0)
#                 if price > max_price:
#                     max_price = price
#                     item = j.get("name")
# print(f'name:{item},price:{max_price}')

#9
# d={
#     "Cheap":set(),
#     "Moderate":set(),
#     "Expensive":set()
# }
# for i in data:
#     for j in i.get("menuItems") or []:
#         for cfg in j.get("customConfigs") or []:
#             price = cfg.get("itemPrice",0)
#             if price < 800:
#                 d["Cheap"].add(j.get("name"))
#             elif 800 <= price <= 1200:
#                 d["Moderate"].add(j.get("name"))
#             else:
#                 d["Expensive"].add(j.get("name"))
#     for k in (i.get("subCategories") or []):
#         for j in (k.get("menuItems") or []):
#             for cfg in (j.get("customConfigs") or []):
#                 price = cfg.get("itemPrice", 0)

#                 if price < 800:
#                     d["Cheap"].add(j.get("name"))
#                 elif 800 <= price <= 1200:
#                     d["Moderate"].add(j.get("name"))
#                 else:
#                     d["Expensive"].add(j.get("name"))
# for k in d:
#     d[k] =list(d[k])
# pprint(d)

#10
menu = {}

for items in data:
    category_name = items.get("name")

    # Initialize key if not present
    if category_name not in menu:
        menu[category_name] = []

    # Items directly under category
    for item_name in (items.get("menuItems") or []):
        menu[category_name].append(item_name.get("name"))

    # Items inside subcategories
    for sub in (items.get("subCategories") or []):
        for item_name in (sub.get("menuItems") or []):
            menu[category_name].append(item_name.get("name"))

print(menu) 
