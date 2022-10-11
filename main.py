
from combine import combine
from siasus import siasus_extrair_informacoes_dado_filtro
from sihsus import sihsus_extrair_informacoes_dado_filtro


def sia_sus_gerar_procedimentos_por_municipio_ano_mes():
    filtro = {
        "municipio": "manaus",
        "ano": "2020",
        "mes": "08",
        "formatar_caminho_arquivo": lambda filtro: f'./data/siasus_municipio_ano_mes/{filtro["municipio"]}_{filtro["ano"]}_{filtro["mes"]}.csv'
    }
    for mes in ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]:
        filtro["mes"] = mes
        siasus_extrair_informacoes_dado_filtro(filtro)
    combine("./data/siasus_municipio_ano_mes", "sia_sus_manaus.csv")


def sia_sus_gerar_procedimentos_por_municipio_ano_mes_sexo():
    filtro = {
        "municipio": "manaus",
        "ano": "2020",
        "formatar_caminho_arquivo": lambda filtro: f'./data/siasus_municipio_ano_mes_sexo/{filtro["municipio"]}_{filtro["ano"]}_{filtro["mes"]}_{filtro["sexo"]}.csv'
    }
    for mes in ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]:
        filtro["mes"] = mes
        for sexo in ["M", "F", "N"]:
            filtro["sexo"] = sexo
            siasus_extrair_informacoes_dado_filtro(filtro)
    combine("./data/siasus_municipio_ano_mes_sexo", "sia_sus_manaus.csv")


def sih_sus_gerar_procedimentos_por_municipio_ano_mes():
    filtro = {
        "municipio": "manaus",
        "ano": "2020",
        "mes": "08",
        "formatar_caminho_arquivo": lambda filtro: f'./data/sihsus_municipio_ano_mes/{filtro["municipio"]}_{filtro["ano"]}_{filtro["mes"]}.csv'
    }
    for mes in ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]:
        filtro["mes"] = mes
        sihsus_extrair_informacoes_dado_filtro(filtro)

    combine("./data/sihsus_municipio_ano_mes", "sih_sus_manaus.csv")
