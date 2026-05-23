'''
Luis Díaz, Daniel Muñoz, Richard Rios y James Rodríguez son futbolistas colombianos destacados que pertenecen a uno de los siguientes equipos: Benfica, Bayern Munich, León y Crystal Palace. Luis Díaz pertenece a Benfica o Bayern Munich, Richard Rios no pertenece a León, Daniel Muñoz pertenece a Crystal.
'''

from logic import *

futbolistas = ["Lucho", "Daniel", "Richard", "James"]
equipos = ["Benfica", "Bayern", "Leon", "Crystal"]

simbolos = []

kb = And()

for futbolista in futbolistas:
    for equipo in equipos:
        simbolos.append(Symbol(f"{futbolista}{equipo}"))
        #print(f"{futbolista}.{equipo}")

# Cada futbolista pertenece a un equipo
for futbolista in futbolistas:
    kb.add(Or(
        Symbol(f"{futbolista}Benfica"),
        Symbol(f"{futbolista}Bayern"),
        Symbol(f"{futbolista}Leon"),
        Symbol(f"{futbolista}Crystal")
    ))

# Solo un equipo por futbolista
for futbolista in futbolistas:
    for e1 in equipos:
        for e2 in equipos:
            if e1 != e2:
                kb.add(
                    Implication(Symbol(f"{futbolista}{e1}"), Not(Symbol(f"{futbolista}{e2}")))
                )

# Solo un futbolista por equipo
for equipo in equipos:
    for f1 in futbolistas:
        for f2 in futbolistas:
            if f1 != f2:
                kb.add(
                    Implication(Symbol(f"{f1}{equipo}"), Not(Symbol(f"{f2}{equipo}")))
                )

kb.add(Or(Symbol("LuchoBenfica"), Symbol("LuchoBayern")))
kb.add(Not(Symbol("RichardLeon")))
kb.add(Symbol("DanielCrystal"))
kb.add(Not(Symbol("LuchoBenfica")))

#print(kb.formula())

for simbolo in simbolos:
    #print(simbolo)
    if model_check(kb, simbolo):
        print(simbolo)
