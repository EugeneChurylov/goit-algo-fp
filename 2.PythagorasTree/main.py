import turtle


def draw_pifagor_tree(branch_length, t, recursion_level):
    if recursion_level == 0:
        return
    else:
        t.forward(branch_length)
        t.left(45)
        draw_pifagor_tree(branch_length * 0.7, t, recursion_level - 1)
        t.right(90)
        draw_pifagor_tree(branch_length * 0.7, t, recursion_level - 1)
        t.left(45)
        t.backward(branch_length)

def main():
    # Введення рівня рекурсії від користувача
    recursion_level = int(input("Введіть рівень рекурсії: "))

    # Налаштування вікна для візуалізації
    screen = turtle.Screen()
    screen.bgcolor("white")

    # Створення дерева
    t = turtle.Turtle()
    t.pos()
    t.speed(10000)
    t.color("green")
    t.left(90)
    t.penup()
    t.goto(0, -250)
    t.pendown()
    t.color("red")

    # Виклик функції для малювання дерева Піфагора
    draw_pifagor_tree(200, t, recursion_level)

    # Закриття вікна при кліку
    screen.exitonclick()

if __name__ == "__main__":
    main()
