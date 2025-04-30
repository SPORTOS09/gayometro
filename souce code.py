import tkinter as tk
from tkinter import messagebox

# Domande e punteggi
domande = [
    {"testo": "Coca Cola o Pepsi?", "opzioni": {"C": 0, "P": 10}},
    {"testo": "Giochi a League of Legends?", "opzioni": {"S": 40, "N": 0}},
    {"testo": "Hai i capelli colorati?", "opzioni": {"S": 20, "N": 0}},
    {"testo": "Sei bello?", "opzioni": {"S": 10, "N": 0}},
    {"testo": "Ascolti musica classica?", "opzioni": {"S": 20, "N": 0}}
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz - Livello Gay")
        self.punteggio = 0
        self.domanda_corrente = -1

        self.label = tk.Label(root, text="Ciao, vuoi giocare?", font=("Arial", 14))
        self.label.pack(pady=20)

        self.bottone_si = tk.Button(root, text="Sì", width=10, command=self.inizia_gioco)
        self.bottone_si.pack()

        self.bottone_no = tk.Button(root, text="No", width=10, command=self.risposta_no)
        self.bottone_no.pack()

    def inizia_gioco(self):
        self.bottone_si.pack_forget()
        self.bottone_no.pack_forget()
        self.prossima_domanda()

    def risposta_no(self):
        messagebox.showinfo("Risposta", "Sei gay")
        self.root.destroy()

    def prossima_domanda(self):
        self.domanda_corrente += 1

        if self.domanda_corrente < len(domande):
            domanda = domande[self.domanda_corrente]
            self.label.config(text=domanda["testo"])

            for widget in self.root.winfo_children():
                if isinstance(widget, tk.Button) and widget not in [self.bottone_si, self.bottone_no]:
                    widget.destroy()

            for risposta in domanda["opzioni"].keys():
                tk.Button(self.root, text=risposta, width=10,
                          command=lambda r=risposta: self.valuta_risposta(r)).pack(pady=5)
        else:
            self.mostra_risultato()

    def valuta_risposta(self, risposta):
        punteggio_domanda = domande[self.domanda_corrente]["opzioni"].get(risposta, 0)
        self.punteggio += punteggio_domanda
        if self.domanda_corrente == 3 and risposta == "S":
            messagebox.showinfo("Risposta", "Bugiardo")
        elif self.domanda_corrente == 0 and risposta == "P":
            messagebox.showinfo("Risposta", "Ok -_-")
        else:
            messagebox.showinfo("Risposta", "Ok")
        self.prossima_domanda()

    def mostra_risultato(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.label = tk.Label(self.root, text=f"Il tuo punteggio è {self.punteggio}% livello gay", font=("Arial", 14))
        self.label.pack(pady=20)

# Avvio dell'app
root = tk.Tk()
app = QuizApp(root)
root.mainloop()
