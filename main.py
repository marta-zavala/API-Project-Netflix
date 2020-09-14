import sys
from src.functions import *
from argparse import ArgumentParser

def main():
    parser = ArgumentParser(description = "Escribe descripcion")
    parser.add_argument("--saludar", help="Saluda")

    return parser.parse_args()
