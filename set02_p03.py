#Url Query Builder
def build_query(**filters): #**filters can take key value pairs without limit
    query = []

    for key, value in filters.items():
        query.append(f"{key}={value}") #adding keyvalue pairs in a list

    return "&".join(query)#here joins the all keyvalue pairs without space
print(build_query(city = 'Hyderabad',rating=4, veg=True))
print(build_query())