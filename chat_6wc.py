import pyautogui
import pyperclip
import time
import gspread
import random
from oauth2client.service_account import ServiceAccountCredentials

sheet_url = "https://docs.google.com/spreadsheets/d/1iUl9H_ZUxyiGqC4SB7EiNWPjeHnAbXtZu3gvB9-tAUA/edit?usp=sharing"

def obtener_nombres(sheet_url):
    # Alcance para acceder a Google Sheets y Drive
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    
    # Autenticación con credenciales del archivo JSON
    creds = ServiceAccountCredentials.from_json_keyfile_name("credenciales.json", scope)
    client = gspread.authorize(creds)
    
    # Acceder al documento
    sheet = client.open_by_url(sheet_url)
    worksheet = sheet.sheet1  # primera hoja
    
    # Leer desde la columna D (índice 4) a partir de la fila 2
    nombres_columna_d = worksheet.col_values(4)[1:]  # [1:] salta la primera fila
    
    return nombres_columna_d

def enviar_mensaje(nombre):
    time.sleep(2)
    mensaje = ""
    for nombre in nombres:
        opcion = generar_random()
        
        if opcion == 1:
            mensaje = f"""Holaa {nombre} o/
    Estamos preparando los Tryouts de Arg para el mundial de 6 dígitos (6wc), si te interesa participar para ver si entras al Equipo que va a representar a Argentina unite al servidor de discord.
    https://discord.gg/mRPUxwnkd3"""
            
        elif opcion == 2:
            mensaje = f"""Buenaaas {nombre}!
    Estamos juntando players para los Tryouts de Arg en la 6wc (Mundial de 6 dígitos), si querés unirte a jugar y ver si quedás para el Equipo que represente a Argentina unite al Discord.
    https://discord.gg/mRPUxwnkd3"""
            
        else:
            mensaje = f"""Hola {nombre} o/
    Ya estamos organizando los Tryouts de Arg para la 6wc (Mundial de 6 dígitos) y estamos reclutando jugadores para poder armar el Equipo que represente a Argentina. Si te interesa, metete al Discord:
    https://discord.gg/mRPUxwnkd3"""

        # Abrir chat
        pyautogui.hotkey("ctrl", "n")
        time.sleep(2)
        
        # Escribir nombre
        pyperclip.copy(nombre)
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press("enter")
        pyautogui.moveTo(573, 791)
        pyautogui.click()
        time.sleep(60)
        
        #
        pyperclip.copy(mensaje)
        pyautogui.hotkey("ctrl", "v")
        
        time.sleep(2)
        
def generar_random():
    return random.randint(1, 3)
    print("ola si randomize")

nombres = obtener_nombres(sheet_url)
enviar_mensaje(nombres)



