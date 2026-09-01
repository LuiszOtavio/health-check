import yaml
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")

def connection_test(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"The server {url} is OK, code: {response.status_code}")
        else:
            print(f"The response of the server {url} was unexpected. code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"{e}: Error checking the {url} server.")
        send_mail(url)

def send_mail(url):
    with smtplib.SMTP("smtp.gmail.com", 587) as mailServidor:
        mailServidor.starttls()
        mailServidor.login(EMAIL, APP_PASSWORD)
        mensagem = f"Subject: Alerta de servidor\n\nVerifique o servidor {url}. Timeout/connection error"
        mailServidor.sendmail(EMAIL, EMAIL, mensagem)  

try:
    with open("config.yaml") as fileConnect:
        config = yaml.safe_load(fileConnect)
        for servidor in config['servidores']:
            connection_test(servidor['url'])
        exit(0)
except Exception as e:
    print(f"{e}: Não foi possivel abrir o config.yaml")
    exit(1)