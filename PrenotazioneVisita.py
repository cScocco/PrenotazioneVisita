import tkinter as tk


class SistemaVisite(object):

    def __init__(self):
        self.__prenotazioni = []  # lista (vuota) delle prenotazioni

        # finestra di gestione visite
        self.w_sistema_visite = tk.Tk()
        self.w_sistema_visite.geometry("300x30+900+200")
        self.w_sistema_visite.title("sistema visite")
        self.w_sistema_visite.grid()
        self.lbl_in_attesa = tk.Label(self.w_sistema_visite, text="in attesa : ")
        self.lbl_in_attesa.grid(row=0, column=0)
        self.vIn_attesa = tk.IntVar()
        self.txt_in_attesa = tk.Entry(self.w_sistema_visite, textvariable=self.vIn_attesa, state=tk.DISABLED)
        self.txt_in_attesa.grid(row=0, column=1)
        self.btn_prossimo = tk.Button(self.w_sistema_visite, text="prossimo", command=self.__prossima_prenotazione)
        self.btn_prossimo.grid(row=0, column=2)
        self.btn_chiusura = tk.Button(self.w_sistema_visite, text="chiusura", command=self.__chiusura)
        self.btn_chiusura.grid(row=0, column=3)

        # finestra per inserimento nuova prenotazione
        self.w_prenotazione = tk.Toplevel(self.w_sistema_visite)
        self.w_prenotazione.title("prenotazione")
        self.w_prenotazione.geometry("300x30+100+200")
        self.w_prenotazione.grid()
        self.lbl_nominativo = tk.Label(self.w_prenotazione, text="Inserire nominativo : ")
        self.lbl_nominativo.grid(row=0, column=0)
        self.vNominativo = tk.StringVar()
        self.txt_nominativo = tk.Entry(self.w_prenotazione, textvariable=self.vNominativo)
        self.txt_nominativo.grid(row=0, column=1)
        self.btn_invio = tk.Button(self.w_prenotazione, text="invio", command=self.__nuova_prenotazione)
        self.btn_invio.grid(row=0, column=2)

        # finestra di visualizzazione chiamata
        self.w_chiamata = tk.Toplevel(self.w_sistema_visite)
        self.w_chiamata.title("Chiamata")
        self.w_chiamata.geometry("300x60+500+200")
        self.w_chiamata.grid()
        self.lbl_in_attesa_2 = tk.Label(self.w_chiamata, text="in attesa : ")
        self.lbl_in_attesa_2.grid(row=0, column=0)
        self.vIn_attesa_2 = tk.IntVar()
        self.txt_in_attesa_2 = tk.Entry(self.w_chiamata, textvariable=self.vIn_attesa_2, state=tk.DISABLED)
        self.txt_in_attesa_2.grid(row=0, column=1)
        self.lbl_chiamata = tk.Label(self.w_chiamata, text="Chiamata : ")
        self.lbl_chiamata.grid(row=1, column=0)
        self.vChiamato = tk.StringVar()
        self.txt_chiamato = tk.Entry(self.w_chiamata, textvariable=self.vChiamato, state=tk.DISABLED)
        self.txt_chiamato.grid(row=1, column=1)

        self.__aggiorna_GUI()
        self.w_sistema_visite.mainloop()

    def __aggiorna_GUI(self):
        in_attesa = len(self.__prenotazioni)
        self.vIn_attesa.set(in_attesa)
        self.vIn_attesa_2.set(in_attesa)
        if in_attesa == 0:
            self.btn_prossimo['state'] = tk.DISABLED
        else:
            self.btn_prossimo['state'] = tk.NORMAL

    def __nuova_prenotazione(self):
        self.__prenotazioni.append(self.vNominativo.get())
        self.vNominativo.set("")
        self.__aggiorna_GUI()

    def __prossima_prenotazione(self):
        self.vChiamato.set(self.__prenotazioni.pop(0))
        self.__aggiorna_GUI()

    def __chiusura(self):
        self.w_sistema_visite.destroy()


def main():
    SistemaVisite()


main()
