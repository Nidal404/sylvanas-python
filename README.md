### Environnment local
```
.\.venv\Scripts\activate.bat
pip -V (If you are running the virtual env. it'll show the path to the env.'s location.)
```


### Générer un fichier propre requirements.txt
```
pip install pipreqs
pipreqs C:\Users\Nidal\Dev\Projects\Sylvanas --force
```


### Installer / Désinstaller / Mettre à jour le package Auria
```
pip install git+https://github.com/Nidal404/sylvanas-python.git
pip uninstall sylvanas-python

Le fichier setup, permet d'installer les dépendances du projet (voir pour fixer les versions en cas de problème)
```