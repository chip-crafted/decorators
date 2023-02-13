def outside():
    print('after function call')

def inside():
    print('before function call')

def do_things():
    print('🛠️doing work 🛠️')
    

def wrapper(func):
    inside()
    func()
    outside()

wrapper(do_things)

