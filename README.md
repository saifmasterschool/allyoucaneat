
# SMS - Stock Market Service

Welcome to our SMS project, that gives people the possibility to check there Stocks without internet access.<br><br>
After registering to the service, the user can request the stock information by sending "Stock {stock symbol}".<br>
For example if the Apple Stock data is wanted: "Stock AAPL".

The program then connects to the Seeking Alpha API for the current data.<br>
Afterwards the user receives a SMS with the following info:
- Company Name
- Market Open Price
- Market Closing Price
- High Price
- Low Price
- Current Price


(This project was developed as part of a Masterschool Hackathon)




## REQUIREMENTS

- sqlalchemy
- sqlalchemy
- python-dotenv
- requests
- uuid_utils
- yfinance
## Authors

- [@kaiser-data](https://github.com/kaiser-data)
- [@Marinaropc](https://github.com/Marinaropc)
- [@Suma-H](https://github.com/Suma-H)
- [@samypt](https://github.com/samypt)
- [@SenorGunter](https://github.com/SenorGunter)

