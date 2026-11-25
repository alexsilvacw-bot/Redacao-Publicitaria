# Redação-Publicitária

Skill para escrever títulos, legendas, textos de arte e e-mails publicitários. Disponível exclusivamente em português brasileiro.

## Como funciona o motor de redação

A metodologia foi desenvolvida a partir da leitura e da seleção editorial de grandes textos da publicidade brasileira. A seleção original reúne 441 anúncios. O trabalho de curadoria examinou onde a ideia se completa em cada peça, seja no título, no restante do texto ou na relação com a imagem.

A cada pedido, a skill lê o briefing e coloca os exemplos de redação no contexto do modelo. Para um título, lê títulos, subtítulos e assinaturas. Para uma legenda, lê os corpos dos anúncios. Para texto de arte com legenda ou e-mail, combina os campos. Em todos os formatos, lê a descrição da oferta de referência para entender o sentido da peça. Os fatos do novo anúncio vêm do briefing. O aprendizado durante a execução acontece por exemplos em contexto, com os pesos do modelo fixos.

Esta edição pública vem com oito exemplos inéditos que demonstram o método. A seleção editorial original de 441 anúncios permanece no acervo privado.

## Modelo recomendado

Para melhores resultados, selecione um modelo com capacidade de raciocínio complexo e esforço alto, como **Astra-High** ou **Fable High**. O modelo escolhido no chat lê as referências, desenvolve ideias e escreve a peça.

## Instalação e uso no Codex

Baixe ou clone este repositório. Copie a pasta [`redacao-publicitaria`](redacao-publicitaria) para `~/.codex/skills/` e abra uma nova sessão do Codex. O leitor precisa de Python 3.9 ou mais recente e usa a biblioteca padrão.

```text
Use $redacao-publicitaria para criar três opções de texto de arte com legenda para divulgar a coleta de roupas de inverno do centro comunitário. O público tem agasalhos para doar, mas costuma adiar a entrega. A equipe recebe as doações aos sábados pela manhã.
```

Para usar referências próprias, monte um arquivo de texto com a estrutura de [`anuncios.txt`](redacao-publicitaria/references/anuncios.txt), com os anúncios numerados em sequência. Informe o caminho desse arquivo ao pedir a peça.
