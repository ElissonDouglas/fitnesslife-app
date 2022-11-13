import PySimpleGUI as sg
from utils import ver_categoria_homens, ver_categoria_mulheres, calcula_agua
from webbrowser import open_new
from frases_request import frase_motivacional


def beneficios():
    layout = [
        [sg.Image(filename='imagens/beneficios.png')]
    ]
    janela = sg.Window('Benefícios da água', layout=layout)
    while True:
        evento, valores = janela.read()
        if evento == sg.WIN_CLOSED:
            break
    janela.close()


def falta_de_agua():
    layout = [
        [sg.Image(filename='imagens/pouca_agua.png')]
    ]
    janela = sg.Window('Sinais de que você bebe pouca água', layout=layout)
    while True:
        evento, valores = janela.read()
        if evento == sg.WIN_CLOSED:
            break
    janela.close()


def agua():
    layout = [
        [sg.Push(), sg.Text('Seu peso(kg):'), sg.Input(
            key='peso', size=4), sg.Push()],
        [sg.Push(), sg.Button('Calcular'), sg.Push()],
        [sg.Push(), sg.Text('', key='resultado', size=(
            30, 3), justification='center'), sg.Push()],
        [sg.Push(), sg.Button('Benefícios de se beber água', key='Beneficios'), sg.Push()],
        [sg.Push(), sg.Button('Sinais de que você bebe pouca água',
                              key='pouca_agua'), sg.Push()]
    ]
    janela = sg.Window('Calcular Água', layout=layout, size=(400, 210))
    while True:
        evento, valores = janela.read()
        if evento == sg.WIN_CLOSED:
            break
        elif evento == 'Calcular':
            try:
                calculo = calcula_agua(float(valores['peso']))
                janela['resultado'].update(calculo)
            except:
                janela['resultado'].update('ERRO: Valor inválido!')
        elif evento == 'Beneficios':
            beneficios()
        elif evento == 'pouca_agua':
            falta_de_agua()

    janela.close()


def busca_frases():
    layout = [
        [sg.Text('Clique no botão para gerar uma frase motivacional!',
                 key='frase', justification='center', size=(50, 4))],
        [sg.Push(), sg.Button('Gerar', key='gerar_frase'), sg.Push()]
    ]
    janela = sg.Window('Frases Motivacionais', layout=layout)
    while True:
        evento, valores = janela.read()
        if evento == sg.WIN_CLOSED:
            break
        elif evento == 'gerar_frase':
            janela['frase'].update(frase_motivacional())
    janela.close()


def tabela():
    layout = [
        [sg.Image(filename='imagens/tabela1.png')]
    ]
    janela = sg.Window('Tabela IMC', layout=layout)

    while True:
        evento, valores = janela.read()
        if evento == sg.WIN_CLOSED:
            break
    janela.close()


def calculo_imc():
    opcoes = ['Masculino', 'Feminino']
    layout = [
        [sg.Text('Seu peso(kg)', justification='center', size=(100, 1))],
        [sg.Input(size=(100, 1),  key='peso', justification='center')],
        [sg.Text('Sua altura(m):', justification='center', size=(100, 1))],
        [sg.Input(size=(100, 1),  key='altura', justification='center')],
        [sg.Text('Sexo:'), sg.Combo(['Masculino', 'Feminino'],
                                    default_value='Masculino', key='sexo')],
        [sg.Push(), sg.Button('Calcular IMC'), sg.Push()],
        [sg.Push(), sg.Text('', key='resultado'), sg.Push()],
        [sg.Push(), sg.Button('Visualizar Tabela IMC', key='visualizar'), sg.Push()]
    ]

    janela = sg.Window(title='Calculadora IMC', layout=layout, size=(250, 300))

    while True:
        evento, valores = janela.read()
        if evento == sg.WIN_CLOSED:
            break
        elif evento == 'Calcular IMC':
            try:
                peso = float(valores['peso'])
                altura = float(valores['altura'])
                calculo = peso / (altura * altura)
                txt = f"Seu IMC é {round(calculo, 2)}\n{ver_categoria_mulheres(calculo) if valores['sexo'] == 'Feminino' else ver_categoria_homens(calculo)}"
                janela['resultado'].update(txt)
            except:
                janela['resultado'].update('ERRO: Valores inválidos!')
        elif evento == 'visualizar':
            tabela()

    janela.close()


def main():
    sg.theme('LightBlue2')
    layout_esquerda = [
        [sg.Image(filename='imagens/logo_inicio.png'), ]]
    layout_direita = [
        [sg.Image(filename='imagens/logotipo.png')],
        [sg.Push(), sg.Text('O que deseja fazer?'), sg.Push()],
        [sg.Push(), sg.Button('Calculadora IMC', key='imc'), sg.Push()],
        [sg.Push(), sg.Button('Gerar frases motivacionais', key='gerador'), sg.Push()],
        [sg.Push(), sg.Button('Calcular quantidade de água',
                              key='calcular_agua'), sg.Push()],
        [sg.Push(), sg.Button('Sobre o App', key='sobre'), sg.Push()],
    ]
    layout = [
        [sg.Column(layout_esquerda), sg.VSeparator(),
         sg.Column(layout_direita)]
    ]
    janela = sg.Window('FitnessLife App', layout=layout)

    while True:
        evento, valores = janela.read()
        if evento == sg.WIN_CLOSED:
            break
        elif evento == 'imc':
            calculo_imc()
        elif evento == 'gerador':
            busca_frases()
        elif evento == 'calcular_agua':
            agua()
        elif evento == 'sobre':
            open_new('https://github.com/ElissonDouglas/fitnesslife-app')

    janela.close()


if __name__ == '__main__':
    main()
