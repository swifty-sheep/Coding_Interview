def sum_of_mult_of_3_or_5(k: int = 1000):
    total_sum = 0
    for i in range(1, k):
        if i % 3 == 0 or i % 5 == 0:
            # print(i)
            total_sum += i

    return total_sum


def main():
    ans = sum_of_mult_of_3_or_5(k=1000)
    print(ans)
    ans = sum_of_mult_of_3_or_5(k=10)
    print(ans)


# Driver Code
if __name__ == "__main__":
    main()
