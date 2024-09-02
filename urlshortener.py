import requests

def urlshortener(originallink, apikey):
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


apikey = input('Enter your Cutt.ly API key: ')


inp = input('Enter a link to shorten: ')
urlshortener(inp, apikey)
