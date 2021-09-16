#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(string: str) -> bool:
    length = len(string)
    chaine_pair = ((length % 2) == 0)
    return chaine_pair


def remove_third_char(string: str) -> str:
    new_string = string.split(string[2])
    return (''.join(new_string))


def replace_char(string: str, old_char: str, new_char: str) -> str:
    new_string = ""
    for char in string:
        if char == old_char:
            new_string += new_char
        else:
            new_string += char

    return new_string


def get_number_of_char(string: str, char: str) -> int:
    qte = 0
    for x in range(len(string)):
        if string[x] == char:
            qte += 1
    return qte


def get_number_of_words(sentence: str, word: str) -> int:
        qte = 0
        word_list = sentence.split()
        longueur = len(word_list)
        for x in range(longueur):
            if word_list[x] == word:
                qte += 1
        return qte


def main() -> None:
    chaine = "Bonjour!"
    if is_even_len(chaine):
        print(f"Le nombre de caractère dans la chaine {chaine} est pair")
    else:
        print(f"Le nombre de caractère dans la chaine {chaine} est impair")

    chaine = "salut monde!"
    print(f"On supprime le 3e caratère dans la chaine: {chaine}. Résultat : {remove_third_char(chaine)}")

    chaine = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: {chaine}. Résultat : {replace_char(chaine, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans hello world est : {get_number_of_char(chaine, 'l')}")
    
    chaine = "Baby shark doo doo doo doo doo doo"
    print(f"L'occurence du mot doo dans la chaine {chaine} est: {get_number_of_words(chaine, 'doo')}")


if __name__ == '__main__':
    main()
