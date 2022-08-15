<h1> Webhook Listner for Postal SMTP server</h1>
<h3>This webhook listener is used to store daily email logs on the postal server</h3>

# Webhook Listener
<!--  
> Short blurb about what your product does.
 -->



![](header.png)

## Installation

Create Volume:

```bash
Docker volume create webhook_data
```

install docker image:

```sh
docker run -d \
 --name webhook-listner \
 -p 127.0.0.1:9000:8181 \
 -v webhook:data \
 shubhammore/webhook:latest

```

## volume details

All data will store in data folder
according to today's Date
