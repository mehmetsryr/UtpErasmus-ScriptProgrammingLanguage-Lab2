print("Welcome in Mehmet's store")
product_name = input("Write product name:")

while True:
    try:
        product_price_net = int(input("Write product price net:"))
        break
    except:
        print("Your data type Wrong")
client_email = input("Write client email: ")
client_phone = input("Write client phone:")

groos_p = product_price_net + (product_price_net*23/100)
print("name: ", product_name)

print("net price: ", product_price_net)

print("gross price: ", groos_p)

print("email: ", client_email)
print("phone: ", client_phone)