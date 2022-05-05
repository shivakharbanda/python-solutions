import sys
import requests

def main():
    bitcoin_count = get_bitcoin_count()
    bitcoin_rate = bitcoin_rate_in_usd()
    money = bitcoin_to_dollars(bitcoin_rate, bitcoin_count)
    print(f"${money:,.4f}")



def bitcoin_to_dollars(bitcoin_rate, bitcoin_count):
    bitcoin_rate = bitcoin_rate.replace(",", "")
    bitcoin_rate = bitcoin_rate.split(".")
    bitcoin_rate = int(bitcoin_rate[0]) +  float("." + bitcoin_rate[1])
    money = bitcoin_rate * bitcoin_count
    return money

def bitcoin_rate_in_usd():
    bitcoin_rate_usd = bitcoin_json()
    return bitcoin_rate_usd["bpi"]["USD"]["rate"]

def bitcoin_json():
    try:
        req = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        return req.json()

    except requests.RequestException:
        pass

def get_bitcoin_count():
    try:
        money = sys.argv[1]
        money = float(money)
    except IndexError:
        return "Missing command-line argument"

    except ValueError:
        return ("Command-line argument is not a number")

    else:
        return money

if __name__ == "__main__":
    main()