import itertools

def generate_permutations(count):
    return list(itertools.permutations([1, 2, 3, 4, 5, 6], count))


if __name__ == "__main__":
    result = generate_permutations(2)

    with open('Out/perm-2.txt', 'w') as f:
        for x in result:
            print(x)
            f.write(' '.join(str(s) for s in x) + '\n')