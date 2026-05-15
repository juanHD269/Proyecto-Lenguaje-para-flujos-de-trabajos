# Generated Workflow Code
import sys

# Global state
val = None
estado = 'OK'

def inicio():
    global val, estado
    val = input('Ingrese valor para val: ')
    try: val = int(val)
    except ValueError: pass
    if (val > 50):
        mayor()
        return
    if (val <= 50):
        menor()
        return

def mayor():
    global val, estado
    print("Es mayor")

def menor():
    global val, estado
    print("Es menor")

if __name__ == '__main__':
    inicio()