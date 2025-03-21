import requests
import pandas as pd


def def_trimestre(data):
    url = f"https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/MeiosdePagamentosTrimestralDA(trismestre=@trimestre)?@trimestre='{data}'&$format=json"
    req = requests.get(url)
    dados = req.json()
    df = pd.json_normalize(dados['value'])
    return print(df)

def_trimestre('20191')

