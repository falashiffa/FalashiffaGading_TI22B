# file_utama.py
import tkinter as tk
from Kalkulator_Bangun_Ruang import CalculatorApp,Kalkulator_Bangun_Ruang

# Menggunakan fungsi dari modul_tambahan
Kalkulator_Bangun_Ruang()

# Membuat instance dari kelas modul
objek_modul = CalculatorApp()

# Menggunakan tkinter
root = tk.Tk()
label = tk.Label(root)
label.pack()
root.mainloop()
