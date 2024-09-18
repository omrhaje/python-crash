# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

def func1():
    print(x)                               # Functions can't see into other functions

def func2():
    xc = 12                         # <-- enclosed
    print(x)

x = 12121221            # <-- global function

func1()
func2()