import sys


def main():
    if "--help" in sys.argv or "-h" in sys.argv:
        print("Використання: python src/sys_tool.py")
        print("Сценарій демонструє запуск через командний рядок.")
        return

    print("командна строка")


if __name__ == "__main__":
    main()