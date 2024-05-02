"""
|| HackerRank
    Problem: Priyanka and Toys 
    Level: Easy
    Author: amititkgp
    Implementation: Eugene (apexDev37) & Ndeda (ndedakaduki)
"""

# This is the main entry point function to complete
# on the HackerRank platform. 
# Rename as per specified

def toys(shipping_items: list[int]) -> int:
    sorted_shipping_items = sorted(shipping_items)

    current_min: int = 0
    containers: int = 0
    for item in sorted_shipping_items:
        if not current_min or item > current_min:
            current_min = item + 4
            containers += 1
    return containers 


def main() -> int:
    shipping_items: list[int] = [1, 2, 3, 4, 5, 10, 11, 12, 13]
    number_of_containers = toys(shipping_items=shipping_items)
    print(number_of_containers)


if __name__ == "__main__":
    main()
