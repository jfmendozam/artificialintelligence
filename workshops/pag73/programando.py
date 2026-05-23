'''
Si está conectado el equipo vas a programar
No pueda estar programando y durmiendo
conectado
'''
from logic import *

P = Symbol("PCestaConectado")
Q = Symbol("SantiagoEstaProgramando")
R = Symbol("SantiagoEstaDurmiendo")

kb = And(
    Implication(P, Q),
    Not(And(Q, R)),
    P
)

print(kb.formula())
print(model_check(kb, R))
