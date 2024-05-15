import numpy as np


def generate_random_matrix(rows, cols):

    return np.random.rand(rows,cols)


def calculate_statistics(matrix):
    stats = {}

    stats['mean'] = np.mean(matrix)
    stats['std_dev'] = np.std(matrix)
    stats['variance'] = np.var(matrix)

    return stats

def main():
    rows = int(input("enter the number of rows: "))
    cols = int(input("enter the number of columns: "))

    matrix = generate_random_matrix(rows,cols)

    stats = calculate_statistics(matrix)

    print("\nstatistics:")
    print("mean: ", stats['mean'])
    print("standard deviation: ", stats['std_dev'])
    print("variance",stats['variance'])

if __name__ == "__main__":
    main()