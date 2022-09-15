import typer
from rich import print

app = typer.Typer()


def main(name: str):
    print(f"Hello {name}")


if __name__ == "__main__":
    typer.run(main)

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
