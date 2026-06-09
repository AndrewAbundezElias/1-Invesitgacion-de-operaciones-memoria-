import pulp

# 1. Definir el problema (Minimización)
model = pulp.LpProblem("Cloud_Optimization", pulp.LpMinimize)

# 2. Variables de decisión
x1 = pulp.LpVariable("Almacenamiento Estandar", lowBound=0, cat='Integer')
x2 = pulp.LpVariable("Almacenamiento Premium ", lowBound=0, cat='Integer')

# 3. Función Objetivo
# Minimizar costo mensual
model += 20 * x1 + 60 * x2, "Costo_Total"

# 4. Restricciones

# IOPS (velocidad mínima requerida)
model += x1 + 3 * x2 >= 15, "IOPS"

# Retención mínima de datos
model += 2 * x1 + 2 * x2 >= 14, "Disponibilidad"

# 5. Resolver
model.solve()

# 6. Mostrar resultados
print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"Almacenamiento Estándar: {x1.varValue}")
print(f"Almacenamiento Premium: {x2.varValue}")
print(f"Costo Total Mensual: ${pulp.value(model.objective)}")
