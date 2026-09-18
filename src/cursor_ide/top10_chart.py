"""Gera um gráfico das 10 músicas mais ouvidas no Spotify (2025)."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
CSV_PATH = PROJECT_ROOT / "data" / "most_streamed_spotify_2025.csv"
OUTPUT_PATH = PROJECT_ROOT / "output" / "top10_spotify.png"


def load_top10(csv_path: Path = CSV_PATH) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    return (
        df.nlargest(10, "spotify_streams_total")
        .assign(label=lambda d: d["track"] + " — " + d["artist"])
        .sort_values("spotify_streams_total", ascending=True)
    )


def plot_top10(top10: pd.DataFrame, output_path: Path = OUTPUT_PATH) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    streams_bi = top10["spotify_streams_total"] / 1_000_000_000

    fig, ax = plt.subplots(figsize=(11, 6))
    bars = ax.barh(top10["label"], streams_bi, color="#1DB954", height=0.7)

    ax.bar_label(bars, fmt="%.2f bi", padding=4, fontsize=9, color="#191414")
    ax.set_xlabel("Streams totais (bilhões)")
    ax.set_title("Top 10 músicas mais ouvidas no Spotify (2025)")
    ax.set_xlim(0, streams_bi.max() * 1.15)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(output_path, dpi=150)
    plt.close(fig)
    return output_path


def main() -> None:
    top10 = load_top10()
    path = plot_top10(top10)
    print(f"Gráfico salvo em: {path}")


if __name__ == "__main__":
    main()
