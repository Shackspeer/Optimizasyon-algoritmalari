import numpy as np



NP = 20  # Popülasyon büyüklüğü
D = 2 # Vektör boyutu
F = 0.5 # Ölçekleme Faktörü
CR  = 0.6 # Çaprazlama olasılığı
Gmax = 10 # Maximum iterasyon sayısı
Lower = -5
Upper = 5
M_population = []



def FitnessFunction(x,y):
    
    f = (x**2 - 9) + (y**3 - 8)
        
    return f


    


def CreatePopulation(): # D boyutunda NP adet populasyon oluştur
    population = []
    for i in range(1,NP+1):
        i = np.random.uniform(Lower,Upper,4)
        population.append(i)
    return population



def Mutation(population):
    tempArray = []
    NP = len(population)
    for x in range(NP):
        condidates = list(range(NP))
        condidates.remove(x)
        r1,r2,r3 = np.random.choice(condidates,3,replace=False)
        v = population[r1] + F*(population[r2]-population[r3])
        tempArray.append(v)
    return np.array(tempArray)


def Crossover(population,M_population,CR,NP,D):
    trial_population = np.zeros((NP,D))
    for i in range(NP):
        randValues = np.random.rand(D)
        print(randValues)
        j_Rand = np.random.randint(0,D)
        for j in range(D):
            if randValues[j] <= CR or j == j_Rand:
                trial_population[i][j] = M_population[i][j]
            else:
                trial_population[i][j] = population[i][j]
    return trial_population


def Selection(population,trial_population,NP,D):

    new_population = np.zeros((NP,D))

    for i in range(NP):
        old_fitness = FitnessFunction(population[i][0],population[i][1])
        trial_fitness = FitnessFunction(trial_population[i][0],trial_population[i][0])

        if old_fitness > trial_fitness:
            new_population[i] = trial_population[i]
        else:
            new_population[i] = population[i]
    
    return new_population

population = CreatePopulation()
M_population = Mutation(population)
trial_population = Crossover(population,M_population,CR,NP,D)




'''
for x in population:
    print(x)
print("\nMutation values:\n\n")
for m in M_population:
    print(m)
print("\nTrial values:\n\n")
for t in trial_population:
    print(t)
print("\n New population :\n\n")

'''
for x in population:
    print(x)
print("\nMutation values:\n\n")
for m in M_population:
    print(m)
print("\nTrial values:\n\n")
for t in trial_population:
    print(t)
print("\n New population :\n\n")
for s in Selection(population,trial_population,NP,D):
    print(s)

