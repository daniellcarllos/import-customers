import os
from dotenv import load_dotenv
load_dotenv()

nome_tabela = os.getenv('DB_TABLE_NAME')

# Import file location

delimiter = os.getenv('DELIMITER')

# Import file column names, DF normalization will be performed

UC = 'uc'
NUM_CLI = ''
TITULAR = "titular"
CPF = "cpf"
SITUACAO = 'UEE.COD_SITU_UEE'
ENDERECO = "logradouro"
BAIRRO = "bairro"
MUNICIPIO = "municipio"


db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_DATABASE'),
}