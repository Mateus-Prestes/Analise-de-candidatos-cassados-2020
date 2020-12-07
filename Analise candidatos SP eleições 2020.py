import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

## IMPORTANDO DADOS
consulta_cand2020SP = pd.read_csv('~/Desktop/analise_eleiçoes/consulta_cand_2020/consulta_cand_2020_SP.csv',
delimiter=';', encoding = 'iso-8859-1',error_bad_lines=False)

motivo_cass2020SP = pd.read_csv('~/Desktop/analise_eleiçoes/motivo_cassacao_2020/motivo_cassacao_2020_SP.csv',
delimiter=';', encoding = 'iso-8859-1',error_bad_lines=False)

## Gráfico exibindo quantidade de candidatos cassados e quantidade de candidatos não cassados no estado de SP

## CONJUNTO DE DADOS ->->->

cass=int(len(motivo_cass2020SP['SQ_CANDIDATO'])) 
cand=int(len(consulta_cand2020SP['SQ_CANDIDATO']) - (len(motivo_cass2020SP['SQ_CANDIDATO']))) 

## CRIANDO GRÁFICO E EXIBINDO O GRÁFICO ->->->

labels = ['Cassados', 'Não cassados'] 
candidatos = [cass, cand] 
colors = ['red', 'green'] 
explode = (0.1, 0)

total = sum(candidatos)

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal")) # ->->-> area de plotar e tamanho do grafico

font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }

def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%\n({:d} g)".format(pct, absolute)


wedges, texts, autotexts = ax.pie(candidatos, explode=explode, labels=labels, 
                                colors=colors, autopct=lambda p: '{:.0f}'.format(p * total / 100),
                                shadow=True, startangle=90)
ax.axis('equal')

ax.legend(wedges, candidatos,
        title = 'Candidatos',
        loc = 'center right',
        )

plt.setp(autotexts, size=8, weight="bold")

ax.set_title('Candidatos Cassados', fontdict = font, loc= 'left')

plt.show()

##  Gerando gráfico de motivos de cassação em SP


## CONJUNTO DE DADOS ->->->
motivo = (motivo_cass2020SP.filter(items= [ 'SQ_CANDIDATO', 'DS_MOTIVO_CASSACAO']))

mot = []
valor = []
for i in motivo_cass2020SP['DS_MOTIVO_CASSACAO'] :
    if i not in mot :
        mot.append(str(i))

contas = []
for i in motivo_cass2020SP['DS_MOTIVO_CASSACAO'] :
    for g in range(0, len(mot)):
        if i == mot[g]:
            contas.append(g)

for i in range(0, len(mot)):
    valor.append(contas.count(i))


index = np.arange(len(mot))

## CRIANDO GRÁFICO E EXIBINDO O GRÁFICO->->->
plt.bar(index, valor, color='red')
plt.xlabel('Motivo')
plt.ylabel('Candidatos')
plt.xticks(index, mot, fontsize=6)

plt.title(label='Motivos mais comuns de cassação de candidatos',fontdict= font, fontweight= 30)

plt.show()

## Gráfico de quantidade de candidatos cassados de todos os partidos políticos no estado de SP

## CONJUNTO DE DADOS ->->->

partidos = []
nomepart = []
contas = []
valor = []
cont = 0

for i in motivo_cass2020SP['SQ_CANDIDATO']:
    for x in consulta_cand2020SP['SQ_CANDIDATO']:
        if i == x:
            part = str(consulta_cand2020SP.loc[cont, 'SG_PARTIDO'])
            partidos.append(part)
            cont+=1


for i in partidos:
    if i not in nomepart:
        nomepart.append(i)


for i in partidos :
    for g in range(0, len(nomepart)):
        if i == nomepart[g]:
            contas.append(g)

for i in range(0, len(nomepart)):
    print(nomepart[i], contas.count(i))
    valor.append(contas.count(i))


index = np.arange(len(nomepart))

## CRIANDO GRÁFICO E EXIBINDO O GRÁFICO->->->

plt.bar(index, valor, color='red')
plt.xlabel('Partidos')
plt.ylabel('Nº de Candidatos')
plt.xticks(index, nomepart, fontsize=8)

plt.title(label='Quantia de cassação por partido', fontdict= font, fontweight= 30)

plt.show()
