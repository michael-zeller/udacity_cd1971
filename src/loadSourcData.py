from pytrends.request import TrendReq

def download_google_trends_data(keywords, timeframe='today 5-y', geo='', cat=0, gprop=''):
    requests_args = {
    'headers': {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
}


    pytrends = TrendReq(hl='de-DE', tz=60, requests_args=requests_args)
    pytrends.build_payload(keywords, timeframe=timeframe, geo=geo, cat=cat, gprop=gprop)
    data = pytrends.interest_over_time()
    return data

# Example usage:
if __name__ == "__main__":
    keywords = ['Bitcoin', 'Investment', 'Inflation', 'Economy', 'Wirtschaft']
    trends_data = download_google_trends_data(keywords)
    print(trends_data)