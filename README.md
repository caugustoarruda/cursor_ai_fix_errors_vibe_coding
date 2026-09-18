# Vibe Coding Errors

Laboratório para testar e validar **desenvolvimento por vibe coding**: gerar código com IA, corrigir falhas e analisar bugs em um fluxo real de engenharia.

O objetivo não é um produto acabado. É exercitar o ciclo pedir → gerar → quebrar → diagnosticar → corrigir, com scripts pequenos e dados locais, para entender o que a IA acerta, o que omite e como a revisão humana entra no processo.

## O que estamos validando

- **Vibe coding**: descrever a intenção em linguagem natural e deixar a IA escrever o script, o gráfico e a estrutura do projeto.
- **Correção**: quando o código roda, mas o caminho, o cwd ou a saída estão errados, ajustar com contexto do repositório — não só “fazer funcionar” no terminal atual.
- **Análise de bugs**: ler traceback, localizar a causa (arquivo relativo vs. raiz do projeto, tipos errados, etc.) e aplicar um conserto estável.

## Como executar

Python 3.13+, gerenciado com [uv](https://docs.astral.sh/uv/).

```bash
uv sync
uv run python src/cursor_ide/01_grafico_vendas.py
uv run python src/cursor_ide/03_media_notas.py
uv run python -m cursor_ide.top10_chart
```

Os dados ficam em `data/`. Os gráficos gerados vão para `output/`.

## Scripts

| Script | Dados | Saída |
| --- | --- | --- |
| `src/cursor_ide/01_grafico_vendas.py` | `data/vendas_2024.csv` | `output/grafico_vendas.png` |
| `src/cursor_ide/03_media_notas.py` | `data/notas.txt` | média da turma no terminal |
| `src/cursor_ide/top10_chart.py` | `data/most_streamed_spotify_2025.csv` | `output/top10_spotify.png` |

Os exercícios de bug nasceram propositalmente quebrados. Os caminhos passam a ser resolvidos a partir da raiz do repositório (`Path(__file__)`), para o script não depender de onde o comando foi executado.

### `01_grafico_vendas.py`

`FileNotFoundError` ao abrir `vendas_2024.csv` pelo cwd, em vez de `data/vendas_2024.csv`.

### `03_media_notas.py`

Havia dois problemas em sequência:

1. **`FileNotFoundError`**: o script abria `notas.txt` no cwd; o arquivo está em `data/notas.txt`.
2. **`TypeError` na soma**: `ler_notas` devolvia strings (`"8.5"`). `soma += nota` (e depois `n > media`) falharia ao misturar `int`/`float` com `str`. A correção converte cada linha com `float()` antes do cálculo.
