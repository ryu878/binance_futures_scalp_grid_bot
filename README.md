# Announcement: Discontinuation of Free Bots for Bybit 
I regret to inform that I will no longer be updating or maintaining my free trading bots for the Bybit exchange. This decision comes after a deeply disappointing experience with Bybit's unethical practices, particularly regarding their affiliate program and their handling of user earnings.

Despite fully complying with Bybit's rules, including completing KYC (Know Your Customer) requirements, my affiliate earnings were abruptly terminated without valid justification. Bybit cited "one IP address" as the reason, a claim that is both unreasonable and unfair, especially for users in shared living environments or using shared internet connections. This behavior demonstrates a lack of transparency and fairness, and it has eroded my trust in Bybit as a reliable platform.

I want to thank everyone who has supported my work and used my free bots for Bybit. Your trust and feedback have been invaluable, and I hope to continue providing value to the crypto community through my future projects. Stay tuned for updates, and feel free to reach out if you have any questions or need assistance during this transition.

Thank you for your understanding and support.

---

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

## Disclaimer
This project is for informational and educational purposes only. You should not use this information or any other material as legal, tax, investment, financial or other advice. Nothing contained here is a recommendation, endorsement or offer by me to buy or sell any securities or other financial instruments. If you intend to use real money, use it at your own risk. Under no circumstances will I be responsible or liable for any claims, damages, losses, expenses, costs or liabilities of any kind, including but not limited to direct or indirect damages for loss of profits.

## Contacts
I develop trading bots of any complexity, dashboards and indicators for crypto exchanges, forex and stocks.
To contact me please pm:

Telegram: https://t.me/ryu8777

Discord: https://discord.gg/zSw58e9Uvf

## Crypto Exchanges

😎 Register on BingX and get a 20% discount on fees: https://bingx.com/invite/HAJ8YQQAG/

👍 MEXC: https://promote.mexc.com/r/f3dtDLZK

🐀 Join Bybit: https://www.bybit.com/invite?ref=P11NJW

## VPS for bots and scripts
I prefer using DigitalOcean.
  
[![DigitalOcean Referral Badge](https://web-platforms.sfo2.digitaloceanspaces.com/WWW/Badge%202.svg)](https://www.digitalocean.com/?refcode=3d7f6e57bc04&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge)
  
To get $200 in credit over 60 days use my ref link: https://m.do.co/c/3d7f6e57bc04
