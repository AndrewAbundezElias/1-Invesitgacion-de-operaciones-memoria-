from scipy.optimize import linprog

# 1. Coeficientes de la función objetivo
# Como scipy por defecto MINIMIZA, multiplicamos por -1 para MAXIMIZAR la ganancia
# Ganancia: $2000 por escritorio (x) y $4000 por laptop (y)
c = [-2000, -4000]

# 2. Matriz de restricciones (Lado izquierdo de las inecuaciones)
# Fila 1 (Procesadores): 1x + 1y <= 60
# Fila 2 (Horas de trabajo): 1x + 3y <= 100
A = [
    [1, 1],  # Coeficientes de la restricción de procesadores
    [1, 3]   # Coeficientes de la restricción de horas
]

# 3. Vector de restricciones (Lado derecho de las inecuaciones)
b = [60, 100]

# 4. Límites de las variables (No negatividad: x >= 0, y >= 0)
x_bounds = (0, None)
y_bounds = (0, None)

# 5. Resolver el problema utilizando el método Simplex (o el de la librería por defecto)
res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

# --- Mostrar los resultados en pantalla ---
print("=" * 40)
print("      RESULTADOS DE LA OPTIMIZACIÓN      ")
print("=" * 40)

if res.success:
    # Multiplicamos por -1 para recuperar el valor real de la ganancia máxima
    ganancia_maxima = -res.fun
    computadoras_escritorio = round(res.x[0])
    laptops = round(res.x[1])
    
    print(f"Estado de la solución: Exitosa")
    print(f"Cantidad de Computadoras de Escritorio (x): {computadoras_escritorio}")
    print(f"Cantidad de Laptops (y): {laptops}")
    print("-" * 40)
    print(f"GANANCIA MÁXIMA TOTAL: ${ganancia_maxima:,.2f}")
else:
    print("No se pudo encontrar una solución óptima.")

print("=" * 40)