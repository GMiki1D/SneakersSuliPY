import csv


def read_sneakers_csv():
    sneakers = []
    with open('sneakers.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            sneakers.append(row)
    return sneakers


def display_sneakers(sneakers):
    for sneaker in sneakers:
        print(f"Title: {sneaker['title']}")
        print(f"Color: {sneaker['color_breif']}")
        print(f"Full Price: ${sneaker['fullPrice']}")
        print(f"Current Price: ${sneaker['currentPrice']}")
        print(f"Publish Date: {sneaker['publish_date']}\n")


def sort_sneakers(sneakers, key):
    return sorted(sneakers, key=lambda x: x[key])


def main():
    while True:
        print("1 - title")
        print("2 - color")
        print("3 - full price")
        print("4 - current price")
        print("5 - publish date\n")
        choice = input("Válassz, melyik szempont alapján rendezzem a cipőket:\t")
        sneakers = read_sneakers_csv()
        if choice == '1':
            sorted_sneakers = sort_sneakers(sneakers, 'title')
        elif choice == '2':
            sorted_sneakers = sort_sneakers(sneakers, 'color')
        elif choice == '3':
            sorted_sneakers = sort_sneakers(sneakers, 'fullPrice')
        elif choice == '4':
            sorted_sneakers = sort_sneakers(sneakers, 'currentPrice')
        elif choice == '5':
            sorted_sneakers = sort_sneakers(sneakers, 'publish_date')
        else:
            print("Adj meg egy számot egytől ötig!")
            return

        print("A rendezett cipők:\n")
        display_sneakers(sorted_sneakers)
        again = input("Szeretnéd a listát újrarendezni? (I/N)")
        if again == "I":
            True
        else:
            print("Rendben! Remélem egyszer még vissza térsz cipőket nézegetni!")
            break




main()
