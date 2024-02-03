from matakuliah import Matakuliah

# Update Data
a = Matakuliah()
kodemk = 'PRAKTIKUMPBO'
a.namamk = "BISMILLAH CUMLOD"
a.sks = "4"
a.updateBykodemk(kodemk)
b = a.getAllData()
print(b)
