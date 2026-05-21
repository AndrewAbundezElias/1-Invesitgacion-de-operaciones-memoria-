from pulp import *

problema = LpProblem("Firewall_Seguridad", LpMaximize)

x = LpVariable("Inspeccion_Basica", lowBound=0)
y = LpVariable("Inspeccion_Profunda", lowBound=0)

problema += 2*x + 5*y, "Puntos_de_Seguridad"

problema += x + 3*y <= 18, "CPU"
problema += x + y <= 8, "RAM"

problema.solve()


print("Estado:", LpStatus[problema.status])

print("GB en inspección básica =", value(x))
print("GB en inspección profunda =", value(y))

print("Seguridad total =", value(problema.objective))