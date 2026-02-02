#!/usr/bin/env python3

import sys


def ft_inventory_system() -> None:
    if len(sys.argv) < 2:
        return
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = {}
    for items in sys.argv[1:]:
        name_and_quantity = items.split(":")
        inventory[name_and_quantity[0]] = int(name_and_quantity[1])
    total = sum(inventory.values())
    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {len(inventory)}")

    print("\n=== Current Inventory ===")
    sorted_inventory = sorted(
        inventory.items(), key=lambda x: x[1], reverse=True)
    for key, value in sorted_inventory:
        print(f"{key}: {value} ({value / total * 100:.1f}%)")

    print("\n=== Inventory Statistics ===")
    maxi = max(inventory, key=inventory.get)
    mini = min(inventory, key=inventory.get)
    print(f"Most abundant: {maxi} ({inventory[maxi]})")
    print(f"Least abundant: {mini} ({inventory[mini]})")

    print("\n=== Item Categories ===")
    moderate_items = {k: v for k, v in inventory.items() if v > 4}
    print(f"Moderate: {moderate_items}")
    scarce_items = {k: v for k, v in inventory.items() if v <= 3}
    print(f"Scarce: {scarce_items}")

    print("\n=== Management Suggestions ===")
    restock_needed = [k for k, v in inventory.items() if v < 2]
    print(f"Restock needed: {restock_needed}")

    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {list(inventory.keys())}")
    print(f"Dictionary values: {list(inventory.values())}")
    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory} ")


if __name__ == "__main__":
    ft_inventory_system()
