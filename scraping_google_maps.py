from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.common.keys import Keys
import pyautogui
import time

driver = webdriver.Chrome('C:\chrome\chromedriver.exe')
driver.get('https://www.google.com/maps/')
driver.maximize_window()
pesquisar = driver.find_element_by_xpath('//*[@id="searchboxinput"]') #encontra o campo de pesquisa
pesquisar.send_keys('tecnologia') #digita o termo a ser pesquisado
pesquisarbotao = driver.find_element_by_xpath('//*[@id="searchbox-searchbutton"]') #encontra o botão pesquisar
pesquisarbotao.click() #clica no botão
time.sleep(3) #aguarda 3 segundos

for i in range(1,40,2): #incrementa de 2 em 2 >> 1,3,5,7......39
  seleciona = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[3]/div['+str(i)+']') #seleciona o primeiro resultado da pesquisa
  seleciona.click() #clica no resultado
  time.sleep(4) #aguarde 4 segundos
  #try and except foi usado para verificar a existencia do elemento dentro da pagina do resultado selecionado
  try: #tente encontrar esse elemento
    driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[1]/div[3]/div[1]/h1')
  except NoSuchElementException: #se ele não existir atribua o valor 1 para a variavel nome
    nome = 1
    pass #siga em frente
  nome = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[1]/div[3]/div[1]/h1') #se o elemente exisitir, ele sera guardado dentro da variavel nome
  try:
    driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[6]/div/div[1]/span[3]/span[3]')
  except NoSuchElementException:
    endereco = 1
    pass
  endereco = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[6]/div/div[1]/span[3]/span[3]')
  try:
    driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[8]/div/div[1]/span[3]/span[3]')
  except NoSuchElementException:
    site = 1
    pass
  site = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[8]/div/div[1]/span[3]/span[3]')
  try:
    fone = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[9]/div/div[1]/span[3]/span[3]')
  except NoSuchElementException:
    fone = 1
    pass 
  time.sleep(4)

  #if else foi utilizado para validar a variavel e ver se ela possui um elemento Xpath ou o numero 1

  if nome == 1: #se a variavel nome for igual a 1
    print("vazio") #escreva vazio
  else: #caso contrario
    print(nome.text) #escreva o texto que foi capturado do elementro Xpath
  if endereco == 1:
    print("vazio")
  else:
    print(endereco.text)
  if site == 1:
    print("vazio")
  else:
    print(site.text)
  if fone == 1 :
    print("vazio")
  else:
    print(fone.text)

  time.sleep(4)
  volta_resultados = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/button') #encontra o link Voltar para os resultados
  volta_resultados.click() #clica no link
  time.sleep(5)
