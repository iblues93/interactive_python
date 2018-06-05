# utilities
import itertools

def main():
    user_globals = {}
    save_user_globals(user_globals)
    for i, user_input in get_user_input():
        # process user input
        user_globals = execute_user_input(i,user_input,user_globals)
        save_user_globals(user_globals)

def save_user_globals(user_globals,path="user_globals.txt"):

    with open(path,"w") as f:
        f.write("Name    Value    Type\n")
        for key,val,val_type in only_user_variables(user_globals):
            f.write("{} : {} ({})\n".format(key,val,val_type))

def only_user_variables(user_globals):

    for key,val in user_globals.items():
        # Remove dunder items which are built-in variables
        # Remove Imports
        if (not key.startswith("__") or not key.endswith("__")) and val.__class__.__name__ != "module":
            yield (key,val,val.__class__.__name__)

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
    # Since user_globals is going to get updated, copy it as a local variable, then return it. [Referential Transparency]
    user_globals = user_globals.copy()
    try:
        res = exec_function(user_input)(user_input,user_globals)
    except Exception as e:
        print("{}: {}".format(e.__class__.__name__,e))
    else:
        if res != None:
            print("Out[{}]: {}".format(i,res))
    return user_globals

def get_user_input():
     for i in itertools.count():
        try:
            yield i, input('In[{}]: '.format(i))
        except KeyboardInterrupt:
            pass
        except EOFError:
            break


if __name__ == "__main__":
    main()