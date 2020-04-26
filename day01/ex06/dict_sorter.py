def main():

    list_of_tuples = [("Russia", "25"),("France","132"),("Germany", "132"), ("Spain", "178"), ("Italy", "162"), ("Portugal", "17"), ("Finland", "3"), ("Hungary", "2"), ("The Nehterlands", "28"), ("The USA", "610"), ("The United Kingdom", "95"), ("China", "83"), ("Iran", "76"), ("Turkey", "65"), ("Belgium", "34"), ("Canada", "28"), ("Switzerland", "26"), ("Brazil", "25"), ("Austria", "14"), ("Israel", "12")]
    dict_countries = dict(list_of_tuples)
    countries_and_numbers = [item for t in list_of_tuples for item in t]
    countries_and_numbers_reverse = countries_and_numbers
    countries_and_numbers_reverse.reverse()
    numbers = []
    for (m,n) in dict_countries.items():
        numbers.append(int(n))
    numbers.sort()
    numbers.reverse()
    countries_and_numbers = [item for t in list_of_tuples for item in t]
    for i in range(len(numbers)):
        if str(numbers[i]) in countries_and_numbers:
            if i != len(numbers)-1 and numbers[i] == numbers[i + 1]:
                same_numbers = []
                index_country = countries_and_numbers.index(str(numbers[i])) - 1
                same_numbers.append(countries_and_numbers[index_country])
                index_country = countries_and_numbers_reverse.index(str(numbers[i])) + 1
                same_numbers.append(countries_and_numbers_reverse[index_country])
                same_numbers.sort()
                for l in same_numbers:
                    print(l)
            elif numbers[i] != numbers[i-1]:
                index_country = countries_and_numbers.index(str(numbers[i])) - 1
                print(countries_and_numbers[index_country])



if __name__ == '__main__':
    main()
