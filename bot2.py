import pyautogui
from time import sleep
import webbrowser
from random import choice

def mensagem_de_inicio(nome_da_automação):
    pyautogui.alert(f'Iniciando Automação de {nome_da_automação}!! Isso pode levar alguns instantes')
    

def localizar_e_mover(nome_do_arq,arquivo_secundario=None):
    try:
        local = pyautogui.locateCenterOnScreen(nome_do_arq)
        pyautogui.moveTo(local[0],local[1],duration=0.6)
        sleep(1.5)
    except:
        local = pyautogui.locateCenterOnScreen(arquivo_secundario)
        pyautogui.moveTo(local[0],local[1],duration=0.6)
        sleep(1.5)


def verificarCurtida(printDoBotao1,printdoBotao2=None):
    try:
        local_do_botao = pyautogui.locateCenterOnScreen(printDoBotao1)
        pyautogui.moveTo(local_do_botao[0],local_do_botao[1],duration=0.5)
        return True
    except:
        local_botao_jacurti = pyautogui.locateCenterOnScreen(printdoBotao2)
        pyautogui.moveTo(local_botao_jacurti[0],local_botao_jacurti[1],duration=0.5)
        return False
    

def login(login_Do__Usuario_insta,senha):
    localizar_e_mover('telefone_usuario_email.png')
    pyautogui.click()
    sleep(1)
    pyautogui.typewrite(login_Do__Usuario_insta)
    pyautogui.press('tab')
    sleep(1)
    pyautogui.typewrite(senha)
    pyautogui.press('enter')
    sleep(8)


def logout():
    localizar_e_mover('menu_mais.png')
    pyautogui.click()
    localizar_e_mover('botao_sair.png')
    pyautogui.click()
    sleep(3)
    pyautogui.hotkey('alt','f4')


def comentar(text):
    pyautogui.typewrite(text)
    sleep(1.5)
    pyautogui.press('enter')
    sleep(1.5)


def curtir_publicacao():
    try:
        localizar_e_mover('botao_ja_curti.png')
        sleep(1)
        localizar_e_mover('botao_fechar_publicacao.png')
        pyautogui.click()

    except:
        localizar_e_mover('botao_curtir.png','curtir2.png')
        sleep(1)
        pyautogui.click()
        pyautogui.move(40,0,duration=0.8)
        

#  Passo 1:
mensagem_de_inicio('Curtidas e Comentários Instagram')

#    Passo 2:
webbrowser.open_new_tab('https://www.instagram.com/')
sleep(4)
localizar_e_mover('trocar_de_conta.png')
pyautogui.click()
login()   #>>>>>  COLOCAR, LOGIN E SENHA DA CONTA QUE DESEJA LOGAR <<<<<<<

#  Passo 3:
localizar_e_mover('botao_pesquisa.png')
pyautogui.click()
sleep(1)
# pyautogui.typewrite(choice())  # >>>>>>>  Aqui PODERÁ DIGITAR A PAGINA QUE QUER LOCALIZAR  <<<<<<<<<<
pyautogui.typewrite()  # >>>>>>>  Aqui PODERÁ DIGITAR A PAGINA QUE QUER LOCALIZAR  <<<<<<<<<<
pyautogui.press('enter',presses=3,interval=1.5)
sleep(3)

#   Passo 4:
localizar_e_mover('publicacoes1.png','publicacoes2.png')
pyautogui.move(-120,120,duration=1)
pyautogui.click()
    
#    Passo 5,6,7,8:
pyautogui.moveTo(1000,939,duration=0.5)
sleep(1)

verificar_curtida = verificarCurtida('botao_curtir.png','botao_ja_curti.png')
if verificar_curtida == False:
    localizar_e_mover('botao_fechar_publicacao.png')
    pyautogui.click()
else:
    pyautogui.click()
    pyautogui.move(40,0,duration=0.8)
    pyautogui.click()
    comentar('Boa foto!!')
    localizar_e_mover('botao_fechar_publicacao.png')
    pyautogui.click()

# Passo 9:
localizar_e_mover('pagina_inicial.png')
pyautogui.click(clicks=2,interval=1)

#   Passo 10:
logout()

# Passo 11:
pyautogui.alert('Automação Finalizada!!')

