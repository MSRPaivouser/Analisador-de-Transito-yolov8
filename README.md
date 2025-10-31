# Analisador-de-Transito-yolov8
🚦 Analisador de Trânsito Urbano com YOLOv8 e Python

Este projeto em Python utiliza Visão Computacional (YOLOv8) para detectar, contar e analisar o fluxo de veículos e pedestres em vídeos de trânsito.
Ele combina inteligência visual com análise de dados para gerar relatórios automáticos, gráficos e estatísticas detalhadas sobre o comportamento do tráfego urbano.

🎯 Objetivos do Projeto

Aplicar conhecimentos de Visão Computacional na análise de vídeos reais.

Demonstrar o uso prático da biblioteca YOLOv8 para detecção de múltiplos objetos.

Automatizar a coleta e análise estatística de informações de tráfego.

Utilizar Pandas e Seaborn para criar relatórios e visualizações de dados.

Calcular métricas úteis, como médias e correlação entre o fluxo de carros e pedestres.

Gerar gráficos profissionais e arquivos de saída organizados para uso em pesquisas, estudos ou aplicações futuras.

Integrar conceitos de programação, estatística e inteligência artificial em um único sistema funcional.

🧠 Funcionalidades

Detecção automática de objetos em vídeo, incluindo:

Carros 🚗

Ônibus 🚌

Caminhões 🚚

Motos 🏍️

Bicicletas 🚴

Pedestres 🚶‍♂️

Geração automática de relatórios CSV:

deteccoes_por_frame.csv → Detecção de objetos em cada frame.

contagem_veiculos.csv → Contagem total de cada tipo de objeto.

fluxo_por_segundo.csv → Quantidade de objetos detectados a cada segundo.

contagem_veiculos_percentual.csv → Porcentagem de cada tipo de objeto em relação ao total.

Cálculos estatísticos automáticos:

Média por segundo de cada objeto.

Correlação entre o fluxo de carros e pedestres.

Porcentagem total de cada tipo de objeto.

Geração de gráficos com Seaborn e Matplotlib:

Gráfico de barras com a contagem total.

Gráfico de pizza mostrando a distribuição percentual.

⚙️ Estrutura do Projeto

O projeto é organizado da seguinte forma:

main.py

Pasta resultados, contendo:

deteccoes_por_frame.csv

contagem_veiculos.csv

fluxo_por_segundo.csv

contagem_veiculos_percentual.csv

grafico_barras_quantidade.png

grafico_de_pizza.png

Arquivo de vídeo analisado (exemplo: Traffic.mp4)

🧩 Bibliotecas Utilizadas

ultralytics → Utiliza o modelo YOLOv8 para detecção de objetos.

pandas → Manipulação e análise de dados.

seaborn → Criação de gráficos estatísticos.

matplotlib → Visualização dos dados (barras e pizza).

os → Criação e organização de diretórios de resultados.

🏗️ Como Executar o Projeto

Clone o repositório do projeto no GitHub.

Instale as dependências com o comando:
pip install ultralytics pandas seaborn matplotlib

Coloque o vídeo a ser analisado na pasta principal e nomeie-o como Traffic.mp4 (ou altere o nome no código).

Execute o programa com:
python main.py

Pressione ENTER quando solicitado para iniciar a análise.

📈 Resultados Gerados

Após a execução, os resultados são salvos automaticamente na pasta resultados.

Exemplo de saída no terminal:

📹 Iniciando análise de vídeo...
📄 Detecções detalhadas salvas em resultados/deteccoes_por_frame.csv
📄 Contagem total salva em resultados/contagem_veiculos.csv
📄 Análise de fluxo salva em resultados/fluxo_por_segundo.csv
📄 Porcentagem total salva em resultados/contagem_veiculos_percentual.csv
[📊] Correlação entre fluxo de carros e pedestres: -0.09

🧮 Explicando a Correlação

A correlação mede o quanto duas variáveis estão relacionadas.

+1.0 → Relação perfeita positiva (aumentam juntas).

0.0 → Sem relação aparente.

-1.0 → Relação negativa (quando uma aumenta, a outra diminui).

Neste projeto, a correlação é calculada entre o número de carros e pedestres detectados por segundo.
Por exemplo, uma correlação de -0.09 indica que não há relação significativa entre o fluxo de veículos e pedestres no vídeo analisado.

🖼️ Gráficos Gerados

Gráfico de Pizza:
Mostra a distribuição percentual dos objetos detectados.
Arquivo gerado: resultados/grafico_de_pizza.png

Gráfico de Barras:
Mostra a quantidade total de cada tipo de objeto detectado.
Arquivo gerado: resultados/grafico_barras_quantidade.png
