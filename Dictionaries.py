# Dictionaries - to store a bunch of key value pairs
# Name: John Cena
# Email: youcantseeme@yahoo.com
# Phone: 0123456789

# Defining Dictionaries
customer = {
    "name": "John Cena",
    "age": 50,
    "is_Verified": True
}
# Each variable in a Dictionary is called a Key and each key must be Unique

print(customer)

# To access each key, we need to use [] brackets
# Also it is Case Sensitive, so need to pay attention while calling a Key
print(customer["name"])

# To avoid the case sensitive error, we can use the 'get' method which return a 'None' value if a key is not found in the Dictionary
print(customer.get("gender"))
print(customer.get("age"))

# If there isn't a key available, then we can create and assign value to it directly using get method
print(customer.get("gender", 'Male'))
