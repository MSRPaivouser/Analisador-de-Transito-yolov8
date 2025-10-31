#BIBLIOTECAS
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

from ultralytics import YOLO
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#FUNÇÕES

#Essa função utiliza a biblioteca YOLO para identificar veículos
#Além de criar um CSV para detecções de objetos por frame
def contar_veiculos(video_path, modelo_path="yolov8x.pt", conf = 0.6):
    modelo = YOLO(modelo_path)

    resultado = modelo(video_path, show=True, conf=conf, stream=True)

    objetos = ["car", "bus", "truck", "person", "motorcycle", "bicycle"]

    contagem = {v: 0 for v in objetos}

    dados = []

    for frame_id, i in enumerate(resultado):
        quadrados = i.boxes
        for r in quadrados:
            classe = modelo.names[int(r.cls[0])]
            if classe in objetos:
                contagem[classe] += 1
                dados.append({"frame": frame_id, "classe": classe})

    df_detalhado = pd.DataFrame(dados)
    os.makedirs("resultados", exist_ok=True)
    df_detalhado.to_csv("resultados/deteccoes_por_frame.csv", index=False)
    print("📄 Detecções detalhadas salvas em resultados/deteccoes_por_frame.csv")

    return contagem, df_detalhado


#Essa função cria um dataframe com a contagem dos objetos e cria um CSV com a contagem
def salvar_dataframe(contagem, nome_arquivo="resultados/contagem_veiculos.csv"):
    os.makedirs("resultados", exist_ok=True)

    df = pd.DataFrame(list(contagem.items()), columns=["Tipo de Objeto", "Quantidade"])
    df.to_csv(nome_arquivo, index=False)
    print("📄 Contagem total salva em resultados/contagem_veiculos.csv")

    print(df)
    return df


#Analisa a quantidade de cada objeto por segundo de vídeo
def analise_fluxo(df, fps=30):
    df["tempo_seg"] = (df["frame"] / fps).astype(int)
    resumo = df.groupby(["tempo_seg", "classe"]).size().unstack(fill_value=0)

    resumo.to_csv("resultados/fluxo_por_segundo.csv")
    print("📄 Análise de fluxo salva em resultados/fluxo_por_segundo.csv")

    return resumo


#Faz a média por segundo de cada objeto
def media_por_segundo(arquivo="resultados/fluxo_por_segundo.csv"):
    df = pd.read_csv(arquivo)
    medias = df.drop(columns=["tempo_seg"]).mean()

    print("MÉDIA POR SEGUNDO DE CADA OBJETO:")
    for tipo, media in medias.items():
        print(f"{tipo.capitalize()}: {media:.2f}")

    return medias


#Calcula e salva a porcentagem total de cada objeto
def porcentagem(arquivo="resultados/contagem_veiculos.csv"):
    df = pd.read_csv(arquivo)
    total = df["Quantidade"].sum()
    df["Porcentagem (%)"] = (df["Quantidade"] / total) * 100

    df.to_csv("resultados/contagem_veiculos_percentual.csv", index=False)
    print("📄 Porcentagem total salva em resultados/contagem_veiculos_percentual.csv")
    print("🚕---------------------------------🚓-----------------------------------🚗")
    print("🚧----------- 📊 PORCENTAGEM TOTAL DE CADA OBJETO DETECTADO ------------🚧")
    print("🚕---------------------------------🚓-----------------------------------🚗")
    for _, linha in df.iterrows():
        print(f"{linha['Tipo de Objeto'].capitalize()}: {linha['Porcentagem (%)']:.2f}%")

    return df


#Calcula correlação entre carros e pedestres
def correlacao(arquivo="resultados/fluxo_por_segundo.csv"):
    df = pd.read_csv(arquivo)
    df.columns = df.columns.str.strip().str.lower()

    if "car" not in df.columns or "person" not in df.columns:
        print(f"⚠️ Colunas disponíveis: {list(df.columns)}")
        return None

    correlacao = df["car"].corr(df["person"])
    print(f"[📊] Correlação entre fluxo de carros e pedestres: {correlacao:.2f}")
    return correlacao


#Gráfico de pizza (porcentagem)
def grafico_pizza(arquivo="resultados/contagem_veiculos_percentual.csv"):
    df = pd.read_csv(arquivo)
    df = df[df["Porcentagem (%)"] > 0]

    sns.set_theme(style="whitegrid")
    cores = sns.color_palette("dark", len(df))

    plt.figure(figsize=(7,6))
    plt.pie(
        df["Porcentagem (%)"],
        labels=None,
        autopct="%1.1f%%",
        startangle=90,
        colors=cores,
        textprops={"fontsize": 11, "color": "black"},
    )

    legend_labels = [f"{tipo} - {porc:.1f}%" for tipo, porc in zip(df["Tipo de Objeto"], df["Porcentagem (%)"])]
    plt.legend(
        legend_labels,
        title="Objetos Detectados",
        loc="center right",
        bbox_to_anchor=(1, 0.5),
        fontsize=10,
        title_fontsize=11
    )

    plt.title("Distribuição Percentual de Objetos Detectados", fontsize=16, weight="bold")
    plt.axis("equal")

    os.makedirs("resultados", exist_ok=True)
    plt.savefig("resultados/grafico_de_pizza.png", dpi=300, bbox_inches="tight")
    print("📄 Gráfico de pizza salvo em resultados/grafico_de_pizza.png")

    plt.show()


#Gráfico de barras (quantidade)
def grafico_barras(arquivo="resultados/contagem_veiculos.csv"):
    df = pd.read_csv(arquivo)
    df = df.sort_values(by="Quantidade", ascending=False)
    ordem = df["Tipo de Objeto"].tolist()

    sns.set_theme(style="darkgrid")
    plt.figure(figsize=(8,5))

    barra = sns.barplot(
        data=df,
        x="Tipo de Objeto",
        y="Quantidade",
        palette="Blues_r",
        edgecolor="black",
        order=ordem
    )

    for p in barra.patches:
        altura = p.get_height()
        plt.text(
            p.get_x() + p.get_width() / 2,
            altura + (altura * 0.02),
            f"{int(altura)}",
            ha="center",
            fontsize=10,
            weight="bold"
        )

    plt.title("Quantidade de Objetos Detectados", fontsize=15, weight="bold")
    plt.xlabel("Tipo de Objeto", fontsize=12)
    plt.ylabel("Quantidade", fontsize=12)
    sns.despine()

    os.makedirs("resultados", exist_ok=True)
    plt.savefig("resultados/grafico_barras_quantidade.png", dpi=300, bbox_inches="tight")
    print("📄 Gráfico de barras salvo em resultados/grafico_barras_quantidade.png")

    plt.show()


#FUNÇÃO PRINCIPAL
def main():
    print("🚛-------------------ANALISADOR DE TRANSITO URBANO----------------------🚌")
    input("🔹 Pressione ENTER para iniciar a análise do vídeo...")

    print("📹 Iniciando análise de vídeo...")
    contagem, df_detalhado = contar_veiculos("Traffic.mp4")
    salvar_dataframe(contagem)
    print("🚕---------------------------------🚦-----------------------------------🚗")

    analise_fluxo(df_detalhado)
    print("🚕---------------------------------🏃‍♂️-----------------------------------🚗")

    media_por_segundo("resultados/fluxo_por_segundo.csv")
    print("🚕---------------------------------🚚-----------------------------------🚗")

    porcentagem("resultados/contagem_veiculos.csv")
    print("🚕---------------------------------🚓-----------------------------------🚗")

    correlacao("resultados/fluxo_por_segundo.csv")
    print("🚕---------------------------------🏍️-----------------------------------🚗")

    grafico_pizza("resultados/contagem_veiculos_percentual.csv")
    grafico_barras("resultados/contagem_veiculos.csv")


main()
