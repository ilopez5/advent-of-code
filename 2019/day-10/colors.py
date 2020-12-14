GREEN = '\033[38;5;34m'
RED = '\033[38;5;160m'
WHITE = '\033[m'
YELLOW = '\033[38;5;226m'
BLUE = '\033[38;5;39m'

def r(mystring):
    return RED+mystring+WHITE      

def g(mystring):
    return GREEN+mystring+WHITE

def b(mystring):
    return BLUE+mystring+WHITE

def y(mystring):
    return YELLOW+mystring+WHITE

def succ():
    return g("Success")

def fail():
    return r("Failure")