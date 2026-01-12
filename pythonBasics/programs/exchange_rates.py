import requests

response = requests.get('http://api.exchangeratesapi.io/v1/latest'
                         + '?access_key=16010bc596af7c0a6f1a502bcca0f95c'
                         + '&base=EUR'
                        )

if response.ok:
    data = response.json()
    rates = data['rates']
    base = data['base']
    date = data['date']

    print('base: ', base)
    print('date: ', date)

    for rate in rates:
        print(rate + ": ", rates[rate])