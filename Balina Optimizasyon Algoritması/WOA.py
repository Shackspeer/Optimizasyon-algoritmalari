import numpy as np 



# --------------------------------------------------
#   AMAÇ FONKSİYONU
#   --------------------
#   Amaç fonksiyonu belirleyip CostFunction
#   içerisine yazabiliriz.
# --------------------------------------------------

def CostFunction():
    return ''    



# --------------------------------------------------
#   UYGUNLUK DEĞERLERİNİ HESAPLAMA
#   ------------------------------
#   Uygunluk değerlerini hesapladıktan sonra
#   değerler bir dizi şeklinde döndürülecek.
# --------------------------------------------------
def Fitnesses(population):
    Calculated = np.zeros_like(population)
    for i in range(len(population)):
        Calculated[i] = CostFunction(population[i])
        





# --------------------------------------------------
#  POPÜLASYON OLUŞTURMA
#  --------------------
#  NP --> Popülayson büyüklüğü
#  D  --> Çözüm vektörünün büyüklüğü
#  LB --> Alt sınır
#  UB --> Üst sınır
#---------------------------------------------------

def CreatePopulation(NP,D,LB,UB):
    population = np.random.uniform(LB,UB,(NP,D))
    return population
