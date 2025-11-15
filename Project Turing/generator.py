import random
import sys

def generate_test_case(n, max_weight=100, seed=None):
    """Generate a random test case"""
    if seed:
        random.seed(seed)
    
    # Generate weights
    weights = [random.randint(1, max_weight) for _ in range(n)]
    
    # Generate tree edges
    edges = []
    for i in range(2, n + 1):
        parent = random.randint(1, i - 1)
        edges.append((parent, i))
    
    # Choose reasonable T and K values
    total_sum = sum(weights)
    avg_component_size = max(1, total_sum // max(1, n // 3))  # Aim for ~3 components
    
    T = avg_component_size
    K = max(1, T // 4)  # Allow 25% tolerance
    
    return n, T, K, weights, edges

def write_test_case(filename, n, T, K, weights, edges):
    """Write test case to file"""
    with open(filename, 'w') as f:
        f.write(f"{n} {T} {K}\n")
        f.write(" ".join(map(str, weights)) + "\n")
        for u, v in edges:
            f.write(f"{u} {v}\n")

if __name__ == "__main__":
    # Generate additional test cases
    test_cases = [
        (10, 50, 42),   # Medium tree
        (15, 30, 123),  # Larger tree
        (8, 20, 456),   # Small tree with specific seed
    ]
    
    for i, (n, max_w, seed) in enumerate(test_cases, 6):
        n, T, K, weights, edges = generate_test_case(n, max_w, seed)
        write_test_case(f"test_cases/{i}.in", n, T, K, weights, edges)
        print(f"Generated test case {i}: n={n}, T={T}, K={K}")
        print(f"Weights: {weights}")
        print(f"Edges: {edges}")
        print()
