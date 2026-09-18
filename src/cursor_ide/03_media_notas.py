"""
Projeto 3 - Média da turma
--------------------------
Lê as notas dos alunos em notas.txt (uma nota por linha), calcula a
média da turma e mostra quantos ficaram acima dela.
"""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
NOTAS_PATH = PROJECT_ROOT / "data" / "notas.txt"


def ler_notas(caminho=NOTAS_PATH):
    with open(caminho, "r", encoding="utf-8") as f:
        linhas = f.readlines()
    return [float(linha.strip()) for linha in linhas if linha.strip()]


def calcular_media(notas):
    if not notas:
        raise ValueError("Nenhuma nota encontrada para calcular a média.")
    return sum(notas) / len(notas)


def main():
    notas = ler_notas()
    media = calcular_media(notas)
    print(f"Média da turma: {media:.2f}")

    acima = [n for n in notas if n > media]
    print(f"{len(acima)} alunos ficaram acima da média.")


if __name__ == "__main__":
    main()
