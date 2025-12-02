import math
import random
import matplotlib.pyplot as plt

# Seed for reproducibility (optional). Comment out to allow full randomness.
random.seed(42)

size_d = {"alu": (5,5), "cache": (7,4), "control": (4,4), "register": (6,6), "decoder": (5,3), "floating": (5,5)}

def ga(population, iteration=1):
    best = None
    for i in range(iteration):
        fitness = f(population)
        temp, sectemp = find_best(fitness)
        if best is None or (best['fitness'] < temp['fitness']):
            best = temp

        # Pick 4 distinct parents
        r1 = random.randint(0, len(population) - 1)
        r2 = r1
        while r2 == r1:
            r2 = random.randint(0, len(population) - 1)
        r3 = r2
        while r3 == r2 or r3 == r1:
            r3 = random.randint(0, len(population) - 1)
        r4 = r3
        while r4 == r3 or r4 == r2 or r4 == r1:
            r4 = random.randint(0, len(population) - 1)

        p1 = population[r1]
        p2 = population[r2]
        p3 = population[r3]
        p4 = population[r4]

        # Single-point crossover
        point = random.randint(1, len(p1) - 1)
        c1 = p1[0:point] + p2[point::]
        c2 = p2[0:point] + p1[point::]
        c3 = p3[0:point] + p4[point::]
        c4 = p4[0:point] + p3[point::]

        # Mutation
        mutation_rate = 5  # percent
        for c in (c1, c2, c3, c4):
            if random.randint(1, 100) <= mutation_rate:
                idx = random.randint(0, len(c) - 1)
                c[idx] = (random.randint(0, 25), random.randint(0, 25))

        # Elitism: keep the best two from current fitness
        c5 = temp['chromo']
        c6 = sectemp['chromo']
        population = [c1, c2, c3, c4, c5, c6]

    return best


def find_best(fitness_list):
    best = None
    second_best = None
    max_fit = float('-inf')
    second_max_fit = float('-inf')

    for fobj in fitness_list:
        fit = fobj['fitness']
        if fit > max_fit:
            second_best = best
            second_max_fit = max_fit
            best = fobj
            max_fit = fit
        elif fit > second_max_fit:
            second_best = fobj
            second_max_fit = fit

    return best, second_best


def f(population):
    fit = []
    # ALU --> Cache --> Control Unit --> Register File --> Decoder --> Floating Unit
    # size_d reference:
    # {"alu": (5,5), "cache": (7,4), "control": (4,4), "register": (6,6), "decoder": (5,3), "floating": (5,5)}

    for chromo in population:
        items = breakdown(chromo)
        wiring_dist = (
            dist(items, 'register', 'alu') +
            dist(items, 'control','alu') +
            dist(items, 'alu', 'cache') +
            dist(items, 'register', 'floating') +
            dist(items, 'cache', 'decoder') +
            dist(items,'decoder', 'floating')
        )
        area = bounded_area(items)
        overlap = overlap_count(items)
        fitness_value = -((1000 * overlap) + (2 * wiring_dist) + area)

        fit.append({
            "chromo": chromo,
            "fitness": fitness_value,
            "wiring": wiring_dist,
            "area": area,
            "overlap": overlap
        })

    return fit


def overlap_count(items):
    visited = set()
    overlap = 0

    for k1, A in items.items():
        visited.add(k1)
        for k2, B in items.items():
            if k2 in visited:
                continue

            A_left   = min(x for x, y in A)
            A_right  = max(x for x, y in A)
            A_bottom = min(y for x, y in A)
            A_top    = max(y for x, y in A)

            B_left   = min(x for x, y in B)
            B_right  = max(x for x, y in B)
            B_bottom = min(y for x, y in B)
            B_top    = max(y for x, y in B)

            # Rectangles overlap if projections overlap on both axes
            if not (A_right <= B_left or  # A to the left of B
                    A_left >= B_right or   # A to the right of B
                    A_top <= B_bottom or   # A below B
                    A_bottom >= B_top):    # A above B
                overlap += 1

    return overlap


def dist(items, item1, item2):
    bottom_left1 = items[item1][0]
    bottom_right1 = items[item1][1]
    top_left1 = items[item1][2]
    top_right1 = items[item1][3]

    bottom_left2 = items[item2][0]
    bottom_right2 = items[item2][1]
    top_left2 = items[item2][2]
    top_right2 = items[item2][3]

    center1 = (
        bottom_left1[0] + (size_d[item1][0] / 2),
        bottom_left1[1] + (size_d[item1][1] / 2)
    )
    center2 = (
        bottom_left2[0] + (size_d[item2][0] / 2),
        bottom_left2[1] + (size_d[item2][1] / 2)
    )
    euclid = math.sqrt((center1[0]-center2[0])**2 + (center1[1]-center2[1])**2)
    return round(euclid, 2)


def bounded_area(items):
    xs = []
    ys = []
    for corners in items.values():
        for (x, y) in corners:
            xs.append(x)
            ys.append(y)

    x_min = min(xs)
    x_max = max(xs)
    y_min = min(ys)
    y_max = max(ys)

    area = (x_max - x_min) * (y_max - y_min)
    return area


def breakdown(chromo):
    size = [(5,5), (7,4), (4,4), (6,6), (5,3), (5,5)]
    dict1 = {"alu": None, "cache": None, "control": None, "register": None, "decoder": None, "floating": None}
    for i in range(len(chromo)):
        bottom_left = chromo[i]
        bottom_right = (chromo[i][0]+size[i][0], chromo[i][1])
        top_left = (chromo[i][0], chromo[i][1]+size[i][1])
        top_right = (chromo[i][0]+size[i][0], chromo[i][1]+size[i][1])
        dict1[list(dict1.keys())[i]] = (bottom_left, bottom_right, top_left, top_right)
    return dict1


# Initial population (same as provided)
initial_population = [
    [(9,3), (12,15), (13,16), (1,13), (4,15), (9,6)],
    [(8,0), (7,12), (4,11), (1,13), (14,10), (9,11)],
    [(6,5), (12,9), (9,7), (8,6), (2,7), (3,1)],
    [(3,11), (11,12), (14,11), (6,10), (3,11), (3,0)],
    [(10,12), (8,16), (10,4), (13,6), (6,0), (3,7)],
    [(0,2), (0,0), (14,12), (4,5), (12,4), (3,10)]
]


def evaluate_over_intervals(population,
                            start_iter=10,
                            end_iter=300,
                            step=10,
                            runs_per_iter=5):
    """
    Run GA for increasing iteration counts and collect the best fitness.
    To reduce randomness, we run multiple times per iteration and take the best fitness of those runs.

    Returns:
        iter_counts: list of iteration counts tested
        best_fitnesses: list of best fitness values (one per iteration count)
    """
    iter_counts = []
    best_fitnesses = []

    for iters in range(start_iter, end_iter + 1, step):
        iter_counts.append(iters)

        # Run multiple times to mitigate randomness; take the best fitness across runs
        best_fit_for_iters = float('-inf')
        for _ in range(runs_per_iter):
            # Copy the population so runs don't interfere with each other
            pop_copy = [chromo.copy() for chromo in population]
            result = ga(pop_copy, iteration=iters)
            if result['fitness'] > best_fit_for_iters:
                best_fit_for_iters = result['fitness']

        best_fitnesses.append(best_fit_for_iters)

    return iter_counts, best_fitnesses


def main():
    # Configuration: adjust as needed
    start_iter = 10     # starting iteration count
    end_iter = 500      # ending iteration count
    step = 10           # interval step size
    runs_per_iter = 5   # number of GA runs per iteration count (to reduce noise)

    iter_counts, best_fitnesses = evaluate_over_intervals(
        initial_population,
        start_iter=start_iter,
        end_iter=end_iter,
        step=step,
        runs_per_iter=runs_per_iter
    )

    # Plot fitness vs iterations
    plt.figure(figsize=(10, 6))
    plt.plot(iter_counts, best_fitnesses, marker='o', linestyle='-', color='tab:blue', label='Best fitness')
    plt.title('GA Fitness Trend vs Iterations')
    plt.xlabel('Iterations')
    plt.ylabel('Best Fitness (higher is better)')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Optionally print the final best result for the maximum iteration
    print(f"Max iterations tested: {end_iter}")
    print(f"Best fitness at max iterations: {best_fitnesses[-1]:.2f}")


if __name__ == "__main__":
    main()