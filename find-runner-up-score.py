if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    # runner-up score
    remove_duplicates = set(arr)
    sorted_scores = sorted(remove_duplicates)
    runner_up = sorted_scores[-2]
    print(runner_up)


