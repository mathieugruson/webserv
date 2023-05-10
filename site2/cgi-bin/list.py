#!/usr/bin/env python
print ("Content-type: text/html\n\n")
print()
import os
import cgi

# Fonction pour générer une liste de fichiers dans le répertoire courant
def list_files():
    # Ouvre le répertoire courant
    files = os.listdir(".")
    # Crée une liste HTML de liens vers chaque fichier
    file_list = "<ul>\n"
    for f in files:
        # Exclut les fichiers cachés (commençant par un point)
        if not f.startswith("."):
            # Ajoute un élément de liste avec un lien hypertexte vers chaque fichier
            file_list += "<li>" + f + "</li>\n"
        # file_list += "<li><a href=\"/mnt/nfs/\">blabla</a></li>\n"
    file_list += "</ul>"
    # Retourne la liste de fichiers générée
    return file_list

# Code HTML de la page
print ("<html>")
print ("<head>")
print ("<meta charset='utf-8'>")
print ("<title>Liste des fichiers dans le répertoire courant</title>")
print ("</head>")
print ("<body>")
print ("<h1>Liste des fichiers dans le répertoire courant :</h1>")
print (list_files()) # Appelle la fonction list_files() pour générer la liste de fichiers
print ("</body>")
print ("</html>")
