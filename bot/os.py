import os 
import shutil
import argparse

extensions = {
    "imagens": ['.jpg','.jpeg','.png','.gif'],
    "documentos":['.pdf','.docx','.txt'],
    'videos':['.mp4','.mov','.avi'],
    'músicas':['.mp3','.wav']
}

parser = argparse.ArgumentParser(description='Organização de arquivos pro tipo')
parser.add_argument('diretório',help='Caminho do diretório a ser organizado')
args = parser.parse_args()

def organization(directory):
    for archive in os.listdir(directory):
        full_path = os.path.join(directory,archive)
        if os.path.isfile(full_path):
            _, extend = os.path.splitext(archive)
            for pasta , lista_ext in extensions.items():
                if extend.lower() in lista_ext:
                    destiny = os.path.join(directory, pasta)
                    os.makedirs(destiny, exist_ok=True)
                    shutil.move(full_path, os.path.join(destiny,archive))
                    print(f'Movido: {archive} -> {pasta}')
                    break
            
if __name__ == '__main__':
    organization(args.directory)

'''user = os.environ.get('USERNAME')
directory = os.getcwd()
print(f'usuário : {user}')
print(f'Diretório : {directory}')

os.system('ls')

file = os.path.join('documents','rpa','Email','main.py')
print(file)'''
