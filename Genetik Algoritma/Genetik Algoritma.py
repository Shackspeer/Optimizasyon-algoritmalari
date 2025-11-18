import math
import random

# === Beale Fonksiyonu ===
def BealeFunction(x, y):
    return (((1.5 - x + (x * y)) ** 2) +
            ((2.25 - x + (x * (y ** 2))) ** 2) +
            ((2.625 - x + (x * (y ** 3))) ** 2))

# === Popülasyon oluşturma ===
def CreatePopulation(nums, size=128):
    for _ in range(size):
        nums.append([
            round(random.uniform(-10, 10), 2),
            round(random.uniform(-10, 10), 2)
        ])

# === Fitness hesaplama (1 / (1 + f(x,y))) ===
def CalcFitness(nums):
    tempArray = []
    for i in nums:
        if i is not None:
            f_val = BealeFunction(i[0], i[1])
            fitness = round(1 / (1 + f_val), 6)  # 1 / (1 + f(x,y))
            tempArray.append([i[0], i[1], fitness])
    return tempArray

# === Ebeveyn seçimi (en iyi iki birey) ===
def ParentSelection(fitnesses):
    sorted_list = sorted(fitnesses, key=lambda x: x[2], reverse=True)  # fitness büyük olan önce
    parent1 = sorted_list[0]
    parent2 = sorted_list[1]

    fitnesses.remove(parent1)
    fitnesses.remove(parent2)
   
    return parent1, parent2

# === Çaprazlama (2 çocuk üretir) ===
def Crossover(parrents):
    childs = []
    for p1, p2 in parrents:
        # Çocuk 1
        new_x1 = round(p1[0] * 0.5 + p2[0] * 0.5, 3)
        new_y1 = round(p1[1] * 0.5 + p2[1] * 0.5, 3)

        # Çocuk 2 (farklı ağırlıkla)
        new_x2 = round(p1[0] * 0.7 + p2[0] * 0.3, 3)
        new_y2 = round(p1[1] * 0.7 + p2[1] * 0.3, 3)

        childs.append([new_x1, new_y1])
        childs.append([new_x2, new_y2])
    return childs

# === Random Resetting / Gaussian Mutasyonu ===
def Mutation(population, mutation_rate=0.1, key=1, sigma=0.3):
    if key == 1:
        for i in range(len(population)):
            if random.random() < mutation_rate:
                gen_index = random.randint(0, 1)
                old_value = population[i][gen_index]
                population[i][gen_index] = round(random.uniform(-10, 10), 2)
                print(f"Mutasyon: birey {i}, gen {gen_index}, eski={old_value}, yeni={population[i][gen_index]}")
        return population
    elif key == 2:
        for i in range(len(population)):
            if random.random() < mutation_rate:
                gen_index = random.randint(0, 1)
                old_value = population[i][gen_index]
                new_value = old_value + random.gauss(0, sigma)
                new_value = max(min(new_value, 10), -10)
                population[i][gen_index] = round(new_value, 3)
                print(f"Gauss Mutasyon: birey {i}, gen {gen_index}, eski={old_value}, yeni={population[i][gen_index]}")
        return population

# === Accuracy hesaplama (fitness ile aynı mantıkta) ===
def Accuracy_by_function(x, y):
    f_val = BealeFunction(x, y)
    return round(1 / (1 + f_val), 6)
def Accuracy_by_distance(x, y):
    global_min = [3, 0.5]
    distance = math.sqrt((x - global_min[0])**2 + (y - global_min[1])**2)
    return round(1 / (1 + distance), 6)
# === Döngü başlatma ===
def StartLoop(child, epoch=5):
    bestFitness = None
    for e in range(epoch):
        print(f"\n=== EPOCH {e+1} ===")
        numsWithFitness = CalcFitness(child)
       
        parrents = []
        for _ in range(len(numsWithFitness) // 2):
            p1, p2 = ParentSelection(numsWithFitness)
            parrents.append([p1, p2])

        childs = Crossover(parrents)
        childs = Mutation(childs, mutation_rate=0.1, key=2)

        # En iyi bireyi seç (fitness büyük olan)
        best = max(CalcFitness(childs), key=lambda x: x[2])
        if bestFitness is None or best[2] > bestFitness[2]:
            bestFitness = best

        print(f"En iyi birey: {best}, Fitness-Accuracy: {Accuracy_by_function(best[0], best[1])}, "
              f"Distance-Accuracy: {Accuracy_by_distance(best[0], best[1])}")

        child = childs

    print(f"\n=== Genel En İyi ===")
    print(f"Best fitness value : {bestFitness[2]}")
    print(f"Best individual : X --> {bestFitness[0]} , Y -- > {bestFitness[1]}")
    print(f"Fitness-temelli accuracy : {Accuracy_by_function(bestFitness[0], bestFitness[1])*100:.4f}%")
    print(f"Nokta-temelli accuracy : {Accuracy_by_distance(bestFitness[0], bestFitness[1])*100:.4f}%")
# === Program Başlangıcı ===
randNums = []
CreatePopulation(randNums)
numsWithFitness = CalcFitness(randNums)

parrents = []
for _ in range(4):
    p1, p2 = ParentSelection(numsWithFitness)
    parrents.append([p1, p2])

childs = Crossover(parrents)
childs = Mutation(childs, key=2)  # ilk nesle mutasyon

StartLoop(childs, epoch=50)
