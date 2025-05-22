import pandas as pd
from prettytable import PrettyTable

# Caminho do arquivo
file_path = "INFOPOKEMON.txt"  # Ajuste se necessário

# Carregar os dados ignorando linha duplicada de cabeçalho
df = pd.read_csv(file_path, sep="\t", skiprows=[1])

# Função de rank
def gerar_rank(df, atributo: str, quantidade: int):
    mapeamento = {
        "vida": "Vida",
        "dano": "Dano",
        "dano especial": "SP Dano",
        "defesa": "Defesa",
        "defesa especial": "SP Def",
        "velocidade": "Vel"
    }
    atributo_coluna = mapeamento.get(atributo.lower())
    if not atributo_coluna:
        raise ValueError("Atributo inválido. Escolha entre: vida, dano, dano especial, defesa, defesa especial, velocidade.")

    df_atributo = df[["Nome Pokemon", atributo_coluna]].dropna()
    df_atributo[atributo_coluna] = pd.to_numeric(df_atributo[atributo_coluna], errors="coerce")
    df_atributo = df_atributo.dropna(subset=[atributo_coluna])

    return df_atributo.sort_values(by=atributo_coluna, ascending=False).head(quantidade).reset_index(drop=True)

# Função com PrettyTable
def exibir_rank_pretty(df, atributo: str, quantidade: int):
    tabela = gerar_rank(df, atributo, quantidade)

    if quantidade <= 25:
        # Tabela simples
        table = PrettyTable()
        table.field_names = ["Posição", "Nome Pokémon", atributo.capitalize()]
        for i, row in tabela.iterrows():
            table.add_row([i + 1, row["Nome Pokemon"], row.iloc[1]])
        print(table)

    elif quantidade <= 40:
        # Duas colunas lado a lado
        parte = (quantidade + 1) // 2
        col1 = tabela.iloc[:parte].reset_index(drop=True)
        col2 = tabela.iloc[parte:].reset_index(drop=True)

        table = PrettyTable()
        table.field_names = [
            "Pos", "Nome Pokémon", atributo.capitalize(),
            "Pos 2", "Nome Pokémon 2", f"{atributo.capitalize()} 2"
        ]

        for i in range(max(len(col1), len(col2))):
            row1 = [i+1, col1.loc[i, "Nome Pokemon"], col1.iloc[i, 1]] if i < len(col1) else ["", "", ""]
            row2 = [i+1+parte, col2.loc[i, "Nome Pokemon"], col2.iloc[i, 1]] if i < len(col2) else ["", "", ""]
            table.add_row(row1 + row2)

        print(table)

    else:
        # Três colunas lado a lado
        parte = (quantidade + 2) // 3
        col1 = tabela.iloc[:parte].reset_index(drop=True)
        col2 = tabela.iloc[parte:parte*2].reset_index(drop=True)
        col3 = tabela.iloc[parte*2:].reset_index(drop=True)

        table = PrettyTable()
        table.field_names = [
            "Pos", "Nome Pokémon", atributo.capitalize(),
            "Pos 2", "Nome Pokémon 2", f"{atributo.capitalize()} 2",
            "Pos 3", "Nome Pokémon 3", f"{atributo.capitalize()} 3"
        ]

        for i in range(max(len(col1), len(col2), len(col3))):
            row1 = [i+1, col1.loc[i, "Nome Pokemon"], col1.iloc[i, 1]] if i < len(col1) else ["", "", ""]
            row2 = [i+1+parte, col2.loc[i, "Nome Pokemon"], col2.iloc[i, 1]] if i < len(col2) else ["", "", ""]
            row3 = [i+1+2*parte, col3.loc[i, "Nome Pokemon"], col3.iloc[i, 1]] if i < len(col3) else ["", "", ""]
            table.add_row(row1 + row2 + row3)

        print(table)

if __name__ == "__main__":
    exibir_rank_pretty(df, "vida", 60)  # ou qualquer número que deseje