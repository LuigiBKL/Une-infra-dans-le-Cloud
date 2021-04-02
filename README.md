# Une-infra-dans-le-Cloud
Contexte du projet Vous devez mettre en place, pour votre équipe, une infrastructure. Le choix se porte sur AWS, car vous n'avez personne en interne avec les compétences requises pour déployer et maintenir une infrastructure physique. De plus, les services élastiques proposées par Amazon répondent au besoin de scalabilité de l'infra.  L'infrastructure doit inclure une base PostgreSQL (sur RDS, donc) et une API proposant l'accès à cette base (sur EC2). Le fichier SQL servant à créer la base doit être sauvegardé sur S3.  L'API est codée en Python, langage largement maîtrisé par les équipes.


- Une base de données PostgreSQL avec RDS,
- Y importer les données proposées dans le lien ci-dessous

![image](/images/base_de_donnees.png)

- Mettre en place un serveur avec EC2 pour accueillir l'appli Python

![image](/images/EC2.png)

- Ajouter du code Python test qui se connecte à la base et exécute au moins 2 requêtes (au choix dans celles proposées dans les exercices)

`Les fichiers utilisé pour cette tâches sont les suivans` :
- [api](/API/api.py)
- [config](/API/config.py)
- [aws.ini](/API/aws.ini)

- Créer un bucket sur S3 pour sauvegarder la fichier SQL.

![image](/images/s3.png)

## Installation:

Afin de faciliter les choses et pour la sécurité des données on a décidé d'utiliser des containers, et donc un [docker-compose.yml](docker-compose.yml), qui pour être executé aura besoin des fichiers [Dockerfile](Dockerfile), et [requirements.txt](requirements.txt). 

Tous les fichiers necessaires à ce projet seront déposé sur notre machine virtuelle (AWS) à l'aide d'une extension appelée `remote ssh` de `vs code` 

![image](/images/remote_ssh_vscode_png)

Une fois nos fichiers dépose on aura plus qu'à nous situer dans notre dossier de travail avec la commande `cd `de l'invite de commande et ensuite lancer la commande `docker-compose up -d`

- A noter que si vous utiliser Amazon linux plutôt qu'Ubuntu, je vous invite à suivre ce [lien](https://gist.github.com/npearce/6f3c7826c7499587f00957fee62f8ee9) car Amazon linux utilise `yum` de base.
- Ne pas oublier aussi de bien autoriser les adresses ip à se connecter à votre port de fastapi dans le groupe de sécurité

![image](/images/regles_entrantes.png)


Tout ceci terminé nous n'avons plus qu'à nous connecter en tampant dans la barre d'adresse de notre navigateur `l'adresse ip de notre seveur EC2:le port attribuer à notre fastapi`

![image](fastapi.png)

