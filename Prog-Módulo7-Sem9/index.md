# 📘 Aprendizado Contínuo em Modelos de Linguagem

## Introdução
Os Modelos de Linguagem de Grande Escala (LM's) são verdadeiros tesouros de conhecimento, recheados de informações coletadas durante seu treinamento em enormes bases de dados textuais. Eles têm se mostrado incrivelmente valiosos, ajudando-nos em tarefas como responder perguntas, verificar informações e também conduzir diálogos abertos. Porém, existe um desafio: vivemos em um mundo que está sempre mudando, sempre em plena alteração, e esses modelos, por mais avançados que sejam, podem ficar para trás, com informações obsoletas ou incorretas. Isso é o que chamamos de "concept drift", e é um grande desafio manter esses modelos atualizados e relevantes, assim introduzindo também o conceito de MLOps, que seria a aplicação de DevOps em Machine Learning.

## Solução Proposta
### 🖼 Diagrama de Blocos
<img src="https://imgur.com/3DQWBGx.png"/>

### Descrição dos Blocos
A solução que foi proposta por mim com base no artigo disponibilizado envolve uma técnica chamada "Continual Knowledge Learning" (CKL). O objetivo do CKL é lidar com desafios que não eram atendidos por métodos anteriores de aprendizado contínuo, ajustando os parâmetros do modelo para aprender e reter conhecimento em tempo real da maneira mais eficiente possível.

1. **Modelo de Linguagem Pré-treinado:**
   Este é o nosso ponto de partida, o modelo que já tem uma base sólida de conhecimento do mundo, mas que precisa de ajustes constantes para se manter atualizado.

2. **Módulo de Atualização de Conhecimento:**
   Este é o ponto principal da solução proposta, responsável por identificar e aplicar as atualizações necessárias no modelo.
   - **Detector de Concept Drift:** É como um radar, sempre atento a áreas do conhecimento que precisam de revisão e atualização no modelo atual.
   - **Atualizador de Conhecimento:** Este é o mecanismo que irá de fato fazer as atualizações, alterando o modelo com base nas necessidades identificadas pelo "radar" citado acima.

3. **Módulo de Aprendizado Contínuo:**
   Aqui é onde o modelo continua seu desenvolvimento, aprendendo com novas informações e adaptando-se a novos conhecimentos.
   - **Aquisição de Novo Conhecimento:** Este subcomponente está sempre em busca de novas informações, integrando-as ao modelo.
   - **Retenção de Conhecimento:** Este é o filtro de todo o conhecimento relevante adquirido, desse modo, esse têm como função decidir o que deve ser mantido e o que pode ser descartado, tendo em vista que muito dos conhecimentos que foram adquiridos já podem existir na base de dados e assim se tornarem redundantes, ou mesmo, podem estar presente na base atual em forma de sinônimos, havendo assim a necessidade de descarte.

4. **Base de Dados:**
   Este é o local de onde o modelo consome as informações, uma junção de todos os dados novos e antigos que alimentam o processo de aprendizado contínuo, fazendo assim, com que o modelo disponha de todos esses dados quando esse for treinar.

## Conclusão
O CKL é uma estratégia muito importante para manter a relevância dos nossos modelos de linguagem em um mundo que sofre com constantes alterações. Utilizar esse método têm suas dificuldades, pois exige um processo bem cuidadoso e delicado entre a aquisição de novos conhecimentos e a retenção de informações que realmente fazem sentidos de serem atualizadas ou adicionadas. Ter modelos de linguagem que podem se adaptar e evoluir com o mundo significa ter uma fonte sempre atualizada e confiável de informações, o que é importante para muitas aplicações práticas, desde pesquisa acadêmica até o real desenvolvimento de tecnologias novas.

## 📚 Referências Bibliográficas
JANG, Joel et al. Towards Continual Knowledge Learning of Language Models. 2022. Disponível em: https://arxiv.org/abs/2110.03215. Acesso em: 28/09/2023