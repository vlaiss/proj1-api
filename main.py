# Funcionalidades:
# 1. Velocidade do veículo atual (km/h)
# 2. Velocidade do veículo à frente (km/h)
# 3. Leitura do sensor radar (ondas de rádio) 1 (metros)
# 4. Leitura do sensor lidar (pulsos de luz laser) 2 (metros)
# 5. Leitura do sensor câmera 3 (metros)
# 6. Atrito da via (ex: 0.8 para pista seca, 0.4 para pista molhada, 0.25 baixa
# aderência)
# 7. Nível de sensibilidade ADAS (1 = esportivo, 2 = normal, 3 = seguro)
# 8. Distância da faixa esquerda (metros)
# 9. Distância da faixa direita (metros)

#entradas
vel_atual = float(input('Velocidade do veículo atual (km/h): '))
vel_frente = float(input('Velocidade do veículo à frente (km/h): '))



#funções matematicas
def mediana(a,b,c):
    if (a > b):
        if (b > c):
            return b
        elif (a > c):
            return c
        else:
            return a
    else:
        if (a > c):
            return a
        elif (b > c):
            return c
        else:
            return b

#sensores
vel_rel = vel_atual - vel_frente

def analise_colisao(vel_rel, dis_val, dis_seg):
    if vel_rel <= vel_rel:
        mensagem = 'Status: Seguro'
    elif dis_val > dis_seg:
            mensagem = 'Status: Seguro'
    elif (dis_val < dis_seg) and (dis_val >= dis_seg * 0.5):
        mensagem = 'Status: Atenção'
    else:
        mensagem = 'Status: Perigo'
    print(mensagem)

def faixa_dinamico():
