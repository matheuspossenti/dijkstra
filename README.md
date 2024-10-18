
# Documentação do Projeto de Caminhos Mínimos

## Descrição do Projeto

Este projeto implementa um algoritmo de Dijkstra para encontrar o caminho mais curto entre dois pontos em um grafo representado como um dicionário de adjacências. O grafo contém diversos pontos de interesse, e o algoritmo calcula a distância mínima entre um ponto de partida e um ponto de destino escolhido pelo usuário.

## Equipe

O projeto foi desenvolvido por:
- Matheus Possenti
- Thiago Trzcinski
- Rafael Bressan

## Funcionalidades

- Exibir os pontos disponíveis no grafo.
- Permitir que o usuário escolha um ponto de partida e um ponto de destino.
- Calcular e exibir o caminho mais curto entre os pontos escolhidos.
- Exibir a distância total do caminho calculado.

## Estrutura do Código

O código consiste em:
- Um grafo representado por um dicionário, onde as chaves são os pontos e os valores são dicionários com os vizinhos e suas respectivas distâncias.
- A função `dijkstra`, que implementa o algoritmo para encontrar o caminho mais curto.
- A função `mostrar_pontos_disponiveis`, que exibe os pontos disponíveis.
- A função `main`, que gerencia a interação do usuário e coordena a execução do algoritmo.

## Como Executar o Projeto

Para executar o projeto, siga os passos abaixo:

1. **Pré-requisitos**: Certifique-se de que você tem o Python instalado em seu sistema. Você pode baixar o Python [aqui](https://www.python.org/downloads/).

2. **Clone o Repositório**: Se você estiver usando um repositório Git, clone o repositório com o seguinte comando:
   ```bash
   git clone <URL do repositório>
   ```

3. **Navegue até a Pasta do Projeto**:
   ```bash
   cd <pasta do projeto>
   ```

4. **Execute o Código**: Execute o script Python usando o seguinte comando:
   ```bash
   python nome_do_arquivo.py
   ```

5. **Interação com o Programa**: Siga as instruções exibidas no terminal para escolher os pontos de partida e destino. O programa calculará e exibirá o caminho mais curto e a distância total.

## Exemplo de Uso

Ao executar o programa, a saída será semelhante a:

```
Pontos disponíveis:
Guarita
P1
P2
P3
...
Escolha o ponto de partida: Guarita
Escolha o ponto de destino: Ginásio
Caminho mais curto de Guarita para Ginásio: Guarita -> P2 -> P3 -> P1 -> Ginásio
Distância total: 2090 centímetros
```

## Considerações Finais

Este projeto pode ser expandido para incluir mais funcionalidades, como visualização gráfica do grafo, suporte a diferentes algoritmos de caminho mínimo, ou a possibilidade de adicionar ou remover pontos e conexões dinamicamente.
