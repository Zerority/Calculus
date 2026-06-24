import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

x = sp.sympify("x")
def integration_calculated():
    try:
        function_input = input("Enter your function :")
        function_call = sp.sympify(function_input)
        a = float(input("Enter your lower limit (a):"))
        b = float(input("Enter your upper limit (b):"))
        result = sp.integrate(function_call, (x,a,b))
        print(f"Integration of your function from {a} to {b} is : {result}")
        f_integrated = sp.lambdify(x, function_call, "numpy")
        x_plot = np.linspace(a ,b ,400)
        y_plot = f_integrated(x_plot)
        if isinstance(y_plot, (int, float, complex, sp.Number)):
            y_plot = np.full_like(x_plot, float(y_plot))
        fig, ax = plt.subplots()
        ax.plot(x_plot,y_plot, color = "blue", label = "f(x)")
        ax.fill_between(x_plot,y_plot,  color = "skyblue", label = "L'aires")
        plt.title("Integration plot")
        ax.legend()
        ax.grid(True)
        plt.show()

    except Exception as e:
        print("Enter your funcction again")

integration_calculated()