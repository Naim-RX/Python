# Define a decorator function
def greet(fx):

    # Wrapper function that can accept any number of arguments
    def mfx(*args, **kwargs):

        # Code to execute before the original function
        print("Good Morning")

        # Call the original function with its arguments
        fx(*args, **kwargs)

        # Code to execute after the original function
        print("Thanks for using this function")

    # Return the wrapper function
    return mfx


# Apply the greet decorator to the hello() function
@greet
def hello():
    print("Hello World")

hello()

# Apply the greet decorator to the add() function
@greet
def add(a, b):
    print(a + b)

add(2, 3)