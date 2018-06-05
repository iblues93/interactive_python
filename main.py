# utilities
import itertools

def main():

    for i, user_input in get_user_input():
        print(i,user_input)

def get_user_input():
    
    for i in itertools.count():
        yield i, input('In[{}]: '.format(i))

if __name__ == "__main__":
    main()