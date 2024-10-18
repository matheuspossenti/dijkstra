import heapq

grafo = {
    'Guarita': {'P1': 2090, 'P2': 800},
    'P1': {'Guarita': 2090, 'Ginásio': 1800},
    'P2': {'Guarita': 800, 'P3': 1200, 'Administrativo': 700, 'Bloco de Salas': 1500},
    'P3': {'P2': 1200, 'Cantina': 220, 'Bloco Professores': 225, 'P4': 800, 'Bloco de Salas': 1300},
    'P4': {'P3': 800, 'P5': 900, 'P8': 2000},
    'P5': {'P4': 900, 'Biblioteca': 450, 'Auditório': 600, 'P6': 1200},
    'P6': {'P5': 1200, 'Auditório': 185, 'Laboratórios': 225, 'P7': 1200},
    'P7': {'P6': 1200, 'Galpão de Máquinas': 935},
    'P8': {'P4': 2000, 'Refeitório': 500, 'Ginásio': 2200, 'Academia': 1900},
    'Refeitório': {'P8': 500, 'Academia': 1300, 'Ginásio': 1400},
    'Ginásio': {'P1': 1800, 'P8': 2200, 'Refeitório': 1400, 'Academia': 160},
    'Administrativo': {'P2': 700},
    'Bloco de Salas': {'P2': 1500, 'P3': 1300, 'Bloco A': 230, 'Bloco B': 230},
    'Bloco Professores': {'P3': 225},
    'Cantina': {'P3': 220},
    'Biblioteca': {'P5': 450},
    'Auditório': {'P5': 600, 'P6': 185},
    'Laboratórios': {'P6': 225},
    'Galpão de Máquinas': {'P7': 935},
    'Academia': {'P8': 1900, 'Refeitório': 1300, 'Ginásio': 160},
    'Bloco A': {'Bloco de Salas': 230},
    'Bloco B': {'Bloco de Salas': 230}
}

def dijkstra(grafo, inicio, destino):
    fila_prioridade = [(0, inicio)]
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    caminho = {nodo: None for nodo in grafo}

    while fila_prioridade:
        (dist_atual, nodo_atual) = heapq.heappop(fila_prioridade)

        if nodo_atual == destino:
            break

        for vizinho, peso in grafo[nodo_atual].items():
            dist_nova = dist_atual + peso

            if dist_nova < distancias[vizinho]:
                distancias[vizinho] = dist_nova
                caminho[vizinho] = nodo_atual
                heapq.heappush(fila_prioridade, (dist_nova, vizinho))

    rota = []
    nodo_atual = destino
    while nodo_atual:
        rota.append(nodo_atual)
        nodo_atual = caminho[nodo_atual]
    rota.reverse()

    return rota, distancias[destino]

def mostrar_pontos_disponiveis():
    print("Pontos disponíveis:")
    for ponto in grafo.keys():
        print(ponto)

def main():
    mostrar_pontos_disponiveis()

    inicio = input("Escolha o ponto de partida: ")
    while inicio not in grafo:
        print("Ponto inválido. Escolha novamente.")
        inicio = input("Escolha o ponto de partida: ")

    destino = input("Escolha o ponto de destino: ")
    while destino not in grafo:
        print("Ponto inválido. Escolha novamente.")
        destino = input("Escolha o ponto de destino: ")

    rota, distancia = dijkstra(grafo, inicio, destino)

    print(f"Caminho mais curto de {inicio} para {destino}: {' -> '.join(rota)}")
    print(f"Distância total: {distancia} centímetros")

if __name__ == "__main__":
    main()
