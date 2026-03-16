def main():
    print("Hello from cvicenie6!")


if __name__ == "__main__":
    main()

def basic_stats(values):
    return min(values), max(values), round(sum(values) / len(values), 2)


min_v, max_v, avg_v = basic_stats([1200, 980, 1430, 1600, 890])
print(min_v, max_v, avg_v)

