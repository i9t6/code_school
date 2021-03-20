def fun():
    yield 1
    yield 2
    yield 3
    return () <<<<< regresar un generador
    Vs
    retunt [] <<<<< regresar una lista 

a= fun()
next(a)
next(a,"valor default, se acabo")

def gen_list(n):
    for i in range(n):
        yield i 

mi_lista [1,3,6,9]
list_ = []

list_gen

generador
