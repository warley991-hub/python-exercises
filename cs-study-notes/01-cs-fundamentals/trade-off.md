# TRADE-OFF

**Contexto / Origem:** Brilliant / Wikipedia
**Data:** 2026-NOV-24

## O que é (com as minhas palavras)
Um **trade-off** é uma escolha que um indivíduo ou entidade toma que pode fazer você ter que sacrificar algum recurso ou opção para obter determinado resultado, uma opção que tem lucros e prejuízos.

Em um curto resumo: Se ganha algo e se perde algo para manter aquilo que se ganhou.

O 'ganhar' ou 'perder' pode ser em termos de desempenho/métricas ou até mesmo bonificação/vantagem já que esse conceito é amplamente explorado no mundo real.

Esse conceito existe em várias áreas da vida, um **trade-off**, na linguagem popular seria algo como:
*'Sacrificar o almoço para garantir a janta'*.

Também pode ser feito um paralelo com o conceito de *preferência temporal*, o famoso 'Teste do Marshmallow', onde acontece um **trade-off** entre o presente e o futuro.

Na Ciência de Computação o conceito de **trade-off** também é aplicável, como a relação entre espaço e tempo.

Na prática, falando de computadores, um **trade-off** de memória para se obter mais desempenho seria nada mais nada menos do que alocar os recursos para ocupar mais espaço (sacrificar o espaço) na memória para se obter um maior desempenho (ganhar velocidade, diminuir o tempo).

## Exemplo ou Analogia
Um exemplo de **trade-off** recente que percebi foi em um jogo de computador chamado 'Devour'.

#### Explicação rápida sobre o jogo:

Devour é um jogo de terror cooperativo (1 a 4 jogadores) onde a equipe precisa reunir itens de ritual para banir um cultista possuído por um demônio antes que ele os capture.

#### Explicação rápida sobre o mecanismo do jogo:

Em determinado mapa do jogo, existe um número fixo de itens (normalmente 10) que os jogadores devem coletar para realizar um 'ritual', a cada item coletado e ritualizado o 'demônio' que anda pelo mapa fica mais agressivo e persegue os jogadores com maior velocidade, tornando mais difícil para os jogadores se manterem vivos, se todos os jogadores morrerem, o jogo acaba e todos perdem.

Os itens de ritual aparecem no mapa em dois momentos, no primeiro momento aparece apenas metade dos itens para serem coletados, e no segundo momento a outra metade aparece somente quando a primeira metade já foi ritualizada, logo os jogadores não podem reunir todos os 10 itens de uma só vez para realizarem o ritual com um item após o outro na sequência, o jogo os obriga a fazer o ritual com a primeira metade e só depois com a segunda.

Se os jogadores coletarem os 5 primeiros itens e não realizarem o ritual o 'demônio' que anda pelo mapa não os persegue com muita agressividade nem com muita velocidade, é como se ele estivesse 'calmo' e essa paciência vai se esgotando a cada item que é ritualizado. 

Algumas regras do jogo:

1. Cada jogador pode carregar apenas 1 item por vez.
2. Se o jogador soltar um item que ainda não foi ritualizado ele terá que procurá-lo novamente pelo mapa.
3. Os jogadores não são eliminados de forma definitiva pelo 'demônio', os jogadores podem ser derrubados pelo 'demônio', assim que isso acontece o jogador atingido será levado para algum local aleatório do mapa e ele só poderá retornar para ajudar os colegas se algum outro jogador de sua equipe resgatá-lo.
4. O 'demônio' ficará mais agressivo e veloz de maneira progressiva apenas quando um item é ritualizado, apenas segurar o item não afeta a hostilidade do 'demônio'.
5. Quando o 'demônio' estiver em um certo nível de agressividade ele jamais retornará a um nível inferior, exceto que o jogo seja completamente reiniciado.

#### Onde o **trade-off** acontece:

Em experiência prática dentro do jogo, caso os jogadores realizassem o ritual com 1 item de cada vez conforme fossem encontrados pelo mapa, as chances de vitória diminuiriam drasticamente, já que por volta do 7° item ritualizado o 'demônio' do jogo se tornaria muito mais agressivo e perseguiria os jogadores com muito mais velocidade, eliminando um a um e fazendo com que o jogo terminasse.

Com isso já comprovado pelos jogadores, chega-se a uma conclusão óbvia:

- Juntar o máximo de itens possíveis e ritualizá-los todos juntos seria melhor.

Mas o jogo não deixa tão fácil assim... 

Como foi mencionado, apenas 5 itens são liberados no primeiro momento e só depois de serem usados no ritual os outros 5 são liberados, então os jogadores poderiam chegar na próxima conclusão óbvia:

- Ritualizar os 5 primeiros, coletar os próximos 5 e ritualizá-los todos juntos.

Porém isso também acabaria por se tornar complicado...

Apesar das chances de vitória serem maiores do que ritualizar 1 item por vez, quando os jogadores chegassem em 5 itens ritualizados, os próximos 5 estariam espalhados de forma aleatória pelo mapa, então os 4 jogadores da equipe teriam que se espalhar para encontrarem os itens mais rapidamente, já que mesmo no nível 5 o 'demônio' do mapa ainda poderia atacar os jogadores 1 por 1 até que todos caissem, então a velocidade e organização por parte dos jogadores se torna crucial.

E mesmo que cada um dos 4 jogadores retornasse neste segundo momento com 1 item, ainda restaria 1 item para procurar, e o 'demônio' já estaria no nível 9 de agressividade, o que tornaria o jogo ainda mais difícil de se vencer. 

Então essas duas possibilidades já seriam descartadas:

1. Ritualizar 1 item por vez (1-1-1-1-1-1-1-1-1-1).
2. Ritualizar 5 itens em dois momentos (5-5).

Na prática, o próximo plano que funcionaria bem para que os 4 jogadores vençam o jogo seria fazer o seguinte arranjo:

 - Ritualizar 6 itens primeiro e depois 4 itens (6-4).

Com o 'demônio' no nível 6 de agressividade o jogo estaria muito difícil para os jogadores, porém seria muito mais provável que cada um deles encontrasse os 4 últimos itens restantes e que conseguissem realizar o ritual com os itens para vencerem o jogo, já que o nível de agressividade do 'demônio' estaria menor do que no último arranjo (5-5) e não escalaria de maneira dificultosa como no primeiro arranjo (1-1-1-1-1-1-1-1-1-1) dando assim o equilíbrio necessário para os jogadores se organizarem e ainda terem chances de vencer.

Neste exemplo, o conceito de **trade-off** acontece desde o início do jogo, com a decisão de escalar os itens de ritual um a um ou de criar momentos estratégicos para ritualizarem um número específico de itens em momentos também específicos. O **trade-off** aqui acontece em várias nuances:

 1. A velocidade do 'demônio' é proporcional à quantidade de itens ritualizados pelos jogadores.
 2. Se eles não avançarem o jogo nunca terminará.
 3. Se avançarem rápido demais nunca vencerão.

 Existem outros arranjos possíveis para que se pudesse terminar o jogo, porém este pareceu o mais equilibrado entre avançar no progresso e ainda ter chances de completar o objetivo, minimizando as perdas o máximo possível.

 #### Outras maneiras de completar o objetivo:

 Seria completamente possível terminar o jogo com um arranjo (5-5), porém o custo disso seria alto demais, já que no exemplo citado anteriormente, quando o nível chegasse em 9 o 'demônio' se tornaria muito mais veloz e seria capaz de derrubar todos os jogadores com facilidade, porém também existe a possibilidade de 1 jogador encontrar o último item faltante, ritualizá-lo e vencer o jogo sozinho, mesmo que seus 3 companheiros estejam caídos, porém as chances disso acontecer seriam muito baixas, e o número de tentativas para vencer o mapa seria maior.

 Outra forma de terminar seria com um arranjo (7-3), nessa configuração se tem a vantagem que se faltam menos itens para procurar, porém se tem a desvantagem do nível do inimigo ser maior.

E é claro, existem também os demais arranjos que ainda estejam dentro das regras e somados cheguem ao número total de itens, mas nenhum deles parece mais vantajoso que o apresentado (6-4) para essa situação.

 Um perfeito exemplo de gerenciamento de **trade-off** aplicado a um algoritmo de um jogo, onde se precisa encontrar um equilíbrio entre avançar no objetivo e controlar a dificuldade do game.

 ## Trade-off na ciência da computação

 No mundo da computação o conceito de **trade-off** vai muito além de um 'recurso vs. resultado', na maioria das vezes envolve custos e gastos financeiros reais, requisitos que competem um com o outro, por exemplo:

 - Tempo vs. Memória
 - Latência vs. Consistência
 - Complexidade vs. Manutenabilidade
