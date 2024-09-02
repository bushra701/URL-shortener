import requests

def urlshortener(originallink):
    apikey = '083228e6811fdcc9e32843c5b8a75e52'
    baseurl = 'https://cutt.ly/api/api.php'

    
    payload = {'key': apikey, 'short': originallink}
    
    try:
        
        response = requests.get(baseurl, params=payload)
        data = response.json()

        
        if data['url']['status'] == 7:
            print('Short link:', data['url']['shortLink'])
        else:
            print('Error: Could not shorten the URL.')

    except Exception as e:
        print(f"An error occurred: {e}")


inp = input('Enter a link: ')
urlshortener(inp)

