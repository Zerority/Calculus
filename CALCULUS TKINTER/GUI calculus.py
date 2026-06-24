import tkinter as tk 

def show_diff_input():
    hide_integral_input()
    hide_limite_input()
    label_diff_x0.pack(side="left", padx=5)
    entry_diff_x0.pack(side="left", padx=5)
    entry_diff_x0.focus()

def show_limite_input():
    hide_integral_input()
    hide_diff_input()
    label_lim_x.pack(side="left", padx=5)
    entry_lim_x.pack(side="left", padx=5)
    entry_lim_x.focus() 

def show_integral_input():
    hide_limite_input()
    hide_diff_input()
    label_inf.pack(side="left", padx=2)
    entry_inf.pack(side="left", padx=5)
    label_sup.pack(side="left", padx=10)
    entry_sup.pack(side="left", padx=5)
    entry_inf.focus() 

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
root.geometry("1000x700")
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

result_frame = tk.LabelFrame(root, text = "Résultat du calcul", font = ("Times New Roman", 14, "italic"), bg = "#F5F5F5", padx = 10, pady = 10)
result_frame.pack(pady=10, fill="both", expand=True, padx=20)

label_show = tk.Label(result_frame, text="Veuillez saisir les variables et cliquer sur le bouton.", font=("Times New Roman", 15), bg="#F5F5F5", fg="#808080")
label_show.pack(pady=20)

root.mainloop()