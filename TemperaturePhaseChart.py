import matplotlib.pyplot as plt

year = ["MAPbBr$_3$", "FAPbBr$_3$","MAPbCl$_3$","FAPbCl$_3$", "FASnI$_3$", "FAPbI$_3$", "MASnI$_3$", "MAPbI$_3$", "CsSnI$_3$", "CsPbI$_3$"]  
hexagonal = [0.001, 0.001, 0.001, 0.001, 0.001, 220, 0.001, 0.001, 0.001, 0.001]
orthorhombic = [144.5, 125, 172.9, 172, 132.5, 0, 114, 162.2, 351, 573.15]
tetragonal = [92.4, 140, 5.9, 7, 100, 65 ,161, 165.2, 75 ,0]
cubic = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]

plt.figure(figsize=(8,6))
# careful: notice "bottom" parameter became "left"
plt.barh(year, hexagonal, color = 'red')
plt.barh(year, orthorhombic, left=hexagonal)
plt.barh(year, tetragonal, left=list(map(lambda a, b : a + b, hexagonal, orthorhombic)))
plt.barh(year, cubic, left=list(map(lambda a, b, c : a + b + c, hexagonal, orthorhombic, tetragonal))) 

# we also need to switch the labels
plt.xlabel('Temperature (K)')  
#plt.ylabel('Material')
plt.legend(['Hexagonal','Orthohombic','Tetragonal','Cubic'], loc = 4 )
plt.xlim(0,700)
plt.savefig('PhaseChangeTemp.png')