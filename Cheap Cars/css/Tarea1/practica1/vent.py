'''
Caja Registradora
'''
print("Grocery")
print("blvd.740,c.dorado,#0699")
print("6645563892")

print("cantidad de productos: ")
prods=int(input())
i=0
sub=0

while i<prods:
    print("precio del producto" ,i+1, )
    val= int(input())
    print("cantidad del producto: ")
    cant= int(input())
    subpro=val*cant
    sub=sub+subpro
    i+=1
iva= sub * 0.15 
total=sub + iva 
print("se vendieron: ",prods,"productos")
print("subtotal: ",sub)
print("iva 15%: " ,iva) 
print("Total: " ,total) 

