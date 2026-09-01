# Health Check Dashboard

Monitors server availability and sends email alerts on failure.

## Features
- Checks multiple servers via HTTP
- Sends email alert on timeout or unexpected status code
- Configurable via YAML file
- Automated via cron job

## Configuration
Edit `config.yaml` to add your servers:

```yaml
servidores:
  - nome: nginx-local
    url: http://172.24.58.32
  - nome: google
    url: https://google.com

alertas:
  email: your@email.com
```

## Environment Variables
Create a `.env` file:

EMAIL=your@gmail.com
APP_PASSWORD=your_app_password

## Schedule (cron)

30 12 * * * cd /home/luiszotavio/projects/health-check && python3 healthcheck_v2.py
