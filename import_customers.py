import mysql.connector  # type: ignore
import numpy as np  # type: ignore
import pandas as pd
from mysql.connector import errorcode  # type: ignore
from tqdm import tqdm

import config


def import_data(path: str, delimiter: str, debug: bool):

    config_db = config.mod_debug(debug)

    tqdm.pandas()

    # Construct connection string
    try:
        conn = mysql.connector.connect(**config_db)
        print("Connection established")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with the user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursor = conn.cursor()

    # Criando o Dataframe aparti do arquivo (.txt,.csv)
    df = pd.read_csv(path, delimiter=delimiter, converters={
                     config.CPF: str}, encoding='ISO-8859-1')

    # Renomeando colunas para normalizar a base

    df.rename(columns={config.UC: 'UC'}, inplace=True)
    df.rename(columns={config.NUM_CLI: 'CC'}, inplace=True)
    df.rename(columns={config.CPF: 'CPF'}, inplace=True)
    df.rename(columns={config.TITULAR: 'TITULAR'}, inplace=True)
    df.rename(columns={config.SITUACAO: 'STATUS_CLIENTE'}, inplace=True)
    df.rename(columns={config.ENDERECO: 'ENDERECO'}, inplace=True)
    df.rename(columns={config.BAIRRO: 'BAIRRO'}, inplace=True)
    df.rename(columns={config.MUNICIPIO: 'MUNICIPIO'}, inplace=True)

    # Apagando valores vazios
    df = df.fillna(value='')
    df = df.dropna(subset=['UC', 'CPF'], axis=0)

    # Alterando UC para inteiro os dados
    df['UC'] = df['UC'].astype(int)
    # Alterando CPF para str os dados
    df['CPF'] = df['CPF'].astype(str)

    uc = np.unique(df['UC'], return_counts=True)
    count_ = 0
    for key, valor in enumerate(uc[1]):
        if valor > 1:
            print(f'UC Duplicada: ', uc[0][key])
            count_ += 1
    print('Qauntidade de UC duplicadas: ', count_)

    # Apagando registro de UC duplicados
    df = df.drop_duplicates(subset=['UC'])

    # Inserindo as colunas no data frame
    df.loc[:, "id_posto_coleta"] = 0

    # Inserindo os dados no banco e criando as query
    # UC,CLIENTE,CPF,ENDERECO,BAIRRO,MUNICIPIO

    for index, row in tqdm(
            df.iterrows(),
            desc='Importação',
            total=df.shape[0]):

        query = f"""INSERT INTO {config.nome_tabela} (uc, titular, cpf,\
                            logradouro, bairro, municipio, id_posto_coleta)
                            VALUES (%s, %s, %s, %s, %s, %s, %s)
                            ON DUPLICATE KEY UPDATE cpf = VALUES(cpf),\
                            logradouro = VALUES(logradouro),\
                            bairro = VALUES(bairro),\
                            municipio= VALUES(municipio), \
                            titular= VALUES(TITULAR)"""
        values = (row.UC, row.TITULAR, row.CPF, row.ENDERECO,
                  row.BAIRRO, row.MUNICIPIO, row.id_posto_coleta)

        cursor.execute(query, values)  # type: ignore
        conn.commit()  # type: ignore

    cursor.close()  # type: ignore
    conn.close()  # type: ignore


if __name__ == "__main__":
    ...
