import os
from twilio.rest import Client
import cryptocompare

account_sid = "AC0c39ad3fa7fa237e32db910e2a394844"
auth_token = "af7dfb2151ec4e1795e828cc9b0bdc75"

client = Client(account_sid, auth_token)

# Storing all data in a variable
data = cryptocompare.get_coin_list(format=False)
# Empty list to store coin-names
coinnames = []
# List of keys(the symbols are the keys here)
coinsymbols = list(data.keys())

# Empty list to include the names of countries
currencies = []

# Iterate through the list of symbols, get the CoinName for each and append it to the list
for item in coinsymbols:
    coinnames.append(data[item]["CoinName"])

check = True
while check:
    choice = input("Symbol or Names. Respond with the phrase or first letter (S or N )")
    if choice.lower()[0].strip() == "s":
        check1 = True
        while check1:
            cryptosymbol = input("enter symbol ").upper().strip()
            currency = input("enter currency symbol ").upper().strip()
            if cryptosymbol in coinsymbols:
                check1 = False
                currprice = cryptocompare.get_price(cryptosymbol, currency= currency)[cryptosymbol][currency]
                message = client.messages.create(body=f"Current price for {cryptosymbol} in {currency} is {currprice}", from_='+18454426535', to="+919726737274")
                print(message.sid)
                check = False
    elif choice.lower()[0].strip() == "n":
        check2 = True
        cryptoname = input("enter name ").lower().strip()
        currency = input("enter currency symbol ").upper().strip()
        cryptoname = cryptoname.replace(cryptoname[0], cryptoname[0].upper())
        cryptosymbol = coinsymbols[coinnames.index(cryptoname)]
        currprice = cryptocompare.get_price(cryptosymbol, currency = currency)[cryptosymbol][currency]
        message = client.messages.create(body=f"Current price for {cryptosymbol} in {currency} is {currprice}",from_='+18454426535', to="+919726737274")
        print(message.sid)
        check = False
    else:
        print("Invalid entry ")





