from matakuliah import Matakuliah

a = Matakuliah()
kodemk = 'STDA22TI'  # Mendefinisikan nilai untuk variabel 'kodemk'
a.deleteBykodemk(kodemk)
b = a.getAllData()
print(b)
