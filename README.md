# Web Scraping - Google Maps

A aplicação acessa o google maps, realiza uma pesquisa e captura os dados de cada resultado da pesquisa.

## Requisitos para executar a aplicação em seu computador
1. Web Driver do Google Chrome - [ChromeDriver](http://chromedriver.chromium.org/downloads)
2. Python 3.7
3. Bibliotecas

Biblioteca    | Baixar        | pip
------------- | ------------- | ---------
selenium      | [Download](https://pypi.org/project/selenium/)                       | pip install selenium
pyautogui     | [Download](https://pyautogui.readthedocs.io/en/latest/install.html)  | pip install PyAutoGUI
time          | [Documentação](https://docs.python.org/3/library/time.html)          | --

## Instruções
1. Clone o repositório
2. Instale o ChromeDriver
3. Altere o caminho do webdriver no codigo
~~~
    driver = webdriver.Chrome('C:\chrome\chromedriver.exe')
~~~
2. Abra o IDLE
3. Abra o arquivo .py e execute
