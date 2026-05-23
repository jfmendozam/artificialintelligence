'''
Gente              Sitios              Objeto
estudiante José    CRAI                Celular
profesora María    Salón               Ratón
enfermera Angie    Cafetería           Tablet

Jose V Maria V Angie
crai V salon V cafeteria
celular V raton V tablet

no jose V no cafeteria V no raton
'''

import termcolor
from logic import *

jose = Symbol("estJose")
maria = Symbol("profMaria")
angie = Symbol("enfAngie")
personas = [jose, maria, angie]

crai = Symbol("CRAI")
salon = Symbol("salon")
cafeteria = Symbol("cafeteria")
sitios = [crai, salon, cafeteria]

celular = Symbol("celular")
raton = Symbol("raton")
tablet = Symbol("tablet")
objetos = [celular, raton, tablet]

simbolos = personas + sitios + objetos

def check_knowledge(knowledge):
    for symbol in simbolos:
        if model_check(knowledge, symbol):
            termcolor.cprint(f"{symbol}: SI", "green")
        elif not model_check(knowledge, Not(symbol)):
            print(f"{symbol}: QUIZAS")

kb = And(
    Or(jose, maria, angie),
    Or(crai, salon, cafeteria),
    Or(celular, raton, tablet)
)

#kb.add(Not(jose))
#kb.add(Not(cafeteria))
#kb.add(Not(raton))

kb.add(Implication(Not(jose), And(salon, celular)))
kb.add(And(celular, Not(angie)))
kb.add(And(maria, celular))
kb.add(Biconditional(maria, salon))

print(kb.formula())
check_knowledge(kb)
