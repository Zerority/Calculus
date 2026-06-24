import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
x = sp.Symbol("x")
def limit_calculation(): 
    try:
        function_input = input("Saisissez votre fonction (ex: 1/x, x**2): ")
        function_call = sp.sympify(function_input)
        limit_input = input("Point (ex: 0, oo): ")
        limit = sp.sympify(limit_input)
        limit_result = sp.limit(function_call, x, limit)
        print(f"Limit = {limit_result}")
    except Exception as e:
        print("Saisissez à nouveau votre fonction (Erreur de syntaxe)")
        return
    try:
        value = function_call.subs(x, limit)
        if value.is_real:
            print(f"La valeur de la fonction = {value}")
        else:
            print("Cette fonction non définie à ce stade (la valeur n'est pas réelle)")
        if limit.is_real and limit_result.is_real:
            limit_float = float(limit)
            y_point = float(limit_result)
            fig, ax = plt.subplots()
            f_numpy = sp.lambdify(x, function_call, "numpy")
            x_label = np.linspace(limit_float - 2, limit_float + 2, 400)
            with np.errstate(divide="ignore", invalid="ignore"):
                y_label = f_numpy(x_label)
                if isinstance(y_label, (int, float, complex, sp.Number)):
                    y_label = np.full_like(x_label, float(y_label))
            ax.plot(x_label, y_label, color="blue", label="f(x)")
            ax.plot(limit_float, y_point, marker="o", markersize=8, color="red", label="Limite")
            ax.axvline(x=limit_float, linestyle="--", color="red", alpha=0.5)
            ax.grid(True)
            ax.legend()
            plt.title("Graphique de la fonction et sa limite")
            plt.show()
        else:
            print("Impossible de tracer le graphique ")
            
    except Exception as e:
        print(f"Erreur lors du calcul de la valeur ")

limit_calculation()