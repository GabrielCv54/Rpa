import os
import argparse as arg
#import selenium

parser = arg.ArgumentParser(description='Limpa o diretório e coloca os arquivos nas pastas correspondentes')

parser.add_argument(
    '--path',
    type=str,
    default='.',
    help='caminho do diretório a ser limpo.',
    )

args = parser.parse_args()
path = args.path

directory_cont = os.listdir(path)

path_directory_cont = [os.path.join(path, doc) for doc in directory_cont]

document = [doc for doc in path_directory_cont if os.path.isfile(doc)]
folders = [folder for folder in path_directory_cont if os.path.isdir(folder)]

moved = 0
folders_created = []

for d in document:
    full_doc_path, filetype = os.path.splitext(d)
    doc_path = os.path.dirname(full_doc_path)
    doc_name = os.path.basename(full_doc_path)

    print(filetype)
    print(full_doc_path)
    print(doc_path)
    print(doc_name)
    

    if doc_name == 'directory_clear' or doc_name.startswith('.'):
     continue

    subfolder_path = os.path.join(path,filetype[1:].lower())

    if subfolder_path not in folders:
       try:
          os.mkdir(subfolder_path)
          folders_created.append(subfolder_path)
          print(f'A pasta {subfolder_path} foi criada.')
       except FileExistsError as error:
          print(f'A pasta já existe em {subfolder_path} ... {error}')
          
    new_doc_path = os.path.join(subfolder_path,doc_name) + filetype
    moved+=1

    print(f'O arquivo {d} foi movido paa a pasta {new_doc_path}')
print(f'Renomeados {moved} de {len(document)} arquivos')

'''print(f'Limpando: {len(document)} de {len(directory_cont)} elementos')'''