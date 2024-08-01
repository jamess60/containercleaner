import socket
from colorama import Fore, Back, Style  


def ok_msg(text):
    rettext = Fore.BLACK + Back.GREEN + Style.BRIGHT + " [OK] " + Style.RESET_ALL + " - " + text
    print(rettext)
    # return rettext


def info_msg(text):
    rettext = Fore.BLACK + Back.CYAN + Style.BRIGHT + "[INFO]" + Style.RESET_ALL + " - " + text
    print(rettext)
    # return rettext


def warn_msg(text):
    rettext = Fore.BLACK + Back.YELLOW + Style.BRIGHT + "[WARN]" + Style.RESET_ALL + " - " + text
    print(rettext)
    # return rettext


def err_msg(text):
    rettext = Fore.WHITE + Back.RED + Style.BRIGHT + "[FATAL ERROR]" + Style.RESET_ALL + " - " + text
    print(rettext)
    # return rettext



def rainbow(text):
    length = len(text)
    i = 0
    char = text[i]
    try:
        while i != length:
            print(Fore.LIGHTRED_EX + char, end='')
            i = i + 1
            char = text[i]
            print(Fore.LIGHTYELLOW_EX + char, end='')
            i = i + 1
            char = text[i]
            print(Fore.LIGHTGREEN_EX + char, end='')
            i = i + 1
            char = text[i]
            print(Fore.LIGHTCYAN_EX + char, end='')
            i = i + 1
            char = text[i]
            print(Fore.LIGHTBLUE_EX + char, end='')
            i = i + 1
            char = text[i]
            print(Fore.LIGHTMAGENTA_EX + char, end='')
            i = i + 1
            char = text[i]
    except IndexError:
        pass
    return text






