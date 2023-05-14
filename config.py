import os

from dotenv import load_dotenv  # type: ignore

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


def mod_debug(debug: bool):
    if debug:
        db_config = {
            'host': os.getenv('DB_HOST_DEBUG'),
            'user': os.getenv('DB_USER_DEBUG'),
            'password': os.getenv('DB_PASSWORD_DEBUG'),
            'database': os.getenv('DB_DATABASE_DEBUG'),
        }
    else:
        db_config = {
            'host': os.getenv('DB_HOST'),
            'user': os.getenv('DB_USER'),
            'password': os.getenv('DB_PASSWORD'),
            'database': os.getenv('DB_DATABASE'),
        }
    return db_config


if __name__ == "__main__":
    ...
