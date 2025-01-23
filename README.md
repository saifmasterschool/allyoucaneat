# SMS - Stock Market Service

Welcome to our SMS project, that gives people the possibility to check there Stocks without internet access.<br><br>
After registering to the service, the user can request the stock information by sending "Stock {stock symbol}".<br>
For example if the Apple Stock data is wanted: "Stock AAPL".

The program then connects to the Seeking Alpha API for the current data. and uses yahoo finane for historical data<br>

User get menu list by writing any text with following Options to choose:

STOCK <STOCK Symbol> for STock info
COMPARE <COMPARE SYMBOL> <DAYS> STock value compared to last days
UNSUBSCRIBE 


(This project was developed as part of a Masterschool Hackathon)


## REQUIREMENTS
Python 3.12.3 
SQLAlchemy==2.0.37
python-dotenv==1.0.1
requests==2.32.3
yfinanceyfinance==0.2.52


## Authors

- [@kaiser-data](https://github.com/kaiser-data)
- [@Marinaropc](https://github.com/Marinaropc)
- [@Suma-H](https://github.com/Suma-H)
- [@samypt](https://github.com/samypt)
- [@SenorGunter](https://github.com/SenorGunter)
