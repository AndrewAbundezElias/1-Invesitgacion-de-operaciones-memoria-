import pulp

# 1. Definir el problema (Maximización)
model = pulp.LpProblem("Optimizacion_Cluster", pulp.LpMaximize)

# 2. Variables de decisión
x1 = pulp.LpVariable("Backend", lowBound=0, cat='Integer')
x2 = pulp.LpVariable("DataWorker", lowBound=0, cat='Integer')

# 3. Función objetivo
model += 300 * x1 + 250 * x2, "Rendimiento_Total"

# 4. Restricciones

# RAM (GB)
model += 2 * x1 + x2 <= 16, "RAM"

# Almacenamiento SSD (GB)
model += 1000 * x1 + 2000 * x2 <= 17000, "SSD"

# Límite de Backend
model += x1 <= 6, "Limite_Backend"

# Licenciamiento Data Workers
model += x2 <= 7, "Limite_DataWorker"

# 5. Resolver
model.solve()

# 6. Mostrar resultados
print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"Backend (x1): {x.varValue}")
print(f"Data Worker (x2): {x2.varValue}")
print(f"Rendimiento Máximo: ${pulp.value(model.objective)} USD/hora")