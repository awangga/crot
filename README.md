# crot
Convolution based Object Recognition Detection 
How to use :

```py
import crot
ngok=crot.Crot()
ngok.setInput('inputs/1.jpeg')
anu=ngok.getObjects()
print('Jumlah Objek Adalah : '+str(len(anu)))
print(anu)
```