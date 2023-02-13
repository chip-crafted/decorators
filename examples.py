# Validate Data
""" def transform_input(func):
    def validate(text):
        if not text:
            raise ValueError


    def decorator(text):
        validate(text)
        return func(text)
    
    return decorator

@transform_input
def print_text(text):
    print(text)

print_text("Hello World!")
try:
    print_text("")
except ValueError:
    print("invalid text received") """


# Transform Data
""" def transform_input(func):
    def transform(text):
        return text * 2

    def decorator(text):
        new_text = transform(text)
        return func(new_text)
    
    return decorator

@transform_input
def print_text(text):
    print(text)

print_text("Hello World!") 
 """
# New object in next function
 
def add_count(func):
    def count(text):
        return len(text)

    def decorator(text):
        num_letters = count(text)
        return func(text, num_letters)
    
    return decorator

@add_count
def print_text(text, text_count):
    print(text)
    print("-- contains {} characters --".format(text_count))

print_text("Hello World!")