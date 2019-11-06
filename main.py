import crot


ngok=crot.Crot()


for i in range(9):
    fimage='inputs/'+str(i+1)+'.jpeg'
    print(fimage)
    ngok.setInput(fimage)
    anu=ngok.getObjects()
    print('Jumlah Objek Adalah : '+str(len(anu)))
    print(anu)

