import matplotlib.pyplot as plt
import sympy as sp
import numpy as np
x = sp.Symbol("x")
def differentiation_calcul():
    function_input = input("Nhập hàm số f(x) : ")
    function_call = sp.sympify(function_input)
    x0 = float(input("Nhập vào đây hoành độ tiếp điểm :"))
    result = sp.diff(function_call, x)
    print(f"Đạo hàm của {function_call} là : {result}")
    k = result.subs(x, sp.sympify(x0))
    y0 = float(function_call.subs(x, x0))
    phuong_trinh_tiep_tuyen = k*(x-x0) + y0
    f_numpy = sp.lambdify(x, function_call,"numpy")
    f_sympy = sp.lambdify(x, phuong_trinh_tiep_tuyen, "numpy")
    trucx = np.linspace(x0 - 2, x0 + 2, 400)
    trucy = f_numpy(trucx)
    if isinstance(trucy, (int, float, complex, sp.Number)):
        trucy = np.full_like(trucx, float(trucy))
    trucyreal = f_sympy(trucx)
    if isinstance(trucyreal, (int, float, complex, sp.Number)):
        trucyreal = np.full_like(trucx, float(trucyreal))
    fig, ax = plt.subplots()
    ax.plot(x0,y0, color ="red", marker = "o", markersize = "8")
    ax.plot(trucx, trucy, color = "blue", label = "f(x)")
    ax.plot(trucx, trucyreal, color = "red", label = "La tangence")
    ax.legend()
    ax.grid(True)
    plt.show()

differentiation_calcul()
