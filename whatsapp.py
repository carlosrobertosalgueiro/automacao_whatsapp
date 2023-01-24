import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from sys import displayhook

import pandas as pd
import urllib



contatos_df = pd.read_excel("Enviar.xlsx")
displayhook(contatos_df)

options = ChromeOptions()
options.add_experimental_option("detach", True)
navegador = webdriver.Chrome(options=options)

navegador.get("https://web.whatsapp.com/")


while len(navegador.find_elements(By.ID, "side")) < 1:
      time.sleep(1)

for i, mensagem in enumerate(contatos_df["Mensagem"]):
    pessoa = contatos_df.loc[i, "Pessoa"]
    numero = contatos_df.loc[i, "Número"]
    texto = urllib.parse.quote(f"olá, {pessoa}! {mensagem}")
    
    contatos_df.loc[i, "Mensagem"]
    link =  f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link)

