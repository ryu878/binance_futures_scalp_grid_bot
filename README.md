# Binance Futures Scalp Grid Bot <a href="https://github.com/ryu878/binance_futures_scalp_grid_bot/blob/main/LICENSE.md">![image](https://camo.githubusercontent.com/83d3746e5881c1867665223424263d8e604df233d0a11aae0813e0414d433943/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d4d49542d626c75652e737667)</a>

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
- python-binance
- ta
- pandas
- numpy


To start trading on Binance Futures and earn rebates register here: https://www.binance.com/en/futures/ref/421719790

## Disclaimer
<hr>
This project is for informational purposes only. You should not construe this information or any other material as legal, tax, investment, financial or other advice. Nothing contained herein constitutes a solicitation, recommendation, endorsement or offer by us or any third party provider to buy or sell any securities or other financial instruments in this or any other jurisdiction in which such solicitation or offer would be unlawful under the securities laws of such jurisdiction.

If you intend to use real money, use it at your own risk.

Under no circumstances will we be responsible or liable for any claims, damages, losses, expenses, costs or liabilities of any kind, including but not limited to direct or indirect damages for loss of profits.
<hr>

## Contacts

Feel free to contact me via Discord: ryuryu#4087
or join my Discord group: https://discord.gg/zSw58e9Uvf

<a href="https://discord.gg/zSw58e9Uvf">![image](https://user-images.githubusercontent.com/81808867/166115186-70de12b2-39fd-4eda-bb12-c1d8bec24ac6.png)</a>

