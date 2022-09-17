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


def encrypt(text, shift):
    return ""


def decrypt(encrypted_text, shift):
    return ""


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
