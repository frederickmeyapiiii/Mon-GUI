import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox, simpledialog
from tkinter.colorchooser import askcolor
import subprocess
import sys

def nouveau_fichier():
    if len(text_area.get('1.0', tk.END)) > 1:  # Si le texte n'est pas vide
        result = messagebox.askyesno("Enregistrer", "Voulez-vous enregistrer le fichier actuel ?")
        if result:
            enregistrer_fichier()

    text_area.delete(1.0, tk.END)


def ouvrir_fichier():
    filepath = filedialog.askopenfilename(filetypes=[("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")])
    if not filepath:
        return
    text_area.delete(1.0, tk.END)
    with open(filepath, 'r') as input_file:
        text = input_file.read()
        text_area.insert(tk.END, text)


def enregistrer_fichier():
    filepath = filedialog.asksaveasfilename(defaultextension="txt",
                                            filetypes=[("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")])
    if not filepath:
        return
    with open(filepath, 'w') as output_file:
        text = text_area.get(1.0, tk.END)
        output_file.write(text)


def enregistrer_sous_fichier():
    filepath = filedialog.asksaveasfilename(defaultextension="txt",
                                            filetypes=[("Fichiers texte","*.txt"),("Tous les fichiers","*.*")])

    if not filepath:
        return
    with open(filepath,'w') as output_file:
        text = text_area.get(1.0,tk.END)
        output_file.write(text)

def copier_texte():
    root.clipboard_clear
    text = text_area.get("sel.first","sel.last")
    root.clipboard_append(text)

def coller_texte():
    text = root.clipboard_get()
    text_area.insert(tk.INSERT,text)

def couleur():
    couleurs = askcolor(title="choose_Color")
    root.configure(bg=couleurs[1])
    text_area.config(fg=couleurs[1])

def taille():
    taille = simpledialog.askinteger("Taille","Entrez un nombre:")
    current_size = text_area.cget("font")
    text_area.config(font=(current_size,taille))

def calculatrice():
    subprocess.run([sys.executable, "CalcoTK.py"])

    
# Configuration de la fenêtre principale
root = tk.Tk()
root.title("Mon bloc note ")
root.geometry("2100x900")

# Configuration du champ de texte (Text widget)
text_area = tk.Text(root)
text_area.pack(expand=True, fill='both')

# Création de la barre de menu
bloc_note = tk.Menu(root)
# Menu Fichier
fichier_menu = tk.Menu(bloc_note, tearoff=0)
bloc_note.add_cascade(label="Fichier", menu=fichier_menu)
fichier_menu.add_command(label="Nouveau", command=nouveau_fichier)
fichier_menu.add_command(label="Ouvrir", command=ouvrir_fichier)
fichier_menu.add_command(label="enregistrer", command=enregistrer_fichier)
fichier_menu.add_command(label="enregistrer sous", command=enregistrer_sous_fichier)
fichier_menu.add_separator()
fichier_menu.add_command(label="Quitter", command=root.destroy)

édition_menu = tk.Menu(bloc_note, tearoff=0)
bloc_note.add_cascade(label="Edition",menu=édition_menu)
édition_menu.add_command(label="Copier", command=copier_texte)
édition_menu.add_command(label="Coller",command=coller_texte)

option_menu = tk.Menu(bloc_note, tearoff=0)
bloc_note.add_cascade(label="Option",menu=option_menu)
option_menu.add_command(label="Taille", command=taille)
option_menu.add_command(label="Couleur", command=couleur)

outils_menu = tk.Menu(bloc_note, tearoff=0)
bloc_note.add_cascade(label="Outils", menu=outils_menu)
outils_menu.add_command(label="calculatrice", command=calculatrice)

# Configurer la fenêtre pour utiliser la barre de menu créée
root.config(menu=bloc_note)

# Lancer l'application
root.mainloop()

