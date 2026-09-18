"""
Projeto 1 - Relatório de vendas
--------------------------------
Lê o arquivo de vendas de 2024 e gera um gráfico de barras
com o total vendido em cada mês.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
CSV_PATH = PROJECT_ROOT / "data" / "vendas_2024.csv"
OUTPUT_PATH = PROJECT_ROOT / "output" / "grafico_vendas.png"


def carregar_vendas(caminho):
    df = pd.read_csv(caminho)
    return df


def gerar_grafico(df, output_path=OUTPUT_PATH):
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.figure(figsize=(10, 5))
    plt.bar(df["mes"], df["vendas"], color="#3b6ef5")
    plt.title("Vendas por mês - 2024")
    plt.xlabel("Mês")
    plt.ylabel("Vendas (R$)")
    plt.tight_layout()
    plt.savefig(output_path)
    print(f"Gráfico salvo em {output_path}")


def main():
    df = carregar_vendas(CSV_PATH)
    print(f"{len(df)} meses carregados.")
    gerar_grafico(df)


if __name__ == "__main__":
    main()
