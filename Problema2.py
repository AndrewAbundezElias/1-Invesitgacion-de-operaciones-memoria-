import pulp

model = pulp.LpProblem("Maximizacion_Produccion_PC", pulp.LpMaximize)


x = pulp.LpVariable("Escritorios", lowBound=0, cat='Integer')
y = pulp.LpVariable("Laptops", lowBound=0, cat='Integer')


model += 2000 * x + 4000 * y, "Ganancia_Total"


model += 1 * x + 1 * y <= 60, "Limite_Procesadores"
model += 1 * x + 3 * y <= 100, "Limite_Horas_Trabajo"


status = model.solve(pulp.PULP_CBC_CMD(msg=False))


print("=" * 40)
print("      RESULTADOS DE LA OPTIMIZACIÓN      ")
print("=" * 40)

if pulp.LpStatus[status] == "Optimal":
    print(f"Estado de la solución: Exitosa ({pulp.LpStatus[status]})")
    print(f"Cantidad de Computadoras de Escritorio (x): {int(x.varValue)}")
    print(f"Cantidad de Laptops (y): {int(y.varValue)}")
    print("-" * 40)
    print(f"GANANCIA MÁXIMA TOTAL: ${pulp.value(model.objective):,.2f}")
else:
    print("No se pudo encontrar una solución óptima.")

print("=" * 40)