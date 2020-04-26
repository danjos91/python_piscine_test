import sys

def dict_to_lower(original_dict):
    dict_lower = {}
    for (k, v) in original_dict.items():
        dict_lower[str(k).lower()] = str(v).lower()
    return(dict_lower)

def main():

    if len(sys.argv) != 2:
        return "\n"
    else:
        values_original_txt = str(sys.argv[1]).replace(" ", "")
        values_original_list= values_original_txt.split(",")
        values = values_original_txt.lower().split(",")
        for i in values:
            if i == "":
                return("\n")

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

    companies_lower_keys = list(dict_to_lower(companies))
    stocks_lower_keys = list(dict_to_lower(stocks))
    companies_keys = list(companies)
    stocks_keys = list(stocks)
    for i in range(len(values)):
        if values[i] in companies_lower_keys:
            ind = companies_lower_keys.index(values[i])#index of our name in the list with original names
            original_value = companies_keys[ind]
            stock_price = stocks[companies[original_value]]
            print(original_value, "stock price is", stock_price, sep=" ")
        elif values[i] in stocks_lower_keys:
            comp_and_tick = [item for t in companies.items() for item in t]
            ind = stocks_lower_keys.index(values[i])#index of our name in the list with original names
            original_value = stocks_keys[ind]
            company_name= comp_and_tick[comp_and_tick.index(original_value) - 1]
            print(original_value, "is a ticker symbol for", company_name, sep=" ")
        else:
            print(values_original_list[i] + " is an unknown company or an unknown ticker symbol")

if __name__=='__main__':
    main()
