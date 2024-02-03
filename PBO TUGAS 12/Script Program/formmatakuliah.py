import tkinter as tk
from tkinter import Frame, Label, Entry, Button,Radiobutton, ttk, VERTICAL, YES, BOTH, END, Tk, W, StringVar, messagebox
from matakuliah import Matakuliah


class FormMatakuliah:

    def __init__(self, parent, title):
        self.parent = parent
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        # Label
        Label(mainFrame, text='Kode Matakuliah:').grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        self.txtkodemk = Entry(mainFrame)
        self.txtkodemk.grid(row=0, column=1, padx=10, pady=5)
        # menambahkan event Enter key
        self.txtkodemk.bind("<Return>", self.onCari)

        Label(mainFrame, text='Nama Matakuliah:').grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        self.txtnamamk = Entry(mainFrame)
        self.txtnamamk.grid(row=1, column=1, padx=10, pady=5)

        Label(mainFrame, text='Jumlah SKS:').grid(row=2, column=0, sticky=W, padx=10, pady=5)
        self.txtSks = StringVar()
        self.option1 = Radiobutton(mainFrame, text='1 SKS', value='12', variable=self.txtSks)
        self.option1.grid(row=3, column=1, padx=10, pady=5, sticky=W)
        self.option1.select() # set pilihan yang pertama sebagai default
        self.option2 = Radiobutton(mainFrame, text='2 SKS', value='14', variable=self.txtSks)
        self.option2.grid(row=3, column=2, padx=10, pady=5, sticky=W)
        self.option3 = Radiobutton(mainFrame, text='3 SKS', value='16', variable=self.txtSks)
        self.option3.grid(row=3, column=3, padx=10, pady=5, sticky=W)
        self.option4 = Radiobutton(mainFrame, text='4 SKS', value='18', variable=self.txtSks)
        self.option4.grid(row=3, column=4, padx=10, pady=5, sticky=W)

        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan',command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=5, padx=10, pady=5)
        self.btnClear = Button(mainFrame, text='Clear',command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=5, padx=10, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=lambda: self.onDelete(self.txtkodemk.get()), width=10)
        self.btnHapus.grid(row=2, column=5, padx=10, pady=5)

        # define columns
        columns = ('idmk', 'kodemk', 'namamk', 'sks')

        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('idmk', text='ID')
        self.tree.column('idmk', width="50")
        self.tree.heading('kodemk', text='Kode Matakuliah')
        self.tree.column('kodemk', width="200")
        self.tree.heading('namamk', text='Nama Matakuliah')
        self.tree.column('namamk', width="300")
        self.tree.heading('sks', text='Jumlah sks')
        self.tree.column('sks', width="100")
        # set tree position
        self.tree.place(x=0, y=200)
        self.onReload()

    def onClear(self, event=None):
        self.txtkodemk.delete(0, END)
        self.txtnamamk.delete(0, END)
        self.txtsks.set("")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False

    def onReload(self, event=None):
        # get data matakuliah
        mk = Matakuliah()
        result = mk.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        students = []
        for row_data in result:
            students.append(row_data)

        for student in students:
            self.tree.insert('', END, values=student)

    def onCari(self, event=None):
        kodemk = self.txtkodemk.get()
        mk = Matakuliah()
        res = mk.getBykodemk(kodemk)
        rec = mk.affected
        if (rec > 0):
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan")
            self.ditemukan = False
            self.txtnamamk.focus()
        return res

    def TampilkanData(self, event=None):
        kodemk = self.txtkodemk.get()
        mk = Matakuliah()
        res = mk.getBykodemk(kodemk)
        self.txtnamamk.delete(0, END)
        self.txtnamamk.insert(END, mk.namamk)
        self.txtsks.set(mk.sks)
        self.btnSimpan.config(text="Update")

    def onSimpan(self, event=None):
        kodemk = self.txtkodemk.get()
        namamk = self.txtnamamk.get()
        sks = self.txtsks.get()
        mk = Matakuliah()
        mk.kodemk = kodemk
        mk.namamk = namamk
        mk.sks = sks
        if (self.ditemukan == True):
            res = mk.updateBykodemk(kodemk)
            ket = 'Diperbarui'
        else:
            res = mk.simpan()
            ket = 'Disimpan'

        rec = mk.affected
        if (rec > 0):
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec

    def onDelete(self, event=None):
        kodemk = self.txtkodemk.get()
        mk = Matakuliah()
        res = mk.getBykodemk(kodemk)
        rec = mk.affected

        if rec > 0:
            # Jika data ditemukan, munculkan konfirmasi untuk menghapus
            confirm = messagebox.askyesno(
                "Konfirmasi", "Apakah Anda yakin ingin hapus Mata Kuliah ini?")
            if confirm:
                res = mk.deleteBykodemk(kodemk)
                rec = mk.affected
                if rec > 0:
                    messagebox.showinfo("showinfo", "Mata Kuliah Berhasil dihapus")
                else:
                    messagebox.showwarning(
                        "showwarning", "Gagal menghapus Mata Kuliah")
        else:
            # Jika data tidak ditemukan, tampilkan pesan peringatan
            messagebox.showwarning("showwarning", "Mata Kuliah Tidak Ditemukan")

        self.onClear()

    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()


if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = FormMatakuliah(
        root, "Aplikasi Data Matakuliah")
    root.mainloop()
