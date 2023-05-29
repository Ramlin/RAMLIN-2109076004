import random

# Fungsi objektif
def fitness(chromosome):
    a, b, c, d = chromosome
    return abs(a + 4*b + 2*c + 3*d - 30)

# Inisialisasi populasi
def initialize_population(population_size):
    population = []
    for _ in range(population_size):
        chromosome = [random.randint(0, 30), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)]
        population.append(chromosome)
    return population

# Seleksi orang tua menggunakan metode roulette wheel selection
def select_parents(population):
    total_fitness = sum(fitness(chromosome) for chromosome in population)
    probabilities = [fitness(chromosome) / total_fitness for chromosome in population]
    cumulative_probabilities = [sum(probabilities[:i+1]) for i in range(len(probabilities))]

    parents = []
    for _ in range(len(population)):
        r = random.random()
        for i, chromosome in enumerate(population):
            if cumulative_probabilities[i] > r:
                parents.append(chromosome)
                break

    return parents

# Crossover menggunakan one-cut point
def crossover(parents, crossover_rate):
    offspring = []
    for i in range(0, len(parents), 2):
        parent1 = parents[i]
        parent2 = parents[i+1]
        if random.random() < crossover_rate:
            cut_point = random.randint(1, 3)  # Memilih titik potong dari 1 hingga 3
            child1 = parent1[:cut_point] + parent2[cut_point:]
            child2 = parent2[:cut_point] + parent1[cut_point:]
        else:
            child1 = parent1
            child2 = parent2
        offspring.extend([child1, child2])
    return offspring

# Mutasi
def mutate(offspring, mutation_rate):
    total_genes = len(offspring) * 4
    num_mutations = int(total_genes * mutation_rate)

    for _ in range(num_mutations):
        chromosome = random.choice(offspring)
        gene_index = random.randint(0, 3)
        chromosome[gene_index] = random.randint(0, 30) if gene_index == 0 else random.randint(0, 10)

# Algoritma genetika
def genetic_algorithm(population_size, crossover_rate, mutation_rate, num_generations):
    population = initialize_population(population_size)

    for _ in range(num_generations):
        parents = select_parents(population)
        offspring = crossover(parents, crossover_rate)
        mutate(offspring, mutation_rate)

        population = offspring

    # Mengembalikan chromosome dengan fitness terbaik
    best_chromosome = min(population, key=fitness)
    return best_chromosome

# Pengaturan parameter
population_size = 6
crossover_rate = 0.8
mutation_rate = 0.1
num_generations = 100

# Menjalankan algoritma genetika
best_chromosome = genetic_algorithm(population_size, crossover_rate, mutation_rate, num_generations)

# Menampilkan hasil
a, b, c, d = best_chromosome
print("Nilai a:", a)
print("Nilai b:", b)
print("Nilai c:", c)
print("Nilai d:", d)
print("Fungsi Objektif:", fitness(best_chromosome))
