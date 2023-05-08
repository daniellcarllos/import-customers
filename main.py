import import_customers


from argparse import ArgumentParser

parser = ArgumentParser(description=" Importa e atualiza a base de clientes do projeto eco aparti de um arquivo TXT/CSV, é necessiro realizar a configuração para normalização")

parser.add_argument(
    '-d', '--delimiter',
    help="""delimiter é utilizado para separar os dados/coluna de um aquivo CSV informe o caractere entre ASPAS
    default = ',' """,
    type=str,
    metavar='STRING',
    default=',',
    required=False
)

parser.add_argument(
    '-p', '--path_file',
    help=""" Local do arquivo da base do arquivo de importação """,
    type=str,
    metavar='STRING',
    required=True
)
args = parser.parse_args()

if __name__ == '__main__':
    import_customers.importar_dados(args.path_file, args.delimiter)
