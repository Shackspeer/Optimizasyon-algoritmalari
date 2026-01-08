import numpy as np 








# --------------------------------------------------
#   AMAÇ FONKSİYONU
#   --------------------
#   Amaç fonksiyonu belirleyip CostFunction
#   içerisine yazabiliriz.
#   Bu örnekte Rosenbrock fonksiyonu kullanılmıştır.
#   Rosenbrock fonksiyonunun global minimum noktası f(1,1) = 0 noktasıdır.
# --------------------------------------------------

def CostFunction(X):

    cost = (1-X[0])**2 + 100*(X[1] - X[0]**2)**2
    
    if(cost < 0):
        evaluated = 1 / abs(cost)
    else : 
        evaluated = 1 / (1 + cost)

    return evaluated


# --------------------------------------------------
#   UYGUNLUK DEĞERLERİNİ HESAPLAMA
#   ------------------------------
#   Uygunluk değerlerini hesapladıktan sonra
#   değerler bir dizi şeklinde döndürülecek.
# --------------------------------------------------
def Fitnesses(population,G_Best,G_Best_F):
    for i in range(len(population)):
        # Fitness hesapla
        fitness = CostFunction(population[i])
        
        # En iyi fitness güncelle
        

        if fitness >= G_Best_F:
            G_Best_F = fitness
            G_Best = population[i].copy()
    
    return G_Best,G_Best_F
    
# --------------------------------------------------
#  POPÜLASYON OLUŞTURMA
#  --------------------
#  NP --> Popülayson büyüklüğü
#  D  --> Çözüm vektörünün büyüklüğü
#  LB --> Alt sınır
#  UB --> Üst sınır
#---------------------------------------------------

def CreatePopulation(NP=5,D=2,LB=-10,UB=10):
    return np.random.uniform(LB,UB,(NP,D))
    
#---------------------------------------------------
# GÜNCELLEME DEĞERLERİNİN HESAPLANMASI
# --------------------
# Her balinanın konumunu güncellemek için kullanacağımız
# a,A,C,l ve p değerlerinin hesaplanması bu bölümde 
# 
# Burada t mevcut iterasyonken , T maksimum iterasyon sayısıdır.
#---------------------------------------------------

def Calc(T,t,D):
    p = np.random.rand()
    a = 2 * (1 - t / T)
    A = 2 * a * np.random.rand(D) - a
    C = 2 * np.random.rand(D) # Arama uzayı yarıçapı için 2*r burada r yarıçap gibi düşünün
    l = 2 * np.random.rand() - 1 # [-1,1] aralığında sayı üretmek için
    return p,a,A,C,l
    

#---------------------------------------------------
# İTERASYON VE EN İYİ ÇÖZÜMÜN SEÇİLMESİ
# --------------------
# Tüm popülasyon için gerekli güncellemelerin 
# geçerli iterason sayısına göre yapılması bu 
# kısımda olur.
#
# maxGen maksimum iterasyon sayısını ve P çözüm boyutunu
# ifade eder.
#---------------------------------------------------   

def Iteration(maxGen=30,P=2):
    population = CreatePopulation(NP=30,D=P)
    G_best = population[0].copy()
    G_best_F = -np.inf
    for t in range(maxGen):
        

        b = 1
        
        G_best,G_best_F = Fitnesses(population,G_best,G_best_F)

        for i in range(len(population)):
            p,_,A,C,l = Calc(maxGen,t,P)
            scalar_A = np.linalg.norm(A)
            if p < 0.5:
                if scalar_A<1 :
                    D = np.abs((C*G_best) - population[i])
                    population[i] = G_best - (A*D) 
                else:
                    X_rand = population[np.random.randint(0,len(population))]
                    D = np.abs((C*X_rand) - population[i])
                    population[i] = X_rand - (A*D) 
            else:
                D_prime = np.abs(G_best - population[i])
                population[i] = (D_prime * np.exp(b*l) * np.cos(2 * np.pi * l)) + G_best

                

    print(f'Best condition : {G_best}\n'),
    print(f'Best fitness : {G_best_F}')    
    
Iteration(maxGen=30,P=2)






