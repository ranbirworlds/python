product=["Rice","Soap","Shampoo"]
cateogory=[{"Basmati":50,"Minikit":40,"Gobindvog":60},{"Lifebuoy":20,"Dettol":30,"Dove":50},{"Loreal": 65, "Pantene": 60, "Head & Soulder": 75}]
cart=[]
price=[]
quant=[]

print('''     Welcome to Grihini Stores 
           Shopping List   
1. Product list
2. View Cateogory
3. Add to Cart
4. No. of items in the cart
5. Buy
6. Exit     ''')



while(True):
  choose=input("Enter yes to add items into cart or enter no to exit")

  if choose=="y":
    print("Products are :")
    for i in product:
      print(i)
    product_name=input("Enter the product name:")
    indexing=product.index(product_name)
    for i,j in cateogory[indexing].items():
      print(i,":",j)
    Add_cart=input("Enter the cateogory name:")
    Quantity=int(input("Quantity:"))
    cart.append(Add_cart)
    price.append(cateogory[indexing] [Add_cart]*Quantity)
  if choose == "x":
    break
print(cart,price)


