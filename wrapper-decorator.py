def wrapper(func):
    def outside():
        print('after function call')

    def inside():
        print('before function call')

    def decorator(text):
        inside()
        func(text)
        outside()
    
    return decorator


@wrapper
def do_more_things(text):
    print(text)


do_more_things("🛠️doing work 🛠️")