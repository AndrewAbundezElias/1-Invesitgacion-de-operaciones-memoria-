import pulp

# 1. Definir el problema (Maximización)
model = pulp.LpProblem("Edge_Computing", pulp.LpMaximize)

# 2. Variables de decisión (enteras)
x1 = pulp.LpVariable("Servidor_Blade_Estandar", lowBound=0, cat='Integer')
x2 = pulp.LpVariable("Servidor_Rack_Pro", lowBound=2, cat='Integer')  # mínimo 2 por SLA

# 3. Función Objetivo
# Maximizar la capacidad de procesamiento (EPS)
model += 10000 * x1 + 25000 * x2, "EPS_Total"

# 4. Restricciones

# Presupuesto máximo ($30,000)
model += 1500 * x1 + 4000 * x2 <= 30000, "Presupuesto"

# Espacio en rack (24 bahías)
model += x1 + 3 * x2 <= 24, "Espacio_Rack"

# Energía disponible (45 kW)
model += 2 * x1 + 5 * x2 <= 45, "Energia"

# 5. Resolver
model.solve()

# 6. Mostrar resultados
print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"Servidores Blade Estándar: {x1.varValue}")
print(f"Servidores Rack Pro: {x2.varValue}")
print(f"EPS Total: {pulp.value(model.objective):,.0f}")
