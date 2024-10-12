import tkinter as tk
from tkinter import messagebox, Listbox, Scrollbar, Frame
import pygame  

Zamanlayıcı = {}


pygame.mixer.init()
ses_dosyasi = "C:/Users/W11/Desktop/SureTut/SüreDoldu.WAV"  
pygame.mixer.music.load(ses_dosyasi)

def süre_tut():
    try:
        isim = isim_entry.get()
        if not isim:
            messagebox.showerror("Hata", "İsim boş olamaz.")
            return
        if any(char.isdigit() for char in isim):
            messagebox.showerror("Hata","İsim Sayı Olamaz.")
            return
    except ValueError:
        messagebox.showerror("Hata","İsim Sayı Olamaz.")
        return    

    if isim in Zamanlayıcı:
        messagebox.showwarning("Uyarı", f"{isim} için zaten bir süre tutuluyor.")
        return

    try:
        dakika = int(süre_entry.get())
        if dakika < 0:
            raise ValueError("Süre negatif olamaz.")
        elif dakika > 60:
            raise ValueError("Süre 1 saati geçemez.")
    except ValueError as e:
        messagebox.showerror("Hata", f"Geçersiz süre: {e}")
        return

    toplam_saniye = dakika * 60
    Zamanlayıcı[isim] = toplam_saniye 

    liste.insert(tk.END, f"{isim} - Süre: {dakika} dakika")
    row_index = liste.size() - 1

    def GeriSayım():
        nonlocal toplam_saniye
        if toplam_saniye >= 0:
            dakika_kalan = toplam_saniye // 60
            saniye_kalan = toplam_saniye % 60
            
            liste.delete(row_index)  
            liste.insert(row_index, f"Kalan Süre: {isim} - {dakika_kalan} dakika {saniye_kalan} saniye")
            toplam_saniye -= 1
            Zamanlayıcı[isim] = toplam_saniye
            
            pencere.after(1000, GeriSayım)
        else:
            pygame.mixer.music.play() 
            liste.delete(row_index) 
            liste.insert(row_index, f"{isim} için süre doldu.")
            messagebox.showinfo("Süre Doldu", f"{isim} için süre doldu.")
            del Zamanlayıcı[isim]

    GeriSayım()

pencere = tk.Tk()
pencere.title("Süreyi Başlat Programı")
pencere.geometry("500x400")
pencere.resizable(width=False, height=False)
pencere.iconbitmap("C:/Users/W11/Desktop/SureTut/Süre.ico")
pencere.configure(background="#624E88")

isim_label = tk.Label(pencere, text="İsim:", font=("Arial", 12, "bold"), bg="#624E88", fg="#F5F7F8")
isim_label.grid(row=0, column=0, padx=10, pady=10)

isim_entry = tk.Entry(pencere)
isim_entry.grid(row=0, column=1, padx=10, pady=10)

süre_label = tk.Label(pencere, text="Süre (dakika):", font=("Arial", 12, "bold"), bg="#624E88", fg="#F5F7F8")
süre_label.grid(row=1, column=0, padx=10, pady=10)

süre_entry = tk.Entry(pencere)
süre_entry.grid(row=1, column=1, padx=10, pady=10)

Süreyi_Tut_button = tk.Button(pencere, text="Süreyi Tut", bg="#624E88", fg="#F5F7F8", font=("Arial", 12, "bold"), command=süre_tut)
Süreyi_Tut_button.grid(row=2, columnspan=2, pady=20)

frame = Frame(pencere)
frame.grid(row=3, columnspan=2, pady=20)

liste = Listbox(frame, width=80, height=15)
liste.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
scrollbar.config(command=liste.yview)
liste.config(yscrollcommand=scrollbar.set)

pencere.mainloop()
