import requests

url = 'https://api.exchangerate-api.com/v4/latest/USD'


class Currencyconverter:
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

    def converter(self, from_amnt, to_amnt, amnt):
        #print(from_amnt, to_amnt, amnt)
        if from_amnt != 'USD':
            amnt = amnt/self.currencies[from_amnt]
        amnt = round(amnt * self.currencies[to_amnt], 4)
        return amnt


convert = Currencyconverter(url)
print(convert.converter('QAR', 'NPR', 1))
