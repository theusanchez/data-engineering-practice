# Importando bibliotecas que serão utilizadas.
import zipfile
import os
import requests


# Criando váriaveis que serão utilizadas.
download_uris = [
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip'
]
file_names = []

# Lidar com os diretórios da máquina.
# print(os.getcwd()) # Comando para verificar qual é o diretório que está sendo utilizado no momento
# print(os.listdir()) # Comando usado para listar diretórios

os.mkdir('Downloaded_Files2')  # Comando usado para criar um novo diretório.
os.chdir('Downloaded_Files2')  # Comando utilizado para mudar de diretório.


def main():

    # Salvar os nomes dos arquivos através da URL.
    for x in download_uris:
        file_names.append(x.split('/')[-1])
    
    # Baixar os arquivos
    for x in download_uris:
        response = requests.get(x)
        nomearquivo = x.split('/')[-1]
        open(nomearquivo, 'wb').write(response.content)
    
    for x in file_names:
        try:
            with zipfile.ZipFile(x) as zip_ref:
                zip_ref.extractall()
        except Exception as e:
            print(e)
            pass
        
    pass


if __name__ == '__main__':
    main()
