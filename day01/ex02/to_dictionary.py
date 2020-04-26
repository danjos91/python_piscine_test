def main():
    list_of_tuples = [("Russia", "25"),("France","132"),("Germany", "132"), ("Spain", "178"), ("Italy", "162"), ("Portugal", "17"), ("Finland", "3"), ("Hungary", "2"), ("The Nehterlands", "28"), ("The USA", "610"), ("The United Kingdom", "95"), ("China", "83"), ("Iran", "76"), ("Turkey", "65"), ("Belgium", "34"), ("Canada", "28"), ("Switzerland", "26"), ("Brazil", "25"), ("Austria", "14"), ("Israel", "12")]
    swapped = [(item[1], item[0]) for item in list_of_tuples]
    dictionary = dict(swapped)
    print(str(dictionary).replace("'", "\"").replace(",", "\n").replace("{", "").replace("}", ""))

if __name__ == '__main__':
    main()
