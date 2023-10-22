from tkinter import *
import tkinter as tk
from tkinter import ttk


def metodosAnual(dataframe,ruta):
    anualMenu = Toplevel()
    anualMenu.geometry("800x400")
    anualMenu.resizable(False,False)
    anualMenu.iconbitmap(ruta)
    ttk.Label(anualMenu, text="Seleccione el metodo de depreciacion anual").grid(column = 4, row =0)
