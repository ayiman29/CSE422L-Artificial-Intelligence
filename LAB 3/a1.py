def utility(genes, target, id):
    N = max(len(genes), len(target))
    weights = id[-len(target):]
    sum = 0
    for i in range(N):
        if i <= (len(weights) - 1):
            weight = weights[i]
        else:
            weight = 1
        if i <= (len(genes) -1):
            gene = genes[i]
        else:
            gene = 0
        if i <= (len(target) -1):
            tar = target[i]
        else:
            tar = 0
        print(weight, ord(gene), ord(tar))
        sum += (weight * abs(ord(gene) - ord(tar)))
    return -sum

def minimax(pool, gene, a, b, isMax):
    if len(pool) == 0:
        return gene, utility(gene, target, id)
    
    if isMax:
        v = float("-inf")
        for child in pool:
            temp = pool.copy()
            temp.remove(child)
            s, util= minimax(temp, gene+child, a, b, False)
            if v < util:
                v = util
                best_gene = s
            a = max(a, v)
            if b <= a:
                break
        return best_gene, v
    else:
        v = float("inf")
        for child in pool:
            temp = pool.copy()
            temp.remove(child)
            s, util= minimax(temp, gene+child, a, b, True)
            if v > util:
                v = util
                best_gene = s
            a = max(a, v)
            if b <= a:
                break
        return best_gene, v







pool = ["A", "T", "C", "G"]
target = "ATGC"
id = [1, 8, 1, 0, 4, 0, 5, 2]
pool = input().strip().split(",")
target = input().strip()
id = input().strip().replace(" ", "")
id = [int(x) for x in id]

best_gene, score = minimax(pool, "", float("-inf"), float("inf"), True)


print("Best gene sequence generated:", best_gene)
print("Utility score:", score)