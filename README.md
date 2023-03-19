# Crypto-Trend-Analyzer
Web Scraping (Collection, Integration &amp; Preprocessing) -> Crypto Trend Analyzer 💰📈


Yahoo Finance is a media property that is part of the Yahoo! network. It provides financial news, data
and commentary including stock quotes, up-to-date news, portfolio management resources and
international market data. We used this website to collect stock quotes about Crude Oil, Gold &
NASDAQ. We chose those three different stocks based on their popularity in the financial stock
market all over the world. We are interested in the historical data of those three stocks to investigate
the effect of stock market on cryptocurrency.

All three variables are added as part of the URL to be requested using BeautifulSoup. Once the requested URL is accessed, there is a function in the script that goes over the main historical data table in the HTML script and iterates over every row ‘tr’ and get the ‘td.text’ in the selected date range and scrape each column indicating the dollar value for open, high, low, close, adjusted close, and volume count for each date. The function also contains an append to a list for each column so that the output has a complete list for all values for each column along all the dates within the defined date range. Once all the desired rows and columns are scraped. All lists are put together in a panda dataframe and saved to csv file under source (_src) indicating that this is source csv file obtained from the website

Web scraping finance.yahoo.com for Stock market Data (NASDAQ, Gold, Oil) & find correlation with Bitcoin
