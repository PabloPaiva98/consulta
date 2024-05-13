import streamlit as st
import pandas as pd
import numpy as np



seus_dados = [
    {"CÓDIGO": "ABCP11", "SETOR": "Shoppings", "COTA": 66.72, "LIQUIDEZ DIÁRIA": 877, "DIVIDENDO": 0.60, "RENTABILI": 8.38, "PATRIMÔNIO": 1120589958.80, "YIELD MENSAL": 0.88, "YIELD ANUAL": 7.92, "PAGAMENTO": "07/12/2023"},
    {"CÓDIGO": "BCRI11", "SETOR": "Títulos e Val. Mob.", "COTA": 98.70, "LIQUIDEZ DIÁRIA": 4524, "DIVIDENDO": 1.04, "RENTABILI": -1.38, "PATRIMÔNIO": 631486419.13, "YIELD MENSAL": 1.11, "YIELD ANUAL": 9.84, "PAGAMENTO": "15/12/2023"},
    {"CÓDIGO": "BPFF11", "SETOR": "Títulos e Val. Mob.", "COTA": 65.15, "LIQUIDEZ DIÁRIA": 1862, "DIVIDENDO": 0.62, "RENTABILI": 5.39, "PATRIMÔNIO": 330121846.94, "YIELD MENSAL": 0.91, "YIELD ANUAL": 11.71, "PAGAMENTO": "07/12/2023"},
    {"CÓDIGO": "BRCO11", "SETOR": "Logística", "COTA": 95.30, "LIQUIDEZ DIÁRIA": 28877, "DIVIDENDO": 0.65, "RENTABILI": 9.42, "PATRIMÔNIO": 1796316141.41, "YIELD MENSAL": 0.78, "YIELD ANUAL": 9.78, "PAGAMENTO": "14/12/2023"},
    {"CÓDIGO": "BRCR11", "SETOR": "Híbrido", "COTA": 57.88, "LIQUIDEZ DIÁRIA": 25011, "DIVIDENDO": 0.47, "RENTABILI": 1.84, "PATRIMÔNIO": 2673022814.44, "YIELD MENSAL": 0.75, "YIELD ANUAL": 9.25, "PAGAMENTO": "14/12/2023"},
    {"CÓDIGO": "BTLG11", "SETOR": "Logística", "COTA": 94.54, "LIQUIDEZ DIÁRIA": 28777, "DIVIDENDO": 0.74, "RENTABILI": 2.66, "PATRIMÔNIO": 2089628167.96, "YIELD MENSAL": 0.77, "YIELD ANUAL": 9.07, "PAGAMENTO": "26/12/2023"},
    {"CÓDIGO": "CBOP11", "SETOR": "Lajes Corporativas", "COTA": 48.61, "LIQUIDEZ DIÁRIA": 658, "DIVIDENDO": 1.12, "RENTABILI": -20.13, "PATRIMÔNIO": 105832738.70, "YIELD MENSAL": 0.39, "YIELD ANUAL": 4.43, "PAGAMENTO": "14/12/2023"},
    {"CÓDIGO": "CEOC11", "SETOR": "Lajes Corporativas", "COTA": 55.00, "LIQUIDEZ DIÁRIA": 254, "DIVIDENDO": 0.60, "RENTABILI": 7.72, "PATRIMÔNIO": 143085334.17, "YIELD MENSAL": 0.97, "YIELD ANUAL": 12.21, "PAGAMENTO": "14/12/2023"},
    {"CÓDIGO": "CNES11", "SETOR": "Lajes Corporativas", "COTA": 30.50, "LIQUIDEZ DIÁRIA": 39, "DIVIDENDO": 0.17, "RENTABILI": -7.81, "PATRIMÔNIO": 263957120.08, "YIELD MENSAL": 0.36, "YIELD ANUAL": 3.44, "PAGAMENTO": "28/12/2023"},
    {"CÓDIGO": "CPTS11", "SETOR": "Títulos e Val. Mob.", "COTA": 77.52, "LIQUIDEZ DIÁRIA": 71093, "DIVIDENDO": 0.58, "RENTABILI": -8.14, "PATRIMÔNIO": 2858127870.96, "YIELD MENSAL": 0.75, "YIELD ANUAL": 9.99, "PAGAMENTO": "19/12/2023"},
    {"CÓDIGO": "CVBI11", "SETOR": "Títulos e Val. Mob.", "COTA": 87.59, "LIQUIDEZ DIÁRIA": 23418, "DIVIDENDO": 1.10, "RENTABILI": 0.93, "PATRIMÔNIO": 1033370010.97, "YIELD MENSAL": 0.83, "YIELD ANUAL": 12.75, "PAGAMENTO": "18/12/2023"},
    {"CÓDIGO": "CXCE11B", "SETOR": "Outros", "COTA": 40.47, "LIQUIDEZ DIÁRIA": 697, "DIVIDENDO": 0.40, "RENTABILI": 2.56, "PATRIMÔNIO": 112377564.94, "YIELD MENSAL": 1.00, "YIELD ANUAL": 12.37, "PAGAMENTO": "15/12/2023"},
    {"CÓDIGO": "CXRI11", "SETOR": "Híbrido", "COTA": 63.40, "LIQUIDEZ DIÁRIA": 29, "DIVIDENDO": 0.56, "RENTABILI": -0.47, "PATRIMÔNIO": 130236645.57, "YIELD MENSAL": 0.74, "YIELD ANUAL": 9.97, "PAGAMENTO": "12/12/2023"},
    {"CÓDIGO": "CXTL11", "SETOR": "Logística", "COTA": 398.97, "LIQUIDEZ DIÁRIA": 13, "DIVIDENDO": 0.40, "RENTABILI": 7.84, "PATRIMÔNIO": 26235934.44, "YIELD MENSAL": 0.64, "YIELD ANUAL": 5.44, "PAGAMENTO": "15/12/2023"},
    {"CÓDIGO": "EDGA11", "SETOR": "Lajes Corporativas", "COTA": 19.57, "LIQUIDEZ DIÁRIA": 529, "DIVIDENDO": 0.12, "RENTABILI": -3.74, "PATRIMÔNIO": 252142355.54, "YIELD MENSAL": 0.33, "YIELD ANUAL": 6.88, "PAGAMENTO": "29/12/2023"},
    {"CÓDIGO": "FAED11", "SETOR": "Educacional", "COTA": 144.30, "LIQUIDEZ DIÁRIA": 356, "DIVIDENDO": 1.60, "RENTABILI": 14.97, "PATRIMÔNIO": 139752048.22, "YIELD MENSAL": 1.00, "YIELD ANUAL": 12.40, "PAGAMENTO": "14/12/2023"},
    {"CÓDIGO": "FCFL11", "SETOR": "Outros", "COTA": 113.20, "LIQUIDEZ DIÁRIA": 1377, "DIVIDENDO": 0.78, "RENTABILI": 7.57, "PATRIMÔNIO": 403588183.44, "YIELD MENSAL": 0.75, "YIELD ANUAL": 8.58, "PAGAMENTO": "26/12/2023"},
    {"CÓDIGO": "FIGS11", "SETOR": "Shoppings", "COTA": 48.45, "LIQUIDEZ DIÁRIA": 2258, "DIVIDENDO": 0.42, "RENTABILI": 0.00, "PATRIMÔNIO": 217963812.10, "YIELD MENSAL": 0.76, "YIELD ANUAL": 10.74, "PAGAMENTO": "14/12/2023"},
    {"CÓDIGO": "FIIB11", "SETOR": "Híbrido", "COTA": 458.98, "LIQUIDEZ DIÁRIA": 829, "DIVIDENDO": 4.10, "RENTABILI": 8.52, "PATRIMÔNIO": 316120517.04, "YIELD MENSAL": 0.70, "YIELD ANUAL": 9.03, "PAGAMENTO": "11/12/2023"},
    {"CÓDIGO": "FIIP11B", "SETOR": "Logística", "COTA": 145.01, "LIQUIDEZ DIÁRIA": 942, "DIVIDENDO": 1.35, "RENTABILI": -0.66, "PATRIMÔNIO": 172609310.05, "YIELD MENSAL": 0.85, "YIELD ANUAL": 11.09, "PAGAMENTO": "14/12/2023"},
    {"CÓDIGO": "FLMA11", "SETOR": "Híbrido", "COTA": 130.00, "LIQUIDEZ DIÁRIA": 413, "DIVIDENDO": 1.02, "RENTABILI": 17.51, "PATRIMÔNIO": 221247463.81, "YIELD MENSAL": 0.72, "YIELD ANUAL": 8.89, "PAGAMENTO": "14/12/2023"},
    {"CÓDIGO": "FLRP11", "SETOR": "Shoppings", "COTA": 1551.05, "LIQUIDEZ DIÁRIA": 8, "DIVIDENDO": 9.45, "RENTABILI": 43.32, "PATRIMÔNIO": 119158437.08, "YIELD MENSAL": 0.68, "YIELD ANUAL": 11.20, "PAGAMENTO": "14/12/2023"},
    {"CÓDIGO": "FPAB11", "SETOR": "Lajes Corporativas", "COTA": 139.99, "LIQUIDEZ DIÁRIA": 37, "DIVIDENDO": 1.65, "RENTABILI": -31.58, "PATRIMÔNIO": 281261368.63, "YIELD MENSAL": 0.45, "YIELD ANUAL": 9.82, "PAGAMENTO": "14/12/2023"},
    {"CÓDIGO": "GGRC11", "SETOR": "Logística", "COTA": 102.47, "LIQUIDEZ DIÁRIA": 10332, "DIVIDENDO": 0.95, "RENTABILI": 9.03, "PATRIMÔNIO": 981911300.68, "YIELD MENSAL": 0.82, "YIELD ANUAL": 9.96, "PAGAMENTO": "08/12/2023"},
    {"CÓDIGO": "GTWR11", "SETOR": "Lajes Corporativas", "COTA": 74.00, "LIQUIDEZ DIÁRIA": 5666, "DIVIDENDO": 0.79, "RENTABILI": 5.57, "PATRIMÔNIO": 1136410836.60, "YIELD MENSAL": 0.98, "YIELD ANUAL": 12.23, "PAGAMENTO": "14/12/2023"},
    {"CÓDIGO": "HAAA11", "SETOR": "Lajes Corporativas", "COTA": 79.76, "LIQUIDEZ DIÁRIA": 85, "DIVIDENDO": 0.57, "RENTABILI": -10.14, "PATRIMÔNIO": 309763908.88, "YIELD MENSAL": 0.58, "YIELD ANUAL": 5.72, "PAGAMENTO": "14/12/2023"},
    {"CÓDIGO": "HABT11", "SETOR": "Títulos e Val. Mob.", "COTA": 91.15, "LIQUIDEZ DIÁRIA": 49724, "DIVIDENDO": 1.17, "RENTABILI": -7.18, "PATRIMÔNIO": 810912436.00, "YIELD MENSAL": 1.15, "YIELD ANUAL": 15.32, "PAGAMENTO": "12/12/2023"},
    {"CÓDIGO": "HCRI11", "SETOR": "Hospital", "COTA": 227.13, "LIQUIDEZ DIÁRIA": 124, "DIVIDENDO": 3.49, "RENTABILI": -14.03, "PATRIMÔNIO": 61592370.00, "YIELD MENSAL": 1.05, "YIELD ANUAL": 14.51, "PAGAMENTO": "20/12/2023"},
    {"CÓDIGO": "HCTR11", "SETOR": "Outros", "COTA": 98.79, "LIQUIDEZ DIÁRIA": 29962, "DIVIDENDO": 1.10, "RENTABILI": -6.14, "PATRIMÔNIO": 2680557317.01, "YIELD MENSAL": 0.90, "YIELD ANUAL": 7.07, "PAGAMENTO": "18/12/2023"},
    {"CÓDIGO": "HFOF11", "SETOR": "Títulos e Val. Mob.", "COTA": 67.30, "LIQUIDEZ DIÁRIA": 16827, "DIVIDENDO": 0.62, "RENTABILI": -2.71, "PATRIMÔNIO": 1861309846.51, "YIELD MENSAL": 0.85, "YIELD ANUAL": 10.67, "PAGAMENTO": "14/12/2023"},
    {"CÓDIGO": "HGBS11", "SETOR": "Shoppings", "COTA": 185.66, "LIQUIDEZ DIÁRIA": 6046, "DIVIDENDO": 1.40, "RENTABILI": 23.65, "PATRIMÔNIO": 2219188710.93, "YIELD MENSAL": 0.88, "YIELD ANUAL": 10.25, "PAGAMENTO": "14/12/2023"},
    {"CÓDIGO": "HGCR11", "SETOR": "Títulos e Val. Mob.", "COTA": 100.85, "LIQUIDEZ DIÁRIA": 19936, "DIVIDENDO": 1.20, "RENTABILI": 6.53, "PATRIMÔNIO": 1556674946.53, "YIELD MENSAL": 0.98, "YIELD ANUAL": 13.21, "PAGAMENTO": "14/12/2023"},
    {"CÓDIGO": "HGLG11", "SETOR": "Logística", "COTA": 161.26, "LIQUIDEZ DIÁRIA": 27392, "DIVIDENDO": 2.20, "RENTABILI": 6.75, "PATRIMÔNIO": 3612959934.52, "YIELD MENSAL": 0.70, "YIELD ANUAL": 9.03, "PAGAMENTO": "14/12/2023"},
    {"CÓDIGO": "HGPO11", "SETOR": "Lajes Corporativas", "COTA": 254.61, "LIQUIDEZ DIÁRIA": 397, "DIVIDENDO": 1.60, "RENTABILI": 8.74, "PATRIMÔNIO": 524807114.32, "YIELD MENSAL": 0.57, "YIELD ANUAL": 7.21, "PAGAMENTO": "14/12/2023"},
    {"CÓDIGO": "HGRE11", "SETOR": "Lajes Corporativas", "COTA": 112.54, "LIQUIDEZ DIÁRIA": 16501, "DIVIDENDO": 1.10, "RENTABILI": -0.23, "PATRIMÔNIO": 1854090126.97, "YIELD MENSAL": 0.63, "YIELD ANUAL": 7.90, "PAGAMENTO": "14/12/2023"},
    {"CÓDIGO": "HGRU11", "SETOR": "Híbrido", "COTA": 116.36, "LIQUIDEZ DIÁRIA": 26746, "DIVIDENDO": 2.00, "RENTABILI": 24.82, "PATRIMÔNIO": 2262020100.59, "YIELD MENSAL": 0.65, "YIELD ANUAL": 9.72, "PAGAMENTO": "14/12/2023"},
    {"CÓDIGO": "HSML11", "SETOR": "Shoppings", "COTA": 77.52, "LIQUIDEZ DIÁRIA": 22434, "DIVIDENDO": 0.70, "RENTABILI": 17.91, "PATRIMÔNIO": 1539798921.32, "YIELD MENSAL": 0.81, "YIELD ANUAL": 10.80, "PAGAMENTO": "07/12/2023"},
    {"CÓDIGO": "HTMX11", "SETOR": "Hotel", "COTA": 113.57, "LIQUIDEZ DIÁRIA": 2457, "DIVIDENDO": 1.26, "RENTABILI": 2.64, "PATRIMÔNIO": 211128423.78, "YIELD MENSAL": 2.34, "YIELD ANUAL": 20.28, "PAGAMENTO": "07/12/2023"},
    {"CÓDIGO": "IRDM11", "SETOR": "Títulos e Val. Mob.", "COTA": 91.21, "LIQUIDEZ DIÁRIA": 37945, "DIVIDENDO": 0.90, "RENTABILI": -1.29, "PATRIMÔNIO": 1071745389.30, "YIELD MENSAL": 0.92, "YIELD ANUAL": 11.47, "PAGAMENTO": "14/12/2023"},
    {"CÓDIGO": "JSRE11", "SETOR": "Lajes Corporativas", "COTA": 97.05, "LIQUIDEZ DIÁRIA": 21962, "DIVIDENDO": 0.72, "RENTABILI": 1.26, "PATRIMÔNIO": 2620194387.32, "YIELD MENSAL": 0.89, "YIELD ANUAL": 11.09, "PAGAMENTO": "14/12/2023"},
    {"CÓDIGO": "KNHY11", "SETOR": "Outros", "COTA": 89.86, "LIQUIDEZ DIÁRIA": 9, "DIVIDENDO": 0.44, "RENTABILI": 3.55, "PATRIMÔNIO": 22657298.43, "YIELD MENSAL": 0.55, "YIELD ANUAL": 7.32, "PAGAMENTO": "14/12/2023"},
    {"CÓDIGO": "KNIP11", "SETOR": "Títulos e Val. Mob.", "COTA": 84.60, "LIQUIDEZ DIÁRIA": 12716, "DIVIDENDO": 0.94, "RENTABILI": -5.79, "PATRIMÔNIO": 1385539472.42, "YIELD MENSAL": 0.95, "YIELD ANUAL": 13.51, "PAGAMENTO": "14/12/2023"},
    {"CÓDIGO": "KNRI11", "SETOR": "Híbrido", "COTA": 162.53, "LIQUIDEZ DIÁRIA": 69767, "DIVIDENDO": 1.18, "RENTABILI": -0.41, "PATRIMÔNIO": 3551265367.95, "YIELD MENSAL": 0.87, "YIELD ANUAL": 11.57, "PAGAMENTO": "14/12/2023"},
    {"CÓDIGO": "KNRI11B", "SETOR": "Híbrido", "COTA": 174.92, "LIQUIDEZ DIÁRIA": 20317, "DIVIDENDO": 1.30, "RENTABILI": 0.22, "PATRIMÔNIO": 5661558559.10, "YIELD MENSAL": 0.89, "YIELD ANUAL": 11.83, "PAGAMENTO": "14/12/2023"},
    {"CÓDIGO": "RBRD11", "SETOR": "Títulos e Val. Mob.", "COTA": 77.26, "LIQUIDEZ DIÁRIA": 41338, "DIVIDENDO": 0.55, "RENTABILI": -5.55, "PATRIMÔNIO": 1578961206.16, "YIELD MENSAL": 0.84, "YIELD ANUAL": 10.60, "PAGAMENTO": "14/12/2023"},
    {"CÓDIGO": "RBRR11", "SETOR": "Lajes Corporativas", "COTA": 124.00, "LIQUIDEZ DIÁRIA": 2071, "DIVIDENDO": 0.80, "RENTABILI": 5.90, "PATRIMÔNIO": 416541605.19, "YIELD MENSAL": 0.65, "YIELD ANUAL": 8.50, "PAGAMENTO": "14/12/2023"},
    {"CÓDIGO": "RBRF11", "SETOR": "Outros", "COTA": 98.21, "LIQUIDEZ DIÁRIA": 31396, "DIVIDENDO": 0.90, "RENTABILI": -5.40, "PATRIMÔNIO": 1970617862.58, "YIELD MENSAL": 0.92, "YIELD ANUAL": 12.31, "PAGAMENTO": "14/12/2023"},
    {"CÓDIGO": "RBRP11", "SETOR": "Outros", "COTA": 71.31, "LIQUIDEZ DIÁRIA": 3943, "DIVIDENDO": 0.50, "RENTABILI": -7.39, "PATRIMÔNIO": 441738667.21, "YIELD MENSAL": 0.84, "YIELD ANUAL": 10.42, "PAGAMENTO": "14/12/2023"},
    {"CÓDIGO": "RBRR11", "SETOR": "Lajes Corporativas", "COTA": 104.00, "LIQUIDEZ DIÁRIA": 38372, "DIVIDENDO": 0.80, "RENTABILI": 7.18, "PATRIMÔNIO": 384540394.28, "YIELD MENSAL": 0.77, "YIELD ANUAL": 10.10, "PAGAMENTO": "14/12/2023"},
    {"CÓDIGO": "RECT11", "SETOR": "Outros", "COTA": 97.80, "LIQUIDEZ DIÁRIA": 99, "DIVIDENDO": 1.24, "RENTABILI": 4.98, "PATRIMÔNIO": 1572615622.94, "YIELD MENSAL": 1.27, "YIELD ANUAL": 16.96, "PAGAMENTO": "14/12/2023"},
    {"CÓDIGO": "RECR11", "SETOR": "Lajes Corporativas", "COTA": 97.35, "LIQUIDEZ DIÁRIA": 1279, "DIVIDENDO": 0.81, "RENTABILI": -7.27, "PATRIMÔNIO": 148392723.01, "YIELD MENSAL": 0.83, "YIELD ANUAL": 10.85, "PAGAMENTO": "14/12/2023"},
    {"CÓDIGO": "RNGO11", "SETOR": "Outros", "COTA": 91.80, "LIQUIDEZ DIÁRIA": 16, "DIVIDENDO": 1.00, "RENTABILI": -8.11, "PATRIMÔNIO": 14422169.34, "YIELD MENSAL": 1.09, "YIELD ANUAL": 14.22, "PAGAMENTO": "29/12/2023"},
    {"CÓDIGO": "RVBI11", "SETOR": "Outros", "COTA": 89.71, "LIQUIDEZ DIÁRIA": 1785, "DIVIDENDO": 0.75, "RENTABILI": 8.82, "PATRIMÔNIO": 48264208.88, "YIELD MENSAL": 0.92, "YIELD ANUAL": 12.32, "PAGAMENTO": "14/12/2023"},
    {"CÓDIGO": "SAAG11", "SETOR": "Outros", "COTA": 89.88, "LIQUIDEZ DIÁRIA": 39, "DIVIDENDO": 0.84, "RENTABILI": 7.91, "PATRIMÔNIO": 11137033.53, "YIELD MENSAL": 0.94, "YIELD ANUAL": 12.50, "PAGAMENTO": "14/12/2023"},
    {"CÓDIGO": "SADI11", "SETOR": "Outros", "COTA": 100.70, "LIQUIDEZ DIÁRIA": 3839, "DIVIDENDO": 0.88, "RENTABILI": -6.71, "PATRIMÔNIO": 1562583297.76, "YIELD MENSAL": 0.87, "YIELD ANUAL": 11.55, "PAGAMENTO": "14/12/2023"},
    {"CÓDIGO": "SAIC11B", "SETOR": "Híbrido", "COTA": 109.91, "LIQUIDEZ DIÁRIA": 2427, "DIVIDENDO": 0.88, "RENTABILI": -6.27, "PATRIMÔNIO": 200820740.12, "YIELD MENSAL": 0.95, "YIELD ANUAL": 12.67, "PAGAMENTO": "14/12/2023"},
    {"CÓDIGO": "SARE11", "SETOR": "Shoppings", "COTA": 126.97, "LIQUIDEZ DIÁRIA": 36, "DIVIDENDO": 0.80, "RENTABILI": 0.55, "PATRIMÔNIO": 315263897.80, "YIELD MENSAL": 0.63, "YIELD ANUAL": 7.80, "PAGAMENTO": "14/12/2023"},
    {"CÓDIGO": "SDIL11", "SETOR": "Outros", "COTA": 96.00, "LIQUIDEZ DIÁRIA": 43, "DIVIDENDO": 1.00, "RENTABILI": 3.22, "PATRIMÔNIO": 52857944.66, "YIELD MENSAL": 1.04, "YIELD ANUAL": 12.86, "PAGAMENTO": "14/12/2023"},
    {"CÓDIGO": "SFND11", "SETOR": "Outros", "COTA": 103.98, "LIQUIDEZ DIÁRIA": 145, "DIVIDENDO": 0.96, "RENTABILI": 6.40, "PATRIMÔNIO": 122683914.43, "YIELD MENSAL": 0.93, "YIELD ANUAL": 12.43, "PAGAMENTO": "14/12/2023"},
    {"CÓDIGO": "SHOP11", "SETOR": "Shoppings", "COTA": 50.70, "LIQUIDEZ DIÁRIA": 90552, "DIVIDENDO": 0.54, "RENTABILI": 1.77, "PATRIMÔNIO": 3166636471.32, "YIELD MENSAL": 1.08, "YIELD ANUAL": 14.36, "PAGAMENTO": "14/12/2023"},
    {"CÓDIGO": "SHPH11", "SETOR": "Shoppings", "COTA": 95.00, "LIQUIDEZ DIÁRIA": 1485, "DIVIDENDO": 0.73, "RENTABILI": -5.01, "PATRIMÔNIO": 422951052.56, "YIELD MENSAL": 0.77, "YIELD ANUAL": 9.80, "PAGAMENTO": "14/12/2023"},
    {"CÓDIGO": "SHPV11", "SETOR": "Shoppings", "COTA": 117.98, "LIQUIDEZ DIÁRIA": 602, "DIVIDENDO": 0.84, "RENTABILI": 4.10, "PATRIMÔNIO": 673876348.11, "YIELD MENSAL": 0.71, "YIELD ANUAL": 8.91, "PAGAMENTO": "14/12/2023"},
    {"CÓDIGO": "TORD11", "SETOR": "Outros", "COTA": 121.00, "LIQUIDEZ DIÁRIA": 56, "DIVIDENDO": 1.20, "RENTABILI": 4.67, "PATRIMÔNIO": 30162404.15, "YIELD MENSAL": 0.99, "YIELD ANUAL": 13.15, "PAGAMENTO": "30/12/2023"},
    {"CÓDIGO": "UBSR11", "SETOR": "Lajes Corporativas", "COTA": 100.00, "LIQUIDEZ DIÁRIA": 1570, "DIVIDENDO": 0.95, "RENTABILI": -6.53, "PATRIMÔNIO": 362099709.26, "YIELD MENSAL": 0.95, "YIELD ANUAL": 12.64, "PAGAMENTO": "14/12/2023"},
    {"CÓDIGO": "URPR11B", "SETOR": "Outros", "COTA": 93.50, "LIQUIDEZ DIÁRIA": 47, "DIVIDENDO": 0.75, "RENTABILI": -0.67, "PATRIMÔNIO": 13978340.90, "YIELD MENSAL": 0.78, "YIELD ANUAL": 9.92, "PAGAMENTO": "28/12/2023"},
    {"CÓDIGO": "VRTA11", "SETOR": "Outros", "COTA": 104.00, "LIQUIDEZ DIÁRIA": 159, "DIVIDENDO": 1.24, "RENTABILI": 6.57, "PATRIMÔNIO": 1278938655.91, "YIELD MENSAL": 1.19, "YIELD ANUAL": 15.88, "PAGAMENTO": "30/12/2023"},
    {"CÓDIGO": "VSLH11", "SETOR": "Shoppings", "COTA": 127.50, "LIQUIDEZ DIÁRIA": 106, "DIVIDENDO": 1.50, "RENTABILI": -4.39, "PATRIMÔNIO": 410695498.80, "YIELD MENSAL": 1.18, "YIELD ANUAL": 15.68, "PAGAMENTO": "14/12/2023"}
]



# Converter o dicionário em um DataFrame
# Verifique se seus_dados é uma lista
if isinstance(seus_dados, list):
    # Crie o DataFrame a partir dos registros da lista
    df_seus_dados = pd.DataFrame(seus_dados)
else:
    # Se seus_dados não for uma lista, crie o DataFrame a partir do dicionário
    df_seus_dados = pd.DataFrame.from_dict(seus_dados, orient='index')
df = df_seus_dados

# Agora você pode usar o DataFrame combinado 'df' no restante do seu código.
print(df)

# Função para calcular investimento necessário
def calcular_investimento(valor_codigo, rendimento_desejado, df):
    valores_codigo_selecionados = [codigo.strip() for codigo in valor_codigo]
    st.write("Códigos selecionados:", valores_codigo_selecionados)
    
    # Verificar se os códigos selecionados estão presentes no DataFrame
    codigos_validos = df['CÓDIGO'].unique()
    st.write("Códigos no DataFrame:", codigos_validos)
    if not set(valores_codigo_selecionados).issubset(codigos_validos):
        st.warning("Um ou mais códigos selecionados não estão presentes no DataFrame. Verifique os códigos e tente novamente.")
        return None

    # Remover espaços em branco dos códigos no DataFrame
    df.loc[:, 'CÓDIGO'] = df['CÓDIGO'].str.strip()

    valores_requeridos = df.loc[df['CÓDIGO'].isin(valores_codigo_selecionados), ['CÓDIGO', 'COTA', 'DIVIDENDO']].copy()

    if valores_requeridos.empty:
        st.warning("Nenhuma entrada encontrada para os códigos fornecidos. Verifique os códigos e tente novamente.")
        return None

    valores_requeridos['Investimento Necessário'] = (rendimento_desejado / valores_requeridos['DIVIDENDO']) * valores_requeridos['COTA']
    return valores_requeridos

# Função para filtrar o DataFrame pelo setor selecionado
def filtrar_por_setor(setor_selecionado, df):
    df_filtrado_por_setor = df[df['SETOR'] == setor_selecionado]
    return df_filtrado_por_setor

# Função para determinar o número da semana do mês
def determinar_semana_do_mes(data):
    dia_do_mes = data.day
    if dia_do_mes <= 7:
        return 1
    elif dia_do_mes <= 14:
        return 2
    elif dia_do_mes <= 21:
        return 3
    elif dia_do_mes <= 28:
        return 4
    else:
        return 5


# Ajuste: Dividir os valores por 100 na coluna 'PREÇO ATUAL' e 'DIVIDENDO'
#df['COTA'] = df['COTA'] / 100
#df['DIVIDENDO'] = df['DIVIDENDO'] / 100

# Convertendo a coluna 'PAGAMENTO' para datetime
# Defina a função determinar_semana_do_mes
def determinar_semana_do_mes(data):
    if pd.isnull(data):
        return None
    else:
        # Converta a string para objeto de data
        data = pd.to_datetime(data, format='%d/%m/%Y')
        # Extraia o dia do mês e calcule a semana do mês
        dia_do_mes = data.day
        semana_do_mes = (dia_do_mes - 1) // 7 + 1
        return semana_do_mes



# Substitua 'Não informado' por valores ausentes (NaT)
df['PAGAMENTO'] = df['PAGAMENTO'].replace('Não informado', pd.NaT)

# Converta a coluna 'PAGAMENTO' para datetime
df['PAGAMENTO'] = pd.to_datetime(df['PAGAMENTO'], format='%d/%m/%Y')

# Aplique a função para determinar a semana do mês
df['semana_do_mes'] = df['PAGAMENTO'].apply(determinar_semana_do_mes)

# Verifique o DataFrame após a conversão
print(df.head())

# Interface do Streamlit
st.sidebar.title("Parâmetros")

# Opções padrão
valores_padrao = df.iloc[0][['SETOR', 'COTA', 'DIVIDENDO']]

# Seleção de códigos
valores_codigo_selecionados = st.sidebar.multiselect("Selecione os códigos:", df['CÓDIGO'].unique())
rendimento_desejado = st.sidebar.number_input("Digite o valor do rendimento desejado:", value=valores_padrao['DIVIDENDO'])

# Cálculo de quartis para os valores de 'PREÇO ATUAL' e 'DIVIDENDO'
preco_minimo_q, preco_maximo_q = df['COTA'].quantile([0.25, 0.75])
dividendo_minimo_q, dividendo_maximo_q = df['DIVIDENDO'].quantile([0.25, 0.75])

# Definindo margem extra para os valores mínimos e máximos
margem_extra = 0.5

# Adicionando barras deslizantes para os parâmetros de filtragem
preco_minimo, preco_maximo = st.sidebar.slider("Faixa de Preço", preco_minimo_q, preco_maximo_q, (preco_minimo_q, preco_maximo_q))
dividendo_minimo, dividendo_maximo = st.sidebar.slider("Faixa de Dividendo", dividendo_minimo_q, dividendo_maximo_q, (dividendo_minimo_q, dividendo_maximo_q))

setor_selecionado = st.sidebar.selectbox("Selecione o setor:", [''] + list(df['SETOR'].unique()))

# Filtrando o DataFrame com base nos parâmetros selecionados
df_filtrado = df[(df['COTA'] >= preco_minimo) & (df['COTA'] <= preco_maximo) & 
                 (df['DIVIDENDO'] >= dividendo_minimo) & (df['DIVIDENDO'] <= dividendo_maximo)]

# Filtrando também pelo setor selecionado
if setor_selecionado:
    df_filtrado = filtrar_por_setor(setor_selecionado, df_filtrado)

# Exibindo o DataFrame filtrado
st.subheader("DataFrame Filtrado")
st.write(df_filtrado)
 

# Aplica a função para criar a coluna 'semana_do_mes'
df['semana_do_mes'] = df['PAGAMENTO'].apply(determinar_semana_do_mes)

# Ordena as semanas
semanas_ordenadas = sorted(df['semana_do_mes'].unique())

# Interface Streamlit
st.sidebar.header('Filtrar Por Semana e Código')

# Adiciona a opção 'Todos' à lista de códigos
opcoes_codigo = ['Todos'] + list(df['CÓDIGO'].unique())

# Dropdown para selecionar o código
codigo_selecionado = st.sidebar.selectbox('Selecione o Código', opcoes_codigo)

# Multiselect para selecionar as semanas, com as semanas ordenadas
semanas_selecionadas = st.sidebar.multiselect('Selecione as Semanas', semanas_ordenadas)

# Filtra o DataFrame com base no código e nas semanas selecionadas
if codigo_selecionado == 'Todos':
    df_filtrado = df[df['semana_do_mes'].isin(semanas_selecionadas)]
else:
    df_filtrado = df[(df['CÓDIGO'] == codigo_selecionado) & (df['semana_do_mes'].isin(semanas_selecionadas))]

# Mostra o DataFrame filtrado
st.write('DataFrame Filtrado:', df_filtrado)

# Mostra a semana do mês para o código selecionado
if codigo_selecionado != 'Todos':
    st.write(f"Semana do mês para o código {codigo_selecionado}:", df_filtrado['semana_do_mes'].values)

# Botão de cálculo
if st.sidebar.button("Calcular"):
    valores_requeridos = calcular_investimento(valores_codigo_selecionados, rendimento_desejado, df_filtrado)
    if valores_requeridos is not None:
        st.title("Resultados")
        if valores_requeridos.empty:
            st.warning("Nenhum resultado encontrado para os códigos fornecidos. Verifique os códigos e tente novamente.")
        else:
            st.success("Investimento necessário para cada código selecionado:")
            st.write(valores_requeridos)

            fig = px.bar(valores_requeridos, x='CÓDIGO', y='Investimento Necessário', title='Investimento Necessário por Código')
            st.plotly_chart(fig)
