# Rust Discord Bot for RustyCorns

![What the bot looks like](https://gyazo.com/c87daaf468ee51828316ae6efccfa166.png)

### How to install modules

```
for windows:
python -m pip install -r requirements.txt

for linux:
python3 -m pip install -r requirements.txt
```

### ENV

rename `.env.example` to `.env` then store your token and some other private info like this:

Find your server on BattleMetrics [Here](https://www.battlemetrics.com/servers/rust)

![Where to get the BM ID](https://gyazo.com/ba8b6566a017293e9e145cb07086cc86.png)

```
DISCORD=
battleMetricsServerID=
```

### PM2

PM2 is an alternative script provided by NodeJS, which will reboot your bot whenever it crashes and keep it up with a nice status. You can install it by doing `npm install -g pm2` and you should be done.

```
# Start the bot
pm2 start pm2.json

# Tips on common commands
pm2 <command> [name]
  start rustycorns   Run the bot again if it's offline
  list                    Get a full list of all available services
  stop rustycorns    Stop the bot
  reboot rustycorns  Reboot the bot
```
