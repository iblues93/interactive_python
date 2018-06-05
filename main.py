# utilities
import itertools

def main():
    user_globals = {}
    for i, user_input in get_user_input():
        # process user input
        execute_user_input(i,user_input,user_globals)

def exec_function(user_input):
    # higher level wrapper to determine if user input is statement or expression
    # returns the executable function
    # Try to compile the user input
    # if executable use exec()
    # if expression use eval()

    try:
        compile(user_input,'<stdin>','eval')
    except SyntaxError:
        return exec
    return eval

def execute_user_input(i,user_input,user_globals):
    # get the function to be executed with the parameters user_input and user_globals
    res = exec_function(user_input)(user_input,user_globals)
    if res != None:
        print(res)

def get_user_input():
     for i in itertools.count():
        try:
            yield i, input('In[{}]: '.format(i))
        # except KeyboardInterrupt:
        #     pass
        except EOFError:
            break


if __name__ == "__main__":
    main()