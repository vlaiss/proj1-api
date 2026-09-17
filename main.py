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

import math

def converter_km_para_metros(valor_km):
    valor_convertido = valor_km / 3.6
    return (valor_convertido)

#Exigências A
def dis_validada(sens_radar, sens_lidar, sens_camera):
    if sens_radar > sens_lidar:
        if sens_lidar > sens_camera:
            return sens_lidar
        elif sens_radar > sens_camera:
            return sens_camera
        else:
            return sens_radar
    else:
        if sens_radar > sens_camera:
            return sens_radar
        elif sens_lidar > sens_camera:
            return sens_camera
        else:
            return sens_lidar

# Exigências B
def tempo_reacao(tempo_reacao):
    
    tempo_reacao = float(input('''Tempo de reação: 
    Opção 1(esportivo) = 1.0 seg
    Opção 2(normal) = 1.5 seg
    Opção 3(seguro) = 2.0 seg'''))
    
    if tempo_reacao == ('1'):
    tempo_reacao = 1.0

    elif tempo_reacao == ('2'):
    tempo_reacao = 1.5

    elif tempo_reacao == ('3'):
    tempo_reacao = 2.0

    return tempo_reacao

tempo_reacao = tempo_reacao()

def atrito():
  print("""Nível do atrito na via:
    Opção 1: pista seca
    Opção 2: pista molhada
    Opção 3: baixa aderência""")
        
  atrito = int(input("Digite o número da opção: "))

  if atrito == (1):
   atr = 0.8
  elif atrito == (2):
   atr = 0.4
  elif atrito == (3):
   atr = 0.52
  return atr

# Exigências C
def analise_colisao(vel_rel, dis_val, dis_seg):
    mensagem = f'AEB - {status_aeb} \n Status: {status_frontal}'
    if vel_rel <= vel_rel or dis_val > dis_seg:
        status_frontal = 'NORMAL'
        status_aeb = 'não acionado'
    elif (dis_val < dis_seg) and (dis_val >= dis_seg * 0.5):
        status_frontal = 'ATENCAO'
        status_aeb = 'não acionado'
    elif dis_val < dis_seg * 0.5:
        status_frontal = 'RISCO DE COLISÃO'
        status_aeb = 'ACIONADO'
    return status_frontal
    print(mensagem)

# Exigências D
def ajuste_margem(vel_atual):
    if vel_atual > 80:
        margem = 0.5 + (vel_atual - 80) * 0.01
    return margem

def inv_esq(dis_faixa_esq, margem):
    if dis_faixa_esq < margem:
        mensagem = 'PERIGO DE INVASAO'
    elif dis_faixa_esq < margem + 0.2:
        mensagem = 'ATENCAO'
    else:
        mensagem = 'NORMAL'
    return mensagem
    print(mensagem)

def inv_dir(dis_faixa_dir, margem):
    if dis_faixa_dir < margem:
        mensagem = 'PERIGO DE INVASAO'
    elif dis_faixa_dir < margem + 0.2:
        mensagem = 'ATENCAO'
    else:
        mensagem = 'NORMAL'
    return mensagem
    print(mensagem)

# Exigências B
def status_ADAS():

#main
sens_radar = float(input('Leitura do sensor radar (metros): '))
sens_lidar = float(input('Leitura do sensor lidar (metros): '))
sens_camera = float(input('Leitura do sensor câmera (metros): '))

tempo_reacao = tempo_reacao()
atrito = atrito()

vel_atual = float(input('Velocidade do veículo atual (km/h): '))
vel_frente = float(input('Velocidade do veículo à frente (km/h): '))
vel_rel = vel_atual - vel_frente

dis_faixa_esq = float(input('Distância da faixa esquerda (metros): '))
dis_faixa_dir = float(input('Distância da faixa direita (metros): '))

dis_val = dis_validada(sens_radar, sens_lidar, sens_camera)
dis_seg = (vel_rel * tempo_reacao) + ((vel_rel ** 2) / (2 * atrito * 9.81))
analise_colisao(vel_rel, dis_val, dis_seg)  
ajuste_margem(vel_atual)
inv_esq(dis_faixa_esq, margem)
inv_dir(dis_faixa_dir, margem)
status_ADAS()
