import tkinter as tk

#Définition d'une fonction pour ajouter les numéros cliqué
def calco(button_text):
    calc.insert(tk.END, button_text)

#Définition de la fonction pour effacer  
def clear_calc ():
    calc.delete(0, tk.END)

#Définition de la fonction pour calculer et afficher le résultat 
def calculate():
    try: 
        result = eval(calc.get())
        calc.delete(0, tk.END)
        calc.insert(0, result)
    except:
        calc.delete(0, tk.END)
        calc.insert(0, "Error")

#Création de la fenêtre principale
root = tk.Tk()
root.title("Ma Calculatrice")

#Champ d'affichage
calc = tk.Entry(root, width=20, font=('Arial',14))
calc.grid(row=0, column=0, columnspan=4)

#Les differents textes des boutons
button_textes =[
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "C", "0","+","="
]

#Créer et classer les boutons dans une grille
for i, button_text in enumerate(button_textes):
    row = i // 4 + 1 #Ici on ajoute 1 pour sauter la première ligne réservée à l'Entry
    col = i % 4
    button = tk.Button(root, text=button_text , width=5 , height=2, font=('Arial', 14) , command=lambda text=button_text: calco(text))
    button.grid(row=row, column=col , padx=5, pady=5)

#Ajout des autres boutons
clear_button = tk.Button(root, text="C", width=5, height=2,font=('Arial', 14), command=clear_calc)
clear_button.grid(row=4, column=0, padx=5, pady=5)

equal_button = tk.Button(root, text="=", width=5, height=2, font=('Arial', 14), command=calculate)
equal_button.grid(row=4, column=3, padx=5, pady=5)

#Lancement de la boucle
root.mainloop()