import numpy as np

# Parametreler
NP = 20          # Popülasyon sayısı
D = 2            # Değişken sayısı
F = 0.6          # Mutasyon ölçekleme faktörü
CR = 0.65        # Çaprazlama oranı
Gmax = 20         # Maksimum iterasyon
Lower = -20       # Alt sınır
Upper = 20        # Üst sınır


# ------------------------------------------------------
#  Amaç ve Fitness Fonksiyonları
# ------------------------------------------------------
def CostFunction(vec):
    x, y = vec
    return (x - 3)**2 + (y - 1)**2

def FitnessFunction(vec):
    cost = CostFunction(vec)
    return 1 / (1 + cost)


# ------------------------------------------------------
#  Başlangıç Popülasyonu
# ------------------------------------------------------
def CreatePopulation(NP, D, Lower, Upper):
    return np.random.uniform(Lower, Upper, (NP, D))


# ------------------------------------------------------
#  Mutasyon
# ------------------------------------------------------
def Mutation(population, F):
    NP = len(population)
    mutants = np.zeros_like(population)

    for i in range(NP):
        idxs = [idx for idx in range(NP) if idx != i]
        r1, r2, r3 = np.random.choice(idxs, 3, replace=False)

        mutants[i] = population[r1] + F * (population[r2] - population[r3])

    return mutants


# ------------------------------------------------------
#  Çaprazlama
# ------------------------------------------------------
def Crossover(population, mutants, CR):
    NP, D = population.shape
    trial = np.zeros_like(population)

    for i in range(NP):
        j_rand = np.random.randint(0, D)
        for j in range(D):
            if np.random.rand() <= CR or j == j_rand:
                trial[i, j] = mutants[i, j]
            else:
                trial[i, j] = population[i, j]

    return trial


# ------------------------------------------------------
#  Seleksiyon
# ------------------------------------------------------
def Selection(population, trial):
    NP = len(population)
    new_population = np.zeros_like(population)

    for i in range(NP):
        if FitnessFunction(trial[i]) > FitnessFunction(population[i]):
            new_population[i] = trial[i]
        else:
            new_population[i] = population[i]

    return new_population


# ------------------------------------------------------
#  Ana Döngü
# ------------------------------------------------------
def DifferentialEvolution(NP, D, Gmax, F, CR, Lower, Upper):

    population = CreatePopulation(NP, D, Lower, Upper)

    for gen in range(Gmax):
        mutants = Mutation(population, F)
        trial = Crossover(population, mutants, CR)
        population = Selection(population, trial)

    print("\nFinal Popülasyon:")
    for vec in population:
        print(vec, " fitness=", round(FitnessFunction(vec), 6))


# ------------------------------------------------------
# Çalıştır
# ------------------------------------------------------
DifferentialEvolution(NP, D, Gmax, F, CR, Lower, Upper)
