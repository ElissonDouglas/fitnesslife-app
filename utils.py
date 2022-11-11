def ver_categoria_homens(valor: float) -> str:
    if valor < 20:
        return 'Categoria: IMC abaixo do normal'
    elif valor >= 20 and valor <= 24.9:
        return 'Categoria: IMC ideal'
    elif valor >= 25 and valor <= 29.9:
        return 'Categoria: Obesidade leve'
    elif valor >= 30 and valor <= 39.9:
        return 'Categoria: Obesidade moderada'
    else:
        return 'Categoria: Obesidade mórbida'
    

def ver_categoria_mulheres(valor: float) -> str:
    if valor < 19:
        return 'Categoria: IMC abaixo do normal'
    elif valor >= 19 and valor <= 23.9:
        return 'Categoria: IMC ideal'
    elif valor >= 24 and valor <= 28.9:
        return 'Categoria: Obesidade leve'
    elif valor >= 29 and valor <= 38.9:
        return 'Categoria: Obesidade moderada'
    else:
        return 'Categoria: Obesidade mórbida'
    

def calcula_agua(valor: float) -> str:
    qntd = 35 * valor
    return f'Você precisa beber pelo menos {round(qntd / 100 / 10, 1)}L de água por dia.\nBEBA ÁGUA RAPAZ!'
    