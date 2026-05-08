# Generated Workflow Code
import sys

# Global state
a = None
b = None
estado = 'OK'

def inicio():
    global a, b, estado
    a = 1
    b = 0
    if ((a == 1) and (b == 0)):
        print("AND funciona")
    fin()
    return

def fin():
    global a, b, estado
    print("Fin")

if __name__ == '__main__':
    inicio()