#Librerias
import openai
from tkinter import *
from tkinter import ttk
import tkinter as tk

ruta = "gpt.ico"

def GPTRequest(detalle):
    #Inicializar Ventana 
    GPT = Tk()

    frm = tk.Frame(GPT)
    frm.grid(column=0, row=1, padx=10, pady=10)
    GPT.geometry("600x300")
    GPT.resizable(True,True)
    GPT.title("Depreciacion de Activos ATI [Detalle con GPT3.5]")
    GPT.iconbitmap(ruta)

    #Inicia Mensajes al Usuario
    frm.grid()
    tk.Label(frm, text="GPT 3.5 Dice:", background="lightgreen",font=("Arial",10)).grid(column=0, row=0)

    api_key = "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"  

    openai.api_key = api_key


    # Llamar a la API para obtener la respuesta de ChatGPT
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Puedes utilizar otros modelos como gpt-3.5-turbo, gpt-3.5, etc.
        messages=[
            {"role": "user", "content": detalle}
        ]
    )

    reply = response['choices'][0]['message']['content']
    # print("ChatGPT:", reply)

    #Muestra el Reply en ventana
    descripcionGPT = tk.Label(frm, text=reply, background="white", font=("Arial", 10))
    descripcionGPT.grid(column=0, row=1)  # Adjust the grid parameters as needed
    GPT.mainloop()


