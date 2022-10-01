import codecs

import pandas as pd
import requests
from bs4 import BeautifulSoup

municipio_selecionado = "130260"


def read_from_tabnet_page():
    url = 'http://tabnet.datasus.gov.br/cgi/tabcgi.exe?sia/cnv/qbam.def'
    data = {
        "Linha": "Procedimento",
        "Coluna": "Ano_processamento",
        "Incremento": "Qtd.aprovada",
        "Arquivos": "qbam2207.dbf",
        "pesqmes1": "",
        "SMunic%EDpio": "38",
        "SRegi%E3o_de_Sa%FAde_%28CIR%29": "TODAS_AS_CATEGORIAS__",
        "SMacrorregi%E3o_de_Sa%FAde": "TODAS_AS_CATEGORIAS__",
        "SDivis%E3o_administ_estadual": "TODAS_AS_CATEGORIAS__",
        "pesqmes5": "Digite+o+texto+e+ache+f%E1cil",
        "SMicrorregi%E3o_IBGE": "TODAS_AS_CATEGORIAS__",
        "SRegi%E3o_Metropolitana_-_RIDE": "TODAS_AS_CATEGORIAS__",
        "pesqmes7": "Digite+o+texto+e+ache+f%E1cil",
        "SProcedimento": "TODAS_AS_CATEGORIAS__",
        "SGrupo_procedimento": "TODAS_AS_CATEGORIAS__",
        "pesqmes9": "Digite+o+texto+e+ache+f%E1cil",
        "SSubgrupo_proced.": "TODAS_AS_CATEGORIAS__",
        "pesqmes10": "Digite+o+texto+e+ache+f%E1cil",
        "SForma_organiza%E7%E3o": "TODAS_AS_CATEGORIAS__",
        "SComplexidade": "TODAS_AS_CATEGORIAS__",
        "SCar%E1ter_Atendiment": "TODAS_AS_CATEGORIAS__",
        "SDocumento_registro": "TODAS_AS_CATEGORIAS__",
        "pesqmes14": "Digite+o+texto+e+ache+f%E1cil",
        "SFaixa_et%E1ria": "TODAS_AS_CATEGORIAS__",
        "SSexo": "TODAS_AS_CATEGORIAS__",
        "pesqmes16": "Digite+o+texto+e+ache+f%E1cil",
        "SProfissional_-_CBO": "TODAS_AS_CATEGORIAS__",
        "formato": "table",
        "mostre": "Mostra"
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded',
               'User-Agent': 'insomnia/2022.6.0'}
    res = requests.post(url,
                        headers=headers,
                        data=data)


read_from_tabnet_page()


def read_data_from_file():
    f = codecs.open("exemplo.html", 'r')
    html_page = f.read()
    return html_page


html_page = read_data_from_file()
soup = BeautifulSoup(html_page, 'html.parser')
table = soup.find('table', {"class": "tabdados"})

table_rows = table.find_all('tr')
table_thead = table.find_all('thead')

table_thread_rows = table_thead[0].find_all('tr')
table_thread_titles = table_thread_rows[1].find_all('th')


data_list = []

for row in table_rows[4:]:
    data = {}
    cells = row.find_all('td')
    for i in range(3):
        data[table_thread_titles[i].get_text().lower()] = " ".join(cells[i].get_text().strip().split())
    data["municipio"] = municipio_selecionado
    data_list.append(data)

data_frame = pd.DataFrame(data_list, columns=data_list[0].keys())

data_frame.to_csv('output.csv', index=False)
print("Fim")