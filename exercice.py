#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def get_first_part_of_name(name: str) -> str:
    premier_prenom = name.split("-")[0].title()
    return f"Bonjour, {premier_prenom}"


def get_random_sentence(animals: tuple, adjectives: tuple, fruits: tuple) -> str:
    return (
        f"Aujourd'hui, j'ai vu un {random.choice(animals)} "
        + f"s'emparer d'un panier {random.choice(adjectives)} "
        + f"plein de {random.choice(fruits)}."
    )


def cesar_cipher(text: str, shift: int, reverse: bool = False) -> str:
    alpha_maj = (ord("A"), ord("Z"))

    encrypted_string = ""

    if reverse:
        shift = -shift

    for char in text:
        # use only uppercase
        c_id = ord(char.upper())

        # check if needs to be shifted
        if alpha_maj[0] <= c_id <= alpha_maj[1]:
            # remove base, shifting between A - Z
            shifted_id = (c_id - alpha_maj[0] + shift) % 26

            # shift back character before adding it
            new_char = chr(shifted_id + alpha_maj[0])
        else:
            new_char = char

        encrypted_string += new_char

    return encrypted_string


def encrypt(text: str, shift: int) -> str:
    return cesar_cipher(text, shift)


def decrypt(encrypted_text: str, shift: int) -> str:
    return cesar_cipher(encrypted_text, shift, reverse=True)


if __name__ == "__main__":
    parrot = "jEaN-MARC"
    print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

    animals = ("chevreuil", "chien", "pigeon")
    adjectives = ("rouge", "officiel", "lourd")
    fruits = ("pommes", "kiwis", "mangue")
    print(get_random_sentence(animals, adjectives, fruits))

    print(encrypt("ABC", 1))
    print(encrypt("abc 123 XYZ", 3))
    print(decrypt("DEF 123 ABC", 3))
