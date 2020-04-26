# TP : Cookie clicker
# 1. Créer une fenêtre avec un cookie au centre de l'écran
# 2. Créer un compteur
# 3. Une boutique

# Création de la fenêtre
from tkinter import *
import tkinter as tk
from tkinter import messagebox



window = Tk()

# Personalisation de la fenêtre

window.title("Graven Clicker")
window.geometry("1080x720")
window.iconbitmap("sweet.ico")
window.config(bg="#B0700A")

# Créer le calcul permettant de créer le compteur de clic
count = 0
click = tk.IntVar()
click.set(0)
multi = 0


def clicked():
    global count

    count += 1
    click.set(str(count))
    print(count)

#
# def multiplyer():
#     global multi
#
#     if count >= buy_multiclicker




# Créer la Frame
frame = Frame(window, bg="#B0700A")

# Création d'un second frame
# left_frame = tk.Frame(frame, bg="#B0700A")


# Création du titre
label_title = Label(text="Graven Clicker !", font=("Girassol", 40), bg="#B0700A", fg="White")
label_title.pack()

# window.wm_attributes("-transparentcolor") # Rend transparent la donné choisi par la couleur

# Créer un boutotn
photo = PhotoImage(file="graven.png")
cookie_button = Button(frame, image=photo, bg='#B0700A', bd=0, highlightthickness=0, command=clicked, activebackground="#B0700A")
cookie_button.pack()

# Afficher les compteur de click
label_click = Label(frame, textvariable=click, font=("Girassol", 25), bg="#B0700A", fg="White")
label_click.pack(padx=50, pady=50)

# Print le nombre de multiply_cookie d'acheté
nb_multiply = Label(window, text=0, font=("Girassol", 12), bg="#B0700A", fg="White")
nb_multiply.pack(side=RIGHT, padx=1, pady=10)

# creer le bouton multiplicateur de cookie

multiply_cookie = Button(window, text="Acheter un multiplicateur :", font=("Helvetica", 12), bg='#B0700A', fg="Black", bd=2, highlightthickness=2, activebackground="#B0700A", command=...)
multiply_cookie.pack(side=RIGHT, padx=50, pady=70)

# Print le nombre d'autoclicker d'acheté

mulclick = Label(window, text=0, font=("Helvetica", 12), bg="#B0700A", fg="White")
mulclick.pack(side=RIGHT, padx=0, pady=0)

# creer le bouton autockicker de cookie

auto = Button(window, text="Acheter un autoclickeur :", font=("Helvetica", 12), bg='#B0700A', fg="Black", bd=2, highlightthickness=2, activebackground="#B0700A", command=...)
auto.pack(side=RIGHT,  padx=50, pady=100)



# création d'une barre de menu
menu_bar = Menu(window)


# créer un premier menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Nouveau', command=clicked)
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)

# configurer notre fenêtre pour ajouter cette menu bar
window.config(menu=menu_bar)

# Afficher la Frame

frame.pack(side=LEFT)
window.mainloop()
