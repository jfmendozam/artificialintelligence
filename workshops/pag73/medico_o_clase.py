from logic import *

enfermo = Symbol("enfermo")
medico = Symbol("medico")
clase = Symbol("clase")

kb = And(
    Implication(Not(enfermo), clase),
    Or(clase, medico),
    Not(And(clase, medico)),
    medico
)

print(kb.formula())
print(model_check(kb, enfermo))
