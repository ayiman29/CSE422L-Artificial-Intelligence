import random
import time
def ga(target, population, chars):
    gen = 0
    li = []
    while True:
        '''
        if gen == 10:
            print("BEYOND REACH. GIVING UP.")
            return 0
        '''
        gen += 1
        list1 = []
        for i in range(len(population)):
            temp = fitness(population[i], target)
            list1.append((temp, i))
        list1 = list(reversed(sorted(list1)))
        p1 = population[list1[0][1]]
        p2 = population[list1[1][1]]
        p3 = population[list1[2][1]]
        p4 = population[list1[3][1]]
        if gen == 1:
            li.append((p1, p2, p3, p4))
        sp = random.randint(1, len(population[0]) - 1)
        print("======================================")
        print("Parent 1:", p1)
        print("Parent 2:", p2)
        print("Parent 3:", p3)
        print("Parent 4:", p4)
        print("Target:", target)
        print("======================================")
        if target in population:
            print("FOUND PARENT:", p1, "IN GEN:", gen)
            print("Parents of the First Generation:", li)
            return 1
        c1 = p1[:sp] + p2[sp:]
        c2 = p2[:sp] + p1[sp:]
        c3 = p3[:sp] + p4[sp:]
        c4 = p4[:sp] + p3[sp:]
        rate = 5
        if random.random() < rate / 100:
            ran = random.randint(0, len(c2) - 1)
            c2 = c2[:ran] + chr(random.choice(chars)) + c2[ran+1:]
        if random.random() < rate / 100:
            ran = random.randint(0, len(c3) - 1)
            c3 = c3[:ran] + chr(random.choice(chars)) + c3[ran+1:]

        population = [p1, p2, p3, p4] + population[:42] + [c1, c2, c3, c4]



def fitness(chrom, target):
    score = 0
    for c, t in zip(chrom, target):
        if c == t:
            score += 2
        elif c.lower() == t.lower():
            score += 1
    return score






target = input()

chars = (
    list(range(65, 91)) +
    list(range(97, 123)) +
    list(range(48, 58)) +
    [32]
)
population = []
for i in range(50):
    temp = ""
    for j in range(len(target)):
        temp += chr(random.choice(chars))
    population.append(temp)
start = time.time()
ga(target, population, chars)
end = time.time()
print("Time taken:", end - start, "seconds")
