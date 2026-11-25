---
name: redacao-publicitaria
description: Escreve títulos, legendas, textos de arte e e-mails publicitários em português brasileiro a partir de um briefing e de referências de redação. Use quando o usuário invocar $redacao-publicitaria ou pedir criação de texto publicitário com esta skill.
---

# Redação-Publicitária

Escreva a peça diretamente nesta conversa com o modelo e o esforço selecionados pelo usuário. Use o leitor local para trazer os anúncios de referência ao contexto antes de escrever.

## Defina a entrada

Use o briefing do usuário para definir produto ou serviço, público, objetivo, fatos disponíveis, canal e formato, conforme aplicável. Peça esclarecimento se faltar um dado essencial para escrever. Se o usuário pedir para repetir um briefing, identifique o briefing correto antes de prosseguir. O acervo fornece referências de escrita. O briefing fornece os fatos sobre a oferta nova.

| Entrega solicitada | Modo local | Campos de copy a ler |
| --- | --- | --- |
| Headline | `headline` | Headline vigente, subtítulo e assinatura |
| Legenda | `legenda` | Corpo do anúncio |
| Texto de arte e legenda, inclusive headline com legenda, ou e-mail         | `completo` | Headline vigente, subtítulo, corpo do anúncio e assinatura |

Leia **Produto ou serviço** em todos os modos para entender a oferta à qual cada peça se refere, inclusive o sentido do título. Use apenas os campos de copy do modo escolhido. Em um anúncio sem campos preenchidos para aquele modo, leia Produto ou serviço e siga para o próximo.

## Leia a seleção editorial

Use a [seleção editorial de 441 anúncios](references/anuncios.txt) que acompanha a skill. O leitor local [scripts/ler_anuncios.py](scripts/ler_anuncios.py) entrega apenas os campos do modo solicitado, em lotes ordenados. Resolva o caminho do script a partir da pasta deste `SKILL.md`. Se o usuário pedir o uso de outro arquivo de referências no mesmo formato, use `--acervo <caminho>` em todos os comandos de leitura.

1. Execute `python3 <caminho-do-script> <modo>` para obter o plano de lotes. Por exemplo, `python3 <caminho-do-script> legenda`.
2. Leia cada lote com `python3 <caminho-do-script> <modo> <número-do-lote>`. Comece pelo lote 1, siga o plano até o último lote e mantenha todos os anúncios no contexto da geração. O lote só conta como lido após seu conteúdo inteiro estar disponível. Se a ferramenta truncar a saída de um lote, recupere o trecho faltante. Se a conversa não comportar a leitura integral, informe a limitação antes de oferecer uma execução parcial.
3. Observe como cada peça transforma um fato da oferta em ideia e como as frases desenvolvem essa ideia. Use essas escolhas como referência de técnica. Quando um campo estiver marcado com `[trecho]`, use a passagem disponível como referência parcial.

## Escreva e entregue

Escreva texto original em português brasileiro. Use liberdade poética e deixe o briefing determinar o argumento. Quando oferecer opções, varie a ideia entre elas. Respeite a quantidade e o formato solicitados. Em texto de arte com legenda, faça a legenda desenvolver a ideia da arte. Se a ideia depender de uma imagem específica, descreva a **cena sugerida** separadamente.
