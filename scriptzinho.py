import pyautogui 
import pyperclip
import time

# setar quanto tempo entre cada leitura de linha
pyautogui.PAUSE = 1
# abrir o navegador
pyautogui.press("win")
pyperclip.copy("opera")
pyautogui.hotkey("ctrl","v")
pyautogui.press("enter")
# aguardar 3 segundos para terminar o carregamento do navegador
time.sleep(3)
# abrir o twitter
pyperclip.copy("twitter.com/home")
pyautogui.hotkey("ctrl","v")
pyautogui.press("enter")
# aguardar 7 segundos para terminar o carregamento da pagina
time.sleep(7)
# abrir o modal de novo tweet
pyautogui.press("n")
# aguardar 3 segundos para a abertura do modal
time.sleep(3)
# Tweetar. 😃
pyperclip.copy("Okay, meu primeiro tweet feito totalmente em #python 🐍")
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("ctrl","enter")