def greet():
    """

    :return:
    """

    print("hello!")
    return 0
greet()
x=greet()
print(x)

def greet_improved(name):
    """

    :param name: the name od the person to greet
    :return:  None
    """
    print("hello",name)
greet_improved("john")
greet_improved("jane")

def custom_op(x=0, y=0):
    """
    custom op: 10x+y
    :param x: the first number
    :param y: the second number
    :return: number,10x+y
    """
    result=10*x +y
    return result
print(custom_op(5, 8))
x=custom_op(5,9)
print(f"the result of custom_op is :{x}")
x=custom_op(y=9, x=5)
print(f"the result of custom_op is : {x}")
print(custom_op(5))
print(custom_op())
print(custom_op(y=5))

def bond_intro(name):
    print("the name is.", name)
def bond_name(first,last):
    return f"{last}, {first}, {last}"
print(bond_name("Ismail", "Chorfi"))
bond_intro(bond_name("ismail", "chorfi"))
bond_intro(bond_name("james", "bond"))
