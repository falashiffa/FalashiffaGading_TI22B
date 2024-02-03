from tkinter import *
from datetime import date

root = Tk()
root.geometry("450x300")
root.title("Kalkulator Umur")

def kalkulatorUmur():
    today = date.today()
    birth_date = date(int(year_entry.get()), int(month_entry.get()), int(day_entry.get()))
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

    Label(text=f"Hi {nama_value.get()}! umur mu adalah : {age} tahun", font=("arial", 15, "bold")).grid(row=6, column=1)

Label(text="Nama",font=("Times New Roman", 15, "bold")).grid(row=1, column=0, padx=50)
Label(text="Tahun lahir",font=("Times New Roman", 15, "bold")).grid(row=2, column=0)
Label(text="Bulan lahir",font=("Times New Roman", 15, "bold")).grid(row=3, column=0)
Label(text="Tanggal lahir",font=("Times New Roman", 15, "bold")).grid(row=4, column=0)

nama_value=StringVar()
year_value=StringVar()
month_value=StringVar()
day_value=StringVar()

nama_entry= Entry(root, textvariable=nama_value)
year_entry= Entry(root, textvariable=year_value)
month_entry= Entry(root,textvariable=month_value)
day_entry= Entry(root, textvariable=day_value)

nama_entry.grid(row=1, column=1, pady=5)
year_entry.grid(row=2, column=1, pady=5)
month_entry.grid(row=3, column=1, pady=5)
day_entry.grid(row=4, column=1, pady=5)

button= Button(text="Kalkulator Umur", font=("Arial",15,"bold"), fg="magenta", command=kalkulatorUmur)
button.grid(row=5, column=1, pady=5)


root.mainloop()