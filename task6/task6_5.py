# Write an example on decorators.
#defining decorator function
def smart_greet(func):
    #defining the wrapper function
    def wrapper():
        print("before decorating")
        func()                          #func() has greet()
        print("after decorating")
    return wrapper


#funtion to be enhanced
@smart_greet                #using @<decorator func name> will enhance the present func
def greet():
    print("welcome this is python programming")
    print("function to be enhanced")


#strategy 1
# result_greet=smart_greet(greet)         #greet() sent as a parameter to func;result_greet holds wrapper()
# result_greet()                      #as good as calling wrapper()

#output
# before decorating
# welcome this is python programming
# function to be enhanced
# after decorating

#strategy 2..using @

greet()                 #when @ is used it is enough to call the present function only

#output
# before decorating
# welcome this is python programming
# function to be enhanced
# after decorating
#
# Process finished with exit code 0

