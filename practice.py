# Ex 2.3-practicing casing in strings
name = "eric"
print("Hello " + name.title() + ", would you like to learn some Python today?")
print(f"Hello {name.title()}, would you like to learn some Python today?")

# EX 2.4-casing in strings
name = "eric nam"
print(f"\n{name.lower()}")
print(name.upper())
print(name.title())

# ex 2.5 - f-strings
quote = "Rejection is redirection to God's chosen destination for you"
author = "PFlo"
print(f"\n{author} once said, \"{quote}\"")

# ex 2.6 - f-strings and variables
famous_person = "PFlo"
message = f"\n{famous_person} once said, \"{quote}\""
print(message)

# ex 2.7 - adding/removing whitespace
new_name = " eric nam "
print("\teric nam")
print("\neric nam")
print(new_name)
print(new_name.lstrip())
print(new_name.rstrip())
print(new_name.strip())
