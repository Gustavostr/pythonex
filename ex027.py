"""Faça um programa que leia o nome completo de uma pessoa e mostre qual o primeiro e o ultimo nome"""
name_user = str(input("Digite seu nome completo: "))
print("O primeiro nome é: {}.".format(name_user.split()[0]))
print("O último nome é: {}".format(name_user.split().pop()))