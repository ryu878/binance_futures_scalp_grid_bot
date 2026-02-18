# Binance Futures Scalp Grid Bot

![image](https://user-images.githubusercontent.com/81808867/164885242-d2da893e-e60e-444e-be76-7e41aa9bb7ed.png)


On Binance exchange (at date April 2022) there are Futures nominated in BUSD. And there are rebates 0.01% for market maker, so it is +0.02% per turn if you are using limit orders both for entry and for exit.

<i>This bot can trade any Futures, for example nominated in USDT too. But in this case you need to adjust take profit settings (to ensure that the fees are lower than your profits).</i>


This simple bot written with python enter the market using small grid based on ATR and immediately place close order. In this example it will trade on XRPBUSD pair, but you can change it in settings. Please keep in mind that this example bot will <u>open only short</u> trades.

## How to use
- Edit config.py file, add you API credentials and change initial grid lot size.
- Run python3 xrp.py

## Entry logic
Bot will check EMA 6 High (and, optional, EMA60, EMA120, EMA240) and if price higher it will start placing entry sell orders.

## Known issue
Sometimes bot first delete the grid and then open position. Will fix it in next releases.

## To Do
- Change position and orders info requests to websocket.
- Change decimals for symbol from manual to auto.

## Requirements
Run pip install to install:

<code>pip install python-binance</code>

<code>pip install ta</code>

<code>pip install pandas</code>

To start trading on Binance Futures and earn rebates register here: https://www.binance.com/en/futures/ref/421719790


***

## 📄 License
MIT License - Feel free to modify and distribute.


## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check issues page.

## ⚠️ Disclaimer

> This project is for informational and educational purposes only. You should not use this information or any other material as legal, tax, investment, financial, or other advice. Nothing contained here is a recommendation, endorsement, or offer by me to buy or sell any securities or other financial instruments.
>
> **If you intend to use real money, use it at your own risk.**
>
> Under no circumstances will I be responsible or liable for any claims, damages, losses, expenses, costs, or liabilities of any kind, including but not limited to direct or indirect damages for loss of profits.


***

## 📌 Quantitative Researcher | Algorithmic Trader | Trading Systems Architect

Quantitative researcher and trading systems engineer with end-to-end ownership of systematic strategies — from research and statistical validation to low-latency execution and production deployment.

Core focus areas:
- Systematic strategy design and validation
- Market microstructure analysis (order book dynamics, volume, delta, liquidity, spread behavior)
- Backtesting framework development (tick-level and historical data)
- Execution engine architecture and order lifecycle management
- Real-time market data processing
- Risk-aware system design
- Production-grade trading infrastructure (24/7 environments)

Experience across crypto (CEX, DEX), FX, and exchange-traded markets.

## Technical Stack

- Languages: Python, C++, MQL5
- Execution & Connectivity: REST, WebSocket, FIX
- Infrastructure: Linux, Docker, Redis, PostgreSQL
- Analytics: NumPy, Pandas, custom backtesting frameworks

## Contact

Email: ryu8777@gmail.com

***
