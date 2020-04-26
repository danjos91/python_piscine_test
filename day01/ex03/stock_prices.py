import sys

def main():

    if len(sys.argv) != 2:
        return ""
    else:
        value = str(sys.argv[1])

    companies = {"Apple" : "AAPL",
    "Microsoft" : "MSFT",
    "Netflix" : "NFLX",
    "Tesla" : "TSLA",
    "Nokia" : "NOK"
     }

    stocks = {
         "AAPL" : 287.73,
         "MSFT" : 173.79,
         "NFLX" : 416.90,
         "TSLA" : 724.88,
         "NOK" : 3.37
    }
    if value in companies:
        print(stocks[companies[value]])
    else:
        print("Unknow company")


if __name__ == '__main__':
    main()


