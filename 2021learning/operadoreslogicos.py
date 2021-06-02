"""                                        
True and True -> True otro caso -> False   
Con or minimo un True da true              
Negacion not(True) -> False                
not (False) -> True                        
1. Not                                     
2. And                                     
3. Or                                      
"""                                        
a = 10                                     
b = 15                                     
c = 20                                     
resultado = ((a > b) and (b < c))          
print(resultado)                           
resultado = ((a > b) or (b < c))           
print(resultado)                           
print(not resultado)                       
