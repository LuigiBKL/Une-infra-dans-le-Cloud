# Une-infra-dans-le-Cloud
Contexte du projet Vous devez mettre en place, pour votre équipe, une infrastructure. Le choix se porte sur AWS, car vous n'avez personne en interne avec les compétences requises pour déployer et maintenir une infrastructure physique. De plus, les services élastiques proposées par Amazon répondent au besoin de scalabilité de l'infra.  L'infrastructure doit inclure une base PostgreSQL (sur RDS, donc) et une API proposant l'accès à cette base (sur EC2). Le fichier SQL servant à créer la base doit être sauvegardé sur S3.  L'API est codée en Python, langage largement maîtrisé par les équipes.


- Une base de données PostgreSQL avec RDS,
- Y importer les données proposées dans le lien ci-dessous

![image](/images/base_de_donnees.png)

- Mettre en place un serveur avec EC2 pour accueillir l'appli Python

![image](/images/EC2.png)

- Ajouter du code Python test qui se connecte à la base et exécute au moins 2 requêtes (au choix dans celles proposées dans les exercices)

`Les fichiers utilisé pour cette tâches sont les suivans` :
- [api]('/Api/api.py')
- [config]('/Api/config.py')
- [aws.ini]('/Api/aws.ini')

