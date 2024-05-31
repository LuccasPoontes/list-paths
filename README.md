# Listador de Estrutura de Arquivos

Este projeto é um script em Python que lista todos os arquivos e diretórios a partir de um diretório raiz especificado e salva essa estrutura em um arquivo de texto.

## Funcionalidades

- Percorre recursivamente os diretórios a partir de um diretório raiz especificado.
- Registra a estrutura de diretórios e nomes de arquivos.
- Salva a saída em um arquivo de texto.

## Requisitos

- Python 3.x
- Módulo `os` (incluso na biblioteca padrão do Python)

## Uso

1. Clone o repositório:
    ```bash
    git clone https://github.com/seuusuario/list-paths.git
    cd listador-de-arquivos
    ```

2. Certifique-se de ter o Python 3 instalado. Você pode baixá-lo em [python.org](https://www.python.org/).

3. Execute o script:
    ```bash
    python listar_arquivos.py
    ```

## Exemplo

O script irá listar todos os arquivos e diretórios a partir do diretório raiz especificado e salvar a estrutura em um arquivo chamado `file_structure.txt`.

### Script

```python
import os

def list_files_and_directories(root_dir):
    file_structure = {}
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for dirname in dirnames:
            dir_full_path = os.path.join(dirpath, dirname)
            file_structure[dir_full_path] = []
        for filename in filenames:
            file_full_path = os.path.join(dirpath, filename)
            dir_only = os.path.dirname(file_full_path)
            if dir_only not in file_structure:
                file_structure[dir_only] = []
            file_structure[dir_only].append(filename)
    return file_structure

def save_to_file(file_structure, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for dirpath, files in file_structure.items():
            f.write(f'Directory: {dirpath}\n')
            for file in files:
                f.write(f'    {file}\n')
            f.write('\n')

if __name__ == '__main__':
    root_directory = r'C:\Users\luccas.faustino\Desktop'
    output_file = 'file_structure.txt'
    file_structure = list_files_and_directories(root_directory)
    save_to_file(file_structure, output_file)
    print(f'Report saved to {output_file}')


### Saída
O arquivo de saída file_structure.txt conterá uma lista formatada de diretórios e arquivos, como este exemplo:

          Directory: C:\Users\luccas.faustino\Desktop\Project
              file1.txt
              file2.py
          
          Directory: C:\Users\luccas.faustino\Desktop\Project\Subfolder
              file3.txt

### Agradecimentos
O script utiliza o módulo os para interagir com o sistema operacional.
Certifique-se de personalizar os links, nomes de repositórios e quaisquer outros detalhes específicos do projeto para adequá-los ao seu projeto real.
