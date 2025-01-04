# udacity_cd1971
udacity data science capstone

The goal of this analysis is to predict certain anomalities in the bitcoin price. For some context here an explanation of the German term **"Hausfrauenhoch"**  from ChatGPT:


> The German term **"Hausfrauenhoch"** refers to a phenomenon in the stock market where even inexperienced investors (often retail or small-scale private investors) start investing during a market phase characterized by significant price increases. This behavior typically occurs in the later stages of a bull market, just before a market correction or crash. The term alludes to the idea that even less knowledgeable investors (such as housewives, according to the cliché) begin to invest in the stock market because they believe that profits are "guaranteed."
> 
> There isn't a direct equivalent term in English, but there are similar terms and phrases that can describe the concept. Examples include:
> 
> 1. **Late-stage bull market rally**  
>    Refers to the late phase of a bull market, where prices often continue to rise without fundamental justification, driven by optimism and speculation.
> 
> 2. **Retail investor frenzy**  
>    Describes the behavior of retail investors entering the market in large numbers, often without deep knowledge or expertise.
> 
> 3. **Market euphoria** or **irrational exuberance**  
>    These terms describe the over-the-top enthusiasm and often irrational overvaluation of markets.
> 
> 4. **FOMO buying** (Fear of Missing Out)  
>    Refers to the phenomenon where investors buy into the market out of fear of missing the rally, which further drives prices higher.
> 
> While none of these terms captures the exact nuance of *"Hausfrauenhoch,"* they can be used to describe the broader phenomenon in English.




# datasources

## google trends worldwide

search trends for relevant terms on google

googleTrends_5y
https://trends.google.de/trends/explore?date=2020-01-01%202025-01-01&q=bitcoin,investment,inflation,economy,crypto&hl=de

# bitcoinity price

Weekly price in USD traded on coinbase 

bitcoinity_price_coinbase_USD_5y
https://data.bitcoinity.org/export_data.csv?currency=USD&data_type=price&exchange=coinbase&r=week&t=l&timespan=5y

##  bitcoinity volume

traded volume BTC at several exchanges

bitcoinity_volume_btc_5y.csv
https://data.bitcoinity.org/export_data.csv?c=e&data_type=volume&r=week&t=b&timespan=5y


## bitcoinity price+volume

aggregated price and volume over all exchanges tracked by bitcoinity

bitcoinity_price_volume_USD_btc_5y
https://data.bitcoinity.org/markets/price_volume/5y/USD?r=week&t=lb&vu=curr

## blockchain

1T linear avg 

https://www.blockchain.com/explorer/charts/n-transactions

https://www.blockchain.com/explorer/charts/estimated-transaction-volume

https://www.blockchain.com/explorer/charts/market-price