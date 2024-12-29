# Notwendige Module importieren
import tkinter as tk  # Für die Widgets
import random   # Um zufällige Tetris-Figuren anzuzeigen
random.seed()   # Damit die zufällige Zahl abhängig von der Zeit ist.

""" Eine Funktion, welche einen Pixel analysiert. Hat dieser die Hintergrundfarbe (169, 179, 21), 
    dann wird der Wert 0 wiedergegeben, ansonsten 1"""
def einsOderNull(x, y):
    if tk.PhotoImage(file=Figur[Auswahl]).get(x, y) == (169, 179, 21):
        return 0
    else:
        return 1

""" Diese Funktion wird aktiviert, sobald auf den "Überprüfen"-Knopf gedrückt wird. 
    Die Struktur vom Bild in einer Liste mit 1 und 0 wiedergegeben.
    Danach wird diese Liste mit anderen bestimmten Listen verglichen, bis die Figur identifiziert ist.
    Der Name der identifizierten Figur wird dann als Text wiedergegeben. """
def Durchgang():
    bisSieben = 0   # Die bisSieben Variabel stellt sicher, dass sieben und nicht acht Zahlen in die Liste kommen.
    Struktur = []   # Struktur-Liste definieren und leeren
    for y in range(50, 76, 25):
        for x in range(25, 105, 25):
            Struktur.append(einsOderNull(x, y))
            bisSieben += 1
            if bisSieben == 7:
                break
# Wenn die Variable den Wert sieben hat, dann sind sieben Werte in der Liste, die Schleife wird daraufhin abgebrochen.

# Die fertige Struktur wird nun verglichen, findet man ein paar, wird der jeweilige Figurenname wiedergegeben.
    match Struktur:                 
        case [1, 1, 1, 1, 0, 0, 0]:
            FigurName["text"] = "I-Block"
        case [1, 1, 0, 0, 0, 1, 1]:
            FigurName["text"] = "Z-Block"
        case [0, 1, 1, 0, 0, 1, 1]:
            FigurName["text"] = "O-Block"
        case [1, 1, 1, 0, 1, 0, 0]:
            FigurName["text"] = "L-Block"
        case [1, 1, 1, 0, 0, 1, 0]:
            FigurName["text"] = "T-Block"
        case [0, 1, 1, 0, 1, 1, 0]:
            FigurName["text"] = "S-Block"
        case [1, 1, 1, 0, 0, 0, 1]:
            FigurName["text"] = "J-Block"
        case _:                     # Falls die Struktur nicht mit den Tetris-Blöcken übereinstimmt.
            FigurName["text"] = "Keine Tetris-Figur"

# Eine Funktion herstellen, welche ein neues zufällige Bild auswählt und den Text entfernt.
def random_Bild():
    global Auswahl
    Auswahl = random.randint(0,6)
    BlockBild = tk.PhotoImage(file=Figur[Auswahl])
    BlockLabel.configure(image=BlockBild)
    BlockLabel.image=BlockBild
    FigurName["text"] = ""

# Eine Liste, die alle Dateinamen der Tetris-Figuren beinhält.
Figur = ["I-Block.png", "Z-Block.png", "O-Block.png", "L-Block.png", "T-Block.png", "S-Block.png", "J-Block.png"]

# Das Fenster wird definiert.
fenster = tk.Tk()
fenster.title("Figurenerkennung")
fenster.geometry("300x200+500+300")
fenster.resizable(0, 0)

# Ein zufälliger Dateiname wird ausgewählt und angezeigt, abhängig von einer Zufallszahl.
Auswahl = random.randint(0,6)
BlockBild = tk.PhotoImage(file=Figur[Auswahl])
BlockLabel = tk.Label(fenster) 
BlockLabel["image"] = BlockBild
BlockLabel.place(x=150, y=10, anchor="n")

# Der Text unter dem Bild, welcher die Tetris-Figur wiedergibt.
FigurName = tk.Label(fenster, text="", width=20)
FigurName.place(x=148, y=165, anchor="s")

# Die beiden Knöpfe definieren.
Button_random_Bild = tk.Button(fenster, text="Zufallsbild", command=random_Bild, width=12)
Button_random_Bild.place(x=80, y=195, anchor="s")
Button_ueberpruefen = tk.Button(fenster, text="Überprüfen", command=Durchgang, width=12)
Button_ueberpruefen.place(x=220, y=195, anchor="s")

fenster.mainloop()