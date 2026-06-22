import pulp

# 1. Definir el problema (Maximización)
model = pulp.LpProblem("VideoGame_Assets", pulp.LpMaximize)

# 2. Variables de decisión (enteras)
x1 = pulp.LpVariable("Servidor Basico", lowBound=0, cat='Integer')
x2 = pulp.LpVariable("Servidor Avanzado", lowBound=0, cat='Integer')

# 3. Función Objetivo
model += 30 * x1 + 50 * x2, "Valor_Total"

# 4. Restricciones

# Servidores Basicos
model += x1 + 3 * x2 <= 16, "Servidor Basico"

# Servidores Avanzados
model += 2 * x1 + 2 * x2 <= 24, "Servidor Avanzado"

# 5. Resolver
model.solve()

# 6. Mostrar resultados
print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"Servidores Basicos: {x1.varValue}")
print(f"Servidores Avanzados: {x2.varValue}")
print(f"Valor Total: ${pulp.value(model.objective)}")