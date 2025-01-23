# SMS Stock Market Service by Team Wolves of Wallstreet

This SMS service allows users to check stock information without internet access. After registering, users can request stock data by texting "Stock {stock symbol}" to a designated phone number. For example, to get Apple stock data, text "Stock AAPL".

The service retrieves current stock data from the Seeking Alpha API and historical data from Yahoo Finance.

**Features:**

* Check stock information via SMS
* Compare stock value to previous days' values

**How it Works:**

1. Users register for the service.
2. Users text "Stock {stock symbol}" to the service number.
3. The service retrieves and sends back the requested stock information.
4. Optionally, users can text "COMPARE <COMPARE SYMBOL> <DAYS>" to compare the stock value to the previous days' values.

**Text Commands:**

* `Stock {stock symbol}`: Get information about a specific stock.
* `COMPARE <COMPARE SYMBOL> <DAYS>`: Compare a stock's value to the previous days' values. (e.g., "COMPARE AAPL 7")
* `UNSUBSCRIBE`: Unsubscribe from the service.

**(1st Place Winner - Masterschool Hackathon)**

## Requirements

* Python 3.12.3
* SQLAlchemy==2.0.37
* python-dotenv==1.0.1
* requests==2.32.3
* yfinance==0.2.52

## Setup

1. Initialize the database: Run `db-setup.py`.
2. Manage users: Run `usermgmt.py`.
3. Start the service: Run `main.py` to continuously check for incoming texts and respond.

## TEAM

* [@kaiser-data](https://github.com/kaiser-data)
* [@Marinaropc](https://github.com/Marinaropc)
* [@Suma-H](https://github.com/Suma-H)
* [@samypt](https://github.com/samypt)
* [@SenorGunter](https://github.com/SenorGunter)

