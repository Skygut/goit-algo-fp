import matplotlib.pyplot as plt
import numpy as np


def draw_pythagoras_tree(recursion_depth):
    def draw_branch(x, y, angle, depth):
        if depth > 0:
            branch_length = depth**0.7
            new_x = x + np.cos(angle) * branch_length
            new_y = y + np.sin(angle) * branch_length

            plt.plot([x, new_x], [y, new_y], "brown")
            new_angle1 = angle - np.pi / 4
            new_angle2 = angle + np.pi / 4

            draw_branch(new_x, new_y, new_angle1, depth - 1)
            draw_branch(new_x, new_y, new_angle2, depth - 1)

    plt.figure(figsize=(8, 8))
    plt.title(f"Дерево Піфагора з рекурсією {recursion_depth}")
    plt.axis("off")

    x, y, angle = 0, 0, np.pi / 2

    draw_branch(x, y, angle, recursion_depth)

    plt.show()


def main():
    try:
        recursion_level = int(input("Введіть рівень рекурсії для Дерева Піфагора: "))
        draw_pythagoras_tree(recursion_level)
    except ValueError:
        print("Помилка: Будь ласка, введіть ціле число.")


if __name__ == "__main__":
    main()
