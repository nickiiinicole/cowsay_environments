import cowsay

def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def main():
    number = int(input("Introduce un número: "))
    if is_prime(number):
        cowsay.cow(f"O número {number} é primo!")
    else:
        cowsay.cow(f"O número {number} non é primo!")


if __name__ == "__main__":
    main()
