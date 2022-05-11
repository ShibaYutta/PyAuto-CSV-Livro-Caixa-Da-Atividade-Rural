import pyautogui
import csv
from tkinter import Tk
from tkinter.filedialog import askopenfilename

x, y = pyautogui.size()
print("proporção do monitor",x, y)


def mudarPagina(numeroPagina):
    pyautogui.click(285 + ((numeroPagina-1)*35), 147)

def clicarNovo():
    pyautogui.click(1645, 958)

def inserirDados(dia, conta, historico, valor):
    pyautogui.click(300,185)
    pyautogui.write(dia)
    pyautogui.click(300,230)
    pyautogui.write(conta)
    pyautogui.press("enter")
    pyautogui.click(300,280)
    pyautogui.write(historico)
    pyautogui.click(300,385)
    pyautogui.write(valor)
    pyautogui.press("enter")
    pyautogui.press("enter")

def pegarDados():
    filename = askopenfilename()
    with open(filename, newline='') as csvfile:
        csv_readed = csv.reader(csvfile, delimiter=';', quotechar='|')
        list_csv = []
        for x in csv_readed:
            list_csv.append(x)
        return list_csv
    
def organizarDados(dados):
    dict_meses = {}
    for row in dados[1:]:
        mes = row[0][3:5]
        if mes in dict_meses:
            dict_meses[mes].append(row)
        else:
            dict_meses[mes] = [row]
            
    return dict_meses

Tk().withdraw() 
print('Selecione o arquivo csv')
dados = pegarDados()
dados = organizarDados(dados)
for mes in dados:
    dados_mes = dados[mes]
    print("iniciando mes",mes+"..")
    for linha in dados_mes:
        time.sleep(0.250)
        mudarPagina(int(mes))
        clicarNovo()
        time.sleep(0.1)
        inserirDados(linha[0][0:2], linha[1], linha[2], linha[3])    
print('Finalizado!')