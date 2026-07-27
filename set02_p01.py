# Swiggy Order Bill
def place_order(customer,*items, **charges) :
    print("Customer :", customer)

    print(f"Items ordered ({len(items)}):")
    for i, item in enumerate(items,1): # enumerate iterates both i value and items at once 
        print(f"   {i}. {item}")
    print("Charges:")
    for key, value in charges.items():# here items() gives the both key and value
        print(f"   {key:10} : {value}")
place_order("Ravi", "Biryani","Coke", "Gulab Jamun",delivery = 40 , gst = 25, discount = 50)
    


