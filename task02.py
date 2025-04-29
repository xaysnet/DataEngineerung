from collections.abc import Sequence

def check_fibonacci(data: Sequence[int]) -> bool:
    return len(data) < 3 or all(data[i] == data[i - 1] + data[i - 2] for i in range(2, len(data)))

if __name__ == "__main__":
    sequences = [
        [0, 1, 1, 2, 3, 5, 8],
        [3, 5, 8, 13, 21],
        [1, 2, 4, 7, 11],
        [7],
        []
    ]

    for seq in sequences:
        print(f"Последовательность {seq} является Фибоначчи: {check_fibonacci(seq)}")