import sys

def main():
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }

    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }

    string = sys.argv[1]
    args = string.split(',')
    
    for arg in args:
        if arg.strip() == '':
            sys.exit()
    
    print(args)
    for arg in args:
        is_exist = False
        for key, value in COMPANIES.items():
            if arg.capitalize().strip() == key:
                is_exist = True
                print(f'{key} stock price is {STOCKS[COMPANIES[key]]}')  

        for key, value in STOCKS.items():
            if arg.upper().strip() == key:
                for k, v in COMPANIES.items():
                    if key == v:
                        is_exist = True
                        print(f'{arg.upper().strip()} is a ticker symbol for {k.strip()}')
                        
        if is_exist == False:
            print (f'{arg} is an unknown company or an unknown ticker symbol')
            is_exist = False

if __name__ == "__main__":
    main()
             