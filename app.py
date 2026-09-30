def add(a, b):
    return a + b


def is_even(n):
    return n % 2 == 0


if __name__ == "__main__":
    html = (
        f"<h1>CI/CD Demo</h1>"
        f"<p>add(2, 3) = {add(2, 3)}</p>"
        f"<p>is_even(4) = {is_even(4)}</p>"
    )
    with open("site/index.html", "w", encoding="utf-8") as file:
        file.write(html)
