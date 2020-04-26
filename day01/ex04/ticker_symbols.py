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

    new_list = list(companies.items())
    out = [item for t in new_list for item in t]
    valid_names = list(stocks)
    if value in valid_names:
        company_name = out[out.index(value) - 1]
        company_value= stocks[value]
        print(company_name, company_value, sep=" ")

if __name__=='__main__':
    main()
