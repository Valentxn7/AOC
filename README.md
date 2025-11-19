# 🎄 Advent of Code - Validation Automatique

Ce dépôt permet de valider automatiquement vos solutions pour les défis **Advent of Code** demandés dans les TPs.

## Fonctionnement

Chaque fois que vous poussez votre code sur GitLab, un pipeline CI/CD se déclenche automatiquement pour :
- Tester vos solutions Python et/ou Go
- Vérifier que vos résultats correspondent aux sorties attendues
- Vérifier l'éfficacité de vos solutions
- Générer des statistiques de complétion détaillée pour les enseignants

## Structure du dépôt

Organisez votre code selon la structure suivante :

```
<année>/
  day<jour>/
    solution1.py      # Solution partie 1 en Python
    solution2.py      # Solution partie 2 en Python
    solution1.go      # Solution partie 1 en Go
    solution2.go      # Solution partie 2 en Go
```

**Exemple :**
```
2024/
  day1/
    solution1.py
    solution2.py
    solution1.go
    solution2.go
  day5/
    solution1.py
    solution2.py
```

## Utilisation

### 1. Cloner le dépôt
```bash
git clone <url-de-votre-depot>
cd <nom-du-depot>
```

### 2. Créer vos solutions

#### Python
Les scripts Python doivent :
- Accepter le chemin du fichier d'entrée comme argument : `solution1.py input.txt`
- Afficher **uniquement** le résultat final sur la sortie standard (stdout)

**Exemple Python :**
```python
import sys

def solve(input_file):
    with open(input_file, 'r') as f:
        # Votre code ici
        result = ...
    return result

if __name__ == "__main__":
    result = solve(sys.argv[1])
    print(result)
```

#### Go
Les programmes Go doivent :
- Utiliser `//go:embed` pour inclure le fichier `input.txt`
- Afficher **uniquement** le résultat final sur la sortie standard (stdout)

**Exemple Go :**
```go
package main

import (
    _ "embed"
    "fmt"
    "strings"
)

//go:embed input.txt
var input string

func main() {
    lines := strings.Split(strings.TrimSpace(input), "\n")
    
    // Votre code ici
    result := solve(lines)
    fmt.Println(result)
}

func solve(lines []string) int {
    // Votre logique de résolution
    return 0
}
```

### 3. Pousser votre code

```bash
git add .
git commit -m "Add solution for day X"
git push
```

### 4. Vérifier les résultats

- Rendez-vous dans **CI/CD > Pipelines** sur GitLab
- Consultez les résultats des tests pour chaque jour
- Les tests échoués afficheront la différence entre votre résultat et le résultat attendu

## Jours requis pour les TPs

Le pipeline testera automatiquement les jours demandés dans les TPs. Vous pouvez également ajouter d'autres jours si vous souhaitez valider vos solutions supplémentaires !

## Points importants

1. **Format de sortie** : Vos scripts doivent afficher **uniquement** le résultat final, sans texte supplémentaire
2. **Fichier d'entrée** : Le fichier `input.txt` est fourni automatiquement par le pipeline
   - **Python** : Passé en argument de ligne de commande
   - **Go** : Doit être embarqué avec `//go:embed input.txt`
3. **Nom des fichiers** : Respectez exactement la nomenclature `solution1.py`, `solution2.py`, `solution1.go`, `solution2.go`
4. **Structure des dossiers** : Utilisez le format `<année>/day<jour>/`
5. **Go embed** : N'oubliez pas l'import `_ "embed"` et la directive `//go:embed input.txt`

## Dépannage

### Mon test échoue alors que ma solution semble correcte
- Vérifiez que votre script n'affiche **que** le résultat (pas de messages de debug)
- Assurez-vous qu'il n'y a pas d'espace ou de retour à la ligne supplémentaire

### Le pipeline ne se déclenche pas
- Vérifiez que vous avez bien poussé vos modifications sur GitLab
- Assurez-vous que votre dépôt n'est pas un dépôt de type `_pipeline`
- Vérifiez que vous respectez la bonne arborecense de fichiers

### Mon fichier n'est pas testé
- Vérifiez la structure des dossiers et le nom des fichiers
- Le fichier doit exister dans le chemin exact : `<année>/day<jour>/solution<partie>.<extension>`


Bon courage pour vos défis Advent of Code !
