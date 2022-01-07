import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#ROBO PARA ACESSAR O PROTOCOLO DA UNI E TRAMITAR

def acess_p(proto, texbase, usuario, senha):

    #ACESSA O SITE (Lembre de usar Raw String (r"string"), senao o comando não encontra, tambem é possivel usar um Service, do Selenium)
    driver = webdriver.Chrome(executable_path=r"C:\Users\magnu\Downloads\chromedriver_win32\chromedriver.exe")
    driver.get("http://www.protocolosecretaria.unimontes.br/dashboard/login")
    #ENTRA COM AS CREDENCIAIS
    input = driver.find_element(By.ID, "inputEmail")
    pas = driver.find_element(By.ID, "inputPassword")
    input.send_keys(usuario)
    pas.send_keys(senha)
    #PROCURA O PROTOCOLO E TRAMITA
    button = driver.find_element(By.XPATH, ("/html/body/div/form/button"))
    button.click()
    input = driver.find_element(By.XPATH, "/html/body/div[2]/a[3]")
    input.click()
    input = driver.find_element(By.XPATH, ("//*[@id='nova_tramitacao']"))
    input.send_keys(proto)
    input.send_keys(Keys.ENTER)
    input = driver.find_element(By.XPATH, ("//*[@id='DESTINATARIO']"))
    #TRAMITA EM NOME DE
    input.send_keys(usuario)
    input =  driver.find_element(By.XPATH,("//*[@id='PARECER']"))
    input.click()
    #SELECIONA O TEXTO BASE A PARTIR DO PARAMETRO 'texbase'
    if texbase == 1:
        input.send_keys("texto base 1")
    elif texbase == 2:
        input.send_keys("texto base 2")
    elif texbase == 3:
        input.send_keys("texto base 3")
    else:
        return 0
    input = driver.find_element(By.XPATH, ("/html/body/div[2]/div/form/div[4]/button"))
    input.click()
    time.sleep(4)
    #TODOS OS ELEMENTOS DO HTML FORAM ENCONTRADOS POR XPATH
    driver.close()


def main():
    #MAIN COM LOOP INFINITO
    #É POSSÍVEL FAZER COM QUE O PROGRAMA PEGUE OS DADOS DE UM ARQUIVO TXT, MAS AINDA FUNCIONA MANUALMENTE PQ N FIZ KEKE
    user = str (input("Nome de Usuario: "))
    passw = str (input("Senha do usuario: "))
    while True:
        pnum = int (input("Numero do protocolo: "))
        txtb = int (input("Texto de protocolo (Valores entre 1 e 3, 4 para encerrar): "))
        if txtb == 4:
            break
        acess_p(pnum, txtb, user, passw)
main()