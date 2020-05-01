import requests
import sys
from bs4 import BeautifulSoup

def get_soup(ticker):
    adress =  "https://finance.yahoo.com/quote/" + ticker + "/financials?p=" + ticker
    page = requests.get(adress)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

def elements_in_row(row_in_table, parameter):
    element = 0
    for i in row_in_table:
        if list(i)[0].get_text() == parameter:
            element =list(i.children)
    return element

def main():
    if len(sys.argv) != 3:
        print("Wrong number of arguments, please check")
        return
    ticker = sys.argv[1]
    parameter = sys.argv[2]
    result = []
    soup = get_soup(ticker)
    row_in_table = soup.find_all('div', class_="D(tbr)")#if the program does not found anything, so the ticker is wrong
    if not row_in_table:
        print("Wrong ticker, please check")
        return
    elements = elements_in_row(row_in_table, parameter)
    if not elements:
        print("Wrong parameter, please check")
        return
    else:
        for i in elements:
            result.append(i.get_text())
    result = tuple(result)
    print(result)

if __name__ == '__main__':
    main()
