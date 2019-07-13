import os
import inspect
from pprint import pprint as pp
import err


def entrypoint_function():     
    func_db = get_function_database()    
    while True:                
        clear_stout()
        print_options(func_db)  
        #pp(func_db)
        try:            
            user_input = input('\nChoose a function id ::> ')
            if user_input.lower() == 'q':
                print("quitting now...")
                return            
            inx = int(user_input) - 1
            func_db[inx].get('pyfunc')() 

        except IndexError as e:          
            if not handled(e):
                return

        except Exception as e:
            if not handled(e):
                return

def handled(err):
    is_handled = False
    error_type=type(err).__name__            
    print(f"\n***{error_type} {err}\n")     

    user_input = input("Press any key to continue or (q)uit: ")
    if user_input.lower() == 'q':        
        is_handled = False
    else:
        is_handled = True
    return is_handled

def clear_stout():
    os.system('cls' if os.name == 'nt' else "printf '\033c'")

def get_function_database():            
    # setup
    database = []    

    all_error_funcs = inspect.getmembers(err, inspect.isfunction)     
    for func_name, pyfunc in all_bad_funcs:
        idx = len(database) + 1
        payload ={'id':idx, 'func_name':func_name,'pyfunc':pyfunc}
        database.append(payload)        
    return database

def print_options(database):   
    print("*"*40)
    print("   make a selection or press (q)uit  ")
    print("*"*40)
    # pp(database)
    [print(f"{row.get('id')} - {row.get('func_name')}") for row in database]        
    print("*"*40)


if __name__ == "__main__":
    entrypoint_function()