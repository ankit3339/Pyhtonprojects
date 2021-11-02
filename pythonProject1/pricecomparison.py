import json

if __name__ == '__main__':
    price = []
    with open('/Users/ankitpandey/Desktop/python/pythonProject1/data.json', encoding='Utf8') as f:
        price_data = f.read()
        # print(json_file)
    if price_data is not None:
        json_file = json.loads(price_data)

        for d in json_file:
            price.append({'name': d['name'], 'price': d['amazon_price'], 'url': d['amazon_url']})
            price.append({'name': d['name'], 'price': d['ebay_price'], 'url': d['ebay_url']})
            price.append({'name': d['name'], 'price': d['walmart_price'], 'url': d['walmart_url']})

            minPrice = min(price, key=lambda x: float(x['price']))
            store_name = ''
            # Pick the store name based on url
            if 'amazon' in minPrice['url'].lower():
                store_name = 'Amazon'
            elif 'walmart' in minPrice['url'].lower():
                store_name = 'walmart'
            elif 'ebay' in minPrice['url'].lower():
                store_name = 'eBay'
            print('{} is available in cheap price at {}. The price is ${}'.format(minPrice['name'], store_name,
                                                                                  minPrice['price']))
            price = []
