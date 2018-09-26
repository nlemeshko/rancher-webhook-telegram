### Rancher WebHook Telegram


#### Description

Rancher 2.0 has Alert support Webhook, We would like to send message to Telegram instead of Slack, ...

So this project will create webhook server to receive alert event from Rancher Server and send to Telegram



#### Environment


- `TELEGRAM_TOKEN`: Bot Token 
- `TELEGRAM_CHATID`: ID of channel or group ID which you want to send message


#### How to run

- Just run

```
docker-compose up -d 
```
