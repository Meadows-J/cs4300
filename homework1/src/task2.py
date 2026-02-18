#Define one of each of the 4 types
varInt = 1
varFloat = 1.1
varStr = "test"
varBool1 = True
varBool2 = False

def multiplyIntFloat():
    return varInt * varFloat

def reverseString():
    return varStr[::-1]

def booleanAnd():
    return varBool1 & varBool2


def booleanOr():
    return varBool1 or varBool2

#Show how int and floats interact
varTest1 = varInt * varFloat
print (varInt, "*", varFloat)
print(type(varInt), "*", type(varFloat,), "=", multiplyIntFloat(), type(varTest1))

#Show a baisc string opperation
print(varStr, "reversed string = ", reverseString())

#Show basic Boolean logic
print("True and False = ", booleanAnd())
print("True or False = ", booleanOr())
