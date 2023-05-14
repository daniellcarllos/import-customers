from argparse import ArgumentParser

import import_customers

parser = ArgumentParser(description=" Importa e atualiza a base de clientes do\
                         projeto eco a parti de um arquivo TXT/CSV, é \
                         necessario realizar a configuração para normalização")

parser.add_argument('-D', '--debug',
                    action='store_true',
                    help='Ativa o modo de depuração \
                          e salva dados no banco local')

parser.add_argument(
    '-d', '--delimiter',
    help="""delimiter é utilizado para separar os dados/coluna de um aquivo \
          CSV informe o caractere entre ASPAS
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
    import_customers.import_data(args.path_file, args.delimiter, args.debug)
