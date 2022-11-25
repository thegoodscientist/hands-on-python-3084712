greet = "Hello World"
extended_greet = "Hello World, " + "this is a long string"

name = "John"

interpolation = f"Hello {name}"

greet_format = "Hello {}"

formatted = greet_format.format(name)

print(interpolation, formatted)

print(formatted.upper())
print(formatted.lower())
print(formatted.replace("John", "Paul"))
