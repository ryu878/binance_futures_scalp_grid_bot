<strong>Binance Futures Scalp Grid Bot</strong>

![image](https://user-images.githubusercontent.com/81808867/164885242-d2da893e-e60e-444e-be76-7e41aa9bb7ed.png)


On Binance exchange (at date of April 2022) there are Futures nominated in BUSD. And there are rebates 0.01% for market maker, so it is +0.02% per turn if you are using limit orders both for entry and for exit.

<i>This bot can trade any Futures, nomnated in USDT too. But in this case you need to adjust take profit settins (to ensure that the fees are lower than your profits).</i>

This simple bot written with python enter the market using small grid based on ATR and immediately place close order. In this example it will trade on XRPBUSD pair, but you can change it in settings.

<strong>How to use</strong>

1. Edit config.py file, add you API credentials and change initial grid lot size.
2. run python3 xrp.py

<strong>Entry logic</strong>

Bot will check EMA 6 High (and, optional, EMA60, EMA120, EMA240) and if price higher it will start placing entry orders.



To start trading on Binance using BUSD Futures and earn rebates register here: https://www.binance.com/en/futures/ref/421719790

<strong>Contacts</strong>

Feel free to contact me via Discord: ryuryu#4087
or join Discord group here: https://discord.gg/zSw58e9Uvf
