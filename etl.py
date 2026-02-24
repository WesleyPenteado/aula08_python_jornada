import pandas as pd
import os
import glob

# uma funcao de extract que le e consolida os json

pasta = 'data'
arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
print(arquivos_json)

# uma funcao que transforma

# uma funcao que da load em csv ou parquet