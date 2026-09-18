# cursor-ide

Laboratório para testar e validar **desenvolvimento por vibe coding**: gerar código com IA, corrigir falhas e analisar bugs em um fluxo real de engenharia.

O objetivo não é um produto acabado. É exercitar o ciclo pedir → gerar → quebrar → diagnosticar → corrigir, com scripts pequenos e dados locais, para entender o que a IA acerta, o que omite e como a revisão humana entra no processo.

## O que estamos validando

- **Vibe coding**: descrever a intenção em linguagem natural e deixar a IA escrever o script, o gráfico e a estrutura do projeto.
- **Correção**: quando o código roda, mas o caminho, o cwd ou a saída estão errados, ajustar com contexto do repositório — não só “fazer funcionar” no terminal atual.
- **Análise de bugs**: ler traceback, localizar a causa (arquivo relativo vs. raiz do projeto, por exemplo) e aplicar um conserto estável.

## Como executar

Python 3.13+, gerenciado com [uv](https://docs.astral.sh/uv/).

```bash
uv sync
uv run python src/cursor_ide/01_grafico_vendas.py
uv run python -m cursor_ide.top10_chart
```

Os CSVs ficam em `data/`. Os gráficos gerados vão para `output/`.

## Scripts

| Script | Dados | Saída |
| --- | --- | --- |
| `src/cursor_ide/01_grafico_vendas.py` | `data/vendas_2024.csv` | `output/grafico_vendas.png` |
| `src/cursor_ide/top10_chart.py` | `data/most_streamed_spotify_2025.csv` | `output/top10_spotify.png` |

O relatório de vendas nasceu propositalmente quebrado (`FileNotFoundError` ao abrir `vendas_2024.csv` pelo cwd). A correção resolve o caminho a partir da raiz do repositório (`Path(__file__)`), para o script não depender de onde o comando foi executado.
