import itertools

def generate_permutations(count):
    return list(itertools.combinations_with_replacement([1, 2, 3, 4, 5, 6], count))


if __name__ == "__main__":
    result = generate_permutations(20)
    print(len(result))


    # with open('Out/perm-2.txt', 'w') as f:
    #     for x in result:
    #         f.write(' '.join(str(s) for s in x) + '\n')