products=[
    {"p_name":"complan","mrp":230,"avl_qty":50},
    {"p_name": "horlicks", "mrp": 250, "avl_qty": 10},
    {"p_name": "bournvita", "mrp": 220, "avl_qty": 0},
    {"p_name": "nutricharge", "mrp": 200, "avl_qty": 100},
    {"p_name": "mylo", "mrp": 100, "avl_qty": 0},

]

# display all product names
product_name=list(map(lambda prod:prod["p_name"],products))
print(product_name)

# print available products
available=list(filter(lambda item:item["avl_qty"]>0,products))
print(available)

# display out of stock products
available=list(filter(lambda item:item["avl_qty"]==0,products))
print(available)