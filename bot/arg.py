import argparse
import webbrowser

parser = argparse.ArgumentParser(description='Exemplo de estudo')

parser.add_argument('-s',action='store_true',help='ativa a opção S')
parser.add_argument('-p',action='store_true',help='Ativa a opção P')
parser.add_argument('-x',action='store_true',help='Ativa a opção X')
parser.add_argument('-t',action='store_true',help='ativa a opção T')
parser.add_argument('-o',action='store',help='Especifica um valor para a opção O')

args = parser.parse_args()
 
def argument(args):
    if args.s:
        print('S ativado')
    elif args.p:
        print('P ativado')
    elif args.x:
        print('X ativado')
    elif args.t:
        print('T ativado')
    elif args.o:
        print(f'O valor de O é {args.o}')

