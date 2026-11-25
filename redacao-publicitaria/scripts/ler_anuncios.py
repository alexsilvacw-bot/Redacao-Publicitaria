#!/usr/bin/env python3
"""Exibe o plano ou um lote do acervo local, com os campos da entrega pedida."""

import argparse
import re
from pathlib import Path


CORPUS = Path(__file__).resolve().parents[1] / "references" / "anuncios.txt"
LIMITE_LOTE = 18_000
SEPARADOR = "\n\n———\n\n"
INTRODUCAO = "Textos de referência\n\n"
CONTEXTO = "Produto ou serviço"
CAMPOS_COPY = ("Headline vigente", "Subtítulo", "Corpo do anúncio", "Assinatura")
MODOS = {
    "headline": ("Headline vigente", "Subtítulo", "Assinatura"),
    "legenda": ("Corpo do anúncio",),
    "completo": CAMPOS_COPY,
}
ROTULO = re.compile(r"\n\n(" + "|".join(map(re.escape, (*CAMPOS_COPY, CONTEXTO))) + r")\n")


def ler_registros(acervo):
    texto = acervo.read_text(encoding="utf-8")
    if not texto.startswith(INTRODUCAO):
        raise ValueError("Cabeçalho inesperado no arquivo de anúncios.")
    blocos = texto[len(INTRODUCAO):].removesuffix("\n").split(SEPARADOR)
    for numero, bloco in enumerate(blocos, 1):
        titulo, *pares = ROTULO.split(bloco)
        campos = dict(zip(pares[::2], pares[1::2]))
        if titulo != f"Anúncio {numero}" or len(campos) * 2 != len(pares):
            raise ValueError(f"Estrutura inesperada no anúncio {numero}.")
        if not campos.get(CONTEXTO, "").strip() or not any(campos.get(campo, "").strip() for campo in CAMPOS_COPY):
            raise ValueError(f"Falta texto publicitário ou contexto no anúncio {numero}.")
        yield titulo, campos


def montar_lotes(modo, acervo):
    lotes = [[]]
    tamanho_lote = 0
    tamanho_separador = len(SEPARADOR.encode("utf-8"))
    for titulo, campos in ler_registros(acervo):
        registros = [f"{campo}\n{campos[campo]}" for campo in (*MODOS[modo], CONTEXTO) if campo in campos]
        bloco = "\n\n".join([titulo, *registros])
        tamanho = len(bloco.encode("utf-8"))
        custo_no_lote = tamanho + (tamanho_separador if lotes[-1] else 0)
        if lotes[-1] and tamanho_lote + custo_no_lote > LIMITE_LOTE:
            lotes.append([])
            tamanho_lote = 0
            custo_no_lote = tamanho
        lotes[-1].append(bloco)
        tamanho_lote += custo_no_lote
    return lotes


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("modo", choices=MODOS)
    parser.add_argument("lote", type=int, nargs="?", help="Número do lote. Omita para listar o plano.")
    parser.add_argument("--acervo", type=Path, default=CORPUS, help="Arquivo local de referências.")
    args = parser.parse_args()
    try:
        lotes = montar_lotes(args.modo, args.acervo)
    except (OSError, ValueError) as erro:
        parser.error(str(erro))
    if args.lote is None:
        total = sum(len(lote) for lote in lotes)
        print(f"Anúncios: {total} | Lotes: {len(lotes)} | Modo: {args.modo}")
        primeiro = 1
        for numero, lote in enumerate(lotes, 1):
            ultimo = primeiro + len(lote) - 1
            print(f"Lote {numero}: anúncios {primeiro} a {ultimo}")
            primeiro = ultimo + 1
        return
    if not 1 <= args.lote <= len(lotes):
        parser.error(f"O lote deve estar entre 1 e {len(lotes)}.")
    numero = f"{args.lote}/{len(lotes)}"
    print(f"Lote {numero}\n")
    print(SEPARADOR.join(lotes[args.lote - 1]))
    print(f"\nFim do lote {numero}")


if __name__ == "__main__":
    main()
