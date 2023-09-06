# Projeto Integrado PUC Minas - Consultor de Investimentos


---

*Preciso adicionar atualização automática do índice Bovespa - IBOV*

(https://www.b3.com.br/pt_br/market-data-e-indices/indices/indices-amplos/indice-ibovespa-ibovespa-composicao-da-carteira.htm) [link]

### Introdução

1.1. Contexto

O interesse na construção desse projeto surgiu ao acompanhar o mercado financeiro brasileiro e avaliar a dificuldade de fazer boas escolhas na hora de comprar um ativo na bolsa de valores.
O contexto de uso do projeto é para pessoas fora do mercado financeiro, mas que querem fazer boas compras e escolhas mais assertivas na hora de realizar uma operação de compra no mercado financeiro.

1.2. Objetivos

O objetivo principal é trazer para o usuário final em quanto tempo ele terá o retorno desejado em um ativo específico selecionado por ele. O intuito é que essa ferramenta seja utilizada em situações do cotidiano e que possibilite profissionais de fora do mercado financeiro realizar uma operação com um mínimo de previsibilidade sem desprender horas analisando balanços patrimoniais e indicadores técnicos.

1.3. Público alvo

Esse projeto destina-se a profissionais que não dominam o mercado financeiro, mas possuem uma reserva e querem otimizar os seus rendimentos.
Temos dois perfis principais o profissional que já conhece do mercado e tem uma base teórica, mas não possui tempo suficiente para validar suas teorias. O segundo perfil é o usuário que não domina o mercado financeiro, mas possui recursos próprios e quer otimizá-los investindo na bolsa, mas este não tem tempo e nem conhecimento técnico para isso.


### Como atualizar esse projeto

O projeto está dividido em alguns arquivos .py que possuem funções específicas.

 - _settings: É nesse arquivo que configuramos o acesso a base de dados, caminho dos datasets e etc
 - main: Esse módulo chamará todas os demais módulos sendo responsável por criar e manter a base de dados para que o nosso modelo preditivo seja alimentado com novos dados
 - _yfinance: Esse arquivo coleta o histórico de cotação das moedas dos últimos 3 anos.
 - _ibov: Gera um CSV com o índice BOVESPA atualizado para ser utilizado como dimensão do projeto
 - _news: Coleta 10 notícias de cada papel dentro do índice para ser utilizado no modelo preditivo
 - _utils: Nesse modulo temos todas as funções úteis do projeto como insert no banco de dados, criação de tabelas e etc.
 - _fundamentus: Coleta os dados fundamentalitas das empresas do índice para ser usado nas camadas gerenciais, analíticas e preditivas do projeto

