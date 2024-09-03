# Mentorat_EPL_2024-Python2

## Activité 1
### Exercice 1
Ecrire un programme qui fait le calcule entre deux nombres en fonction de l'opération de l'utilisateur

### Exercice 2
Ecrire un programme qui calcule la distance entre deux points $A(x_a, y_a)$ et $B(x_b, y_b)$. La formule de calcul de la distance entre deux points est donnée sous la forme suivante :

$d(A, B) = \sqrt{(x_a - x_b)^2 + (y_a - y_b)^2}$

### Exercice 3 : Première partie du jeu de devinette
Dans cette partie, l'utilisateur est amené à fixer la valeur maximale du nombre aléatoire à générer.  
Les éléments essentiels dans cet exercice sont :
- La génération d'un nombre aléatoire
- Contrôle de la saisie de l'utilisateur
- Le but dans cet exercice est d'aider l'utilisateur à gagner

### Exercice 4 : Deuxième partie du jeu de devinette
Dans cette partie, on permet à l'utilisateur de jouer selon le niveau de difficulté qui dépend de la valeur maximale du nombre aléatoire à générer.
- Facile : 100
- Moyen : 500
- Difficile : 1000
Egalement pour cette partie le but est de permettre au joueur de gagner quelqu'en soit le nombre d'essais.

### Exercice 5 : Troisième partie du jeu de devinette
Dans cette partie on fixe ne nombre de tentatives à 15. On se permet de qualifier chaque joueur en fonction du nombre de tentatives réalisé :
- [1 - 3] tentatives > Voyant
- [4 - 6] tentatives => Sage Voyant
- [7 - 9] tentatives => Apprenti Voyant
- [10 et plus] tentatives => Pusillanime
Quelques notions ont aussi été introduites :
- Score : $Score = 1 - \frac{attempts}{15}$ (sous forme de pourcentage)
- Historisation des tentatives
- Ecart-Type des tentatives
- Moyenne olympique des tentatives
