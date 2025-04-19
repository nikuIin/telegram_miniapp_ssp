# Stone-scissor-paper game in the Telegram Mini App

### Install guide:
1. Clone this repo:

```shell
git clone https://github.com/nikuIin/telegram_miniapp_ssp.git
```

2. Install uv

For macOS and Linux:
```shell
curl -LsSf https://astral.sh/uv/install.sh | sh # mac-os/linux
```

For Windows:
```shell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

3. Add your telgegram-api-token in the .env.example and run commands:
```shell
chmod +x .env.example

. ./.env.example
```

4. Configure your tunnel, you can use such of this solutions:

[ngrok](https://ngrok.com/ )
[vk-tunnel](https://dev.vk.com/ru/libraries/tunnel)
[tuna](https://tuna.am/)

5. Run project

```shell
uv run src/app.py 
```




