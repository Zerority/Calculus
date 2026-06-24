import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox

x = sp.Symbol("x")

def clear_previous_plot():
    for widget in plot.winfo_children():
        widget.destroy()

def integration_calculated():
    try:
        clear_previous_plot()
        function_input = fonc.get()
        function_call = sp.sympify(function_input)
        a = float(entry_inf.get())
        b = float(entry_sup.get())
        result = sp.integrate(function_call, (x,a,b))
        label_show.config(text = f"L'intégration de votre fonction de {a} à {b} est : {result}")
        f_integrated = sp.lambdify(x, function_call, "numpy")
        x_plot = np.linspace(a ,b ,400)
        y_plot = f_integrated(x_plot)
        if isinstance(y_plot, (int, float, complex, sp.Number)):
            y_plot = np.full_like(x_plot, float(y_plot))
        fig, ax = plt.subplots()
        ax.plot(x_plot,y_plot, color = "blue", label = "f(x)")
        ax.fill_between(x_plot,y_plot,  color = "skyblue", label = "L'aires")
        plt.title("La graphique de l'intégrale")
        ax.legend()
        ax.grid(True)
        canvas = FigureCanvasTkAgg(fig, master=plot)
        canvas.draw()
        plt.close(fig)
        canvas.get_tk_widget().pack()

    except Exception as e:
        messagebox.showerror("Erreur", "Veuillez revérifier la fonction ou la borne supérieure ou inférieure que vous avez saisie !")

def differentiation_calcul():
    try :
        clear_previous_plot()
        function_input = fonc.get()
        function_call = sp.sympify(function_input)
        x0 = float(entry_diff_x0.get())
        result = sp.diff(function_call, x)
        k = result.subs(x, sp.sympify(x0))
        y0 = float(function_call.subs(x, x0))
        phuong_trinh_tiep_tuyen = k*(x-x0) + y0
        label_show.config(text=f"La tangence de la fonction sur le point x0 ={x0}: y = {k:.2f}*(x - {x0}) + {y0:.2f}", fg="black")
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
        ax.plot(trucx, trucy, color = "blue", label = "f'(x)")
        ax.plot(trucx, trucyreal, color = "red", label = "La tangence de la fonction f(x)")
        ax.legend()
        ax.grid(True)
        canvas = FigureCanvasTkAgg(fig, master=plot)
        canvas.draw()
        plt.close(fig)
        canvas.get_tk_widget().pack()
    except Exception as e:
        messagebox.showerror("Erreur", "Impossible de calculer la dérivée à ce stade !")

def limit_calculation(): 
    try:    
        clear_previous_plot()
        function_input = fonc.get()
        function_call = sp.sympify(function_input)
        
        limit_input = entry_lim_x.get()
        limit = sp.sympify(limit_input)
        
        limit_result = sp.limit(function_call, x, limit)
        output_text = f"La limite = {limit_result}\n"
        
        value = function_call.subs(x, limit)
        if value.is_real:
            output_text += f"La result de la fonction = {value}"
        else:
            output_text += "La fonction n'est pas définie pour le moment"
            
        label_show.config(text=output_text, fg="black")
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
            canvas = FigureCanvasTkAgg(fig, master=plot)
            canvas.draw()
            plt.close(fig)
            canvas.get_tk_widget().pack()
        else:
            print("Impossible de tracer le graphique ")
            
    except Exception as e:
        label_show.config(text= "Erreur de syntaxe ou impossible de tracer !", fg="red")


def show_diff_input():
    hide_integral_input()
    hide_limite_input()
    label_diff_x0.pack(side="left", padx=5)
    entry_diff_x0.pack(side="left", padx=5)
    entry_diff_x0.focus()
    button.config(command = differentiation_calcul, text = "La dérivée")

def show_limite_input():
    hide_integral_input()
    hide_diff_input()
    label_lim_x.pack(side="left", padx=5)
    entry_lim_x.pack(side="left", padx=5)
    entry_lim_x.focus() 
    button.config(command = limit_calculation, text = "La limite")

def show_integral_input():
    hide_limite_input()
    hide_diff_input()
    label_inf.pack(side="left", padx=2)
    entry_inf.pack(side="left", padx=5)
    label_sup.pack(side="left", padx=10)
    entry_sup.pack(side="left", padx=5)
    entry_inf.focus() 
    button.config(command = integration_calculated, text = "L'intégrale")

def hide_limite_input():
    label_lim_x.pack_forget()
    entry_lim_x.pack_forget()

def hide_integral_input():
    label_inf.pack_forget()
    entry_inf.pack_forget()
    label_sup.pack_forget()
    entry_sup.pack_forget()

def hide_diff_input():
    label_diff_x0.pack_forget()
    entry_diff_x0.pack_forget()

root = tk.Tk()
root.geometry("1000x850")
root.title("LE CALCUL")
root.config(bg = "#F4F1F1")

label  = tk.Label(root, text = "CALCUL ET VISUALISATION", font = ("Times New Roman", 40),bg = "#F4F1F1" ,fg = "#5B4EE8")
label.pack(padx = 20, pady = 5)

sub_title = tk.Label(root, text = "SAISISSEZ VOTRE EQUATION S'IL TE PLAIT", font = ("Times New Roman", 20), bg = "#F4F1F1", fg = "#DC3D3D" )
sub_title.pack(padx = 40, pady = 5)

sub_sub_title = tk.Label(root, text = "Attention, 3^x doit être écrit sous la forme 3**x, 3x = 3*x", font = ("Times New Roman", 15), bg = "#F4F1F1")
sub_sub_title.pack(padx = 40, pady = 5)

frame_enter = tk.Frame(root, bg = "#F4F1F1")
frame_enter.pack(pady=4)

tk.Label(frame_enter, text="Saisissez votre fonction :", font=("Times New Roman", 15), bg = "#F4F1F1").grid(row=0, column=0, padx=5, pady=5)
fonc = tk.Entry(frame_enter, width=35, font=("Times New Roman", 15), justify="center")
fonc.grid(row=0, column=1, padx=5, pady=5, ipadx=100, ipady=5)

frame_extra_inputs = tk.Frame(root, bg = "#F4F1F1")
frame_extra_inputs.pack(pady=5)

label_diff_x0 = tk.Label(frame_extra_inputs, text="Saisissez le point x0 pour la tangente (x0) :", font=("Times New Roman", 14, "bold"), bg = "#F4F1F1", fg="#5B4EE8")
entry_diff_x0 = tk.Entry(frame_extra_inputs, width=10, font=("Times New Roman", 14), justify="center")

label_lim_x = tk.Label(frame_extra_inputs, text="Saisissez la valeur vers laquelle x tend (x ->) :", font=("Times New Roman", 14, "bold"), bg = "#F4F1F1", fg="#5B4EE8")
entry_lim_x = tk.Entry(frame_extra_inputs, width=10, font=("Times New Roman", 14), justify="center")

label_inf = tk.Label(frame_extra_inputs, text="Borne inférieure :", font=("Times New Roman", 14, "bold"), bg = "#F4F1F1", fg="#5B4EE8")
entry_inf = tk.Entry(frame_extra_inputs, width=8, font=("Times New Roman", 14), justify="center")

label_sup = tk.Label(frame_extra_inputs, text="Borne supérieure :", font=("Times New Roman", 14, "bold"), bg = "#F4F1F1", fg="#5B4EE8")
entry_sup = tk.Entry(frame_extra_inputs, width=8, font=("Times New Roman", 14), justify="center")

frame_buttons = tk.Frame(root, bg = "#F4F1F1")
frame_buttons.pack(pady=20)

button_diff = tk.Button(frame_buttons, text = "La dérivée", width = 15, font = ("Times New Roman", 20), bg = "#F4F1F1", command= show_diff_input)
button_diff.pack(side = "left", padx = 20)

button_integral = tk.Button(frame_buttons, text = "L'intégrale", width = 15, font = ("Times New Roman", 20), bg = "#F4F1F1", command=show_integral_input)
button_integral.pack(side = "left", padx = 20)

button_limite = tk.Button(frame_buttons, text = "La limite", width = 15, font = ("Times New Roman", 20), bg = "#F4F1F1", command=show_limite_input)
button_limite.pack(side = "left", padx = 20)

button = tk.Button(root, text="Veuillez choisir une méthode", font=("Times New Roman", 16, "bold"), bg="#5B4EE8", fg="#140202", width=25)
button.pack(pady=10)

result_frame = tk.LabelFrame(root, text = "Résultat du calcul", font = ("Times New Roman", 14, "italic"), bg = "#F5F5F5", padx = 10, pady = 10)
result_frame.pack(pady=10, fill="both", expand=True, padx=20)

label_show = tk.Label(result_frame, text="Veuillez saisir les variables et cliquer sur le bouton.", font=("Times New Roman", 15), bg="#F5F5F5", fg="#808080")
label_show.pack(pady=20)

plot = tk.Frame(root, bg="#F4F1F1")
plot.pack(pady=5, fill="both", expand=True)

root.mainloop()



