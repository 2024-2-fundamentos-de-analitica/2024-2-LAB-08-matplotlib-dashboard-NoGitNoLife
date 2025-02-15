# pylint: disable=line-too-long


import matplotlib.pyplot as plt
import pandas as pd 
import os

def load_data():
    csvloc = "files/input/shipping-data.csv"
    df = pd.read_csv(csvloc)
    return df

def create_visual_for_shipping_per_warehouse(df, docdest):
    df = df.copy()
    plt.figure()
    counts = df.Warehouse_block.value_counts()
    counts.plot.bar(
        title = "Shipping per Warehouse",
        xlabel = "Warehouse block",
        ylabel = "Record Count", 
        color = "tab:blue",
        fontsize=8,
    )
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.savefig(os.path.join(docdest, "shipping_per_warehouse.png"))

def create_visual_for_mode_of_shipment(df, docdest):
    df = df.copy()
    plt.figure()
    counts = df.Mode_of_Shipment.value_counts()
    counts.plot.pie(
        title = "Mode of shipment",wedgeprops = dict(width = 0.35),
        ylabel = "",
        color = ["tab:blue", "tab:orange", "tab:green"]
    )   
    plt.savefig(os.path.join(docdest, "mode_of_shipment.png"))

def create_visual_for_average_customer_rating(df, docdest):
    df = df.copy()
    plt.figure()
    df = (
        df [["Mode_of_Shipment", "Customer_rating"]]
        .groupby("Mode_of_Shipment")
        .describe()
    )

    df.columns = df.columns.droplevel()
    df = df[["mean", "min", "max"]]
    plt.barh(
        y = df.index.values,
        width = df ["max"].values -1,
        left = df["min"].values,
        height = 0.9,
        color = "lightgray",
        alpha = 0.8,
    )

    colors = [
        "tab:green" if value >= 3.0 else "tab:orange" for value in df["mean"].values
    ]

    plt.barh(
        y = df.index.values,
        width = df["mean"].values -1,
        left = df ["min"].values,
        color = colors,
        height = 0.5,
        alpha = 1.0,    
    )

    plt.title("Average Customer Rating")
    plt.gca().spines["left"].set_color("gray")
    plt.gca().spines["bottom"].set_color("gray")
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
           
    plt.savefig(os.path.join(docdest, "average_customer_rating.png"))

def create_visual_for_weight_distribution(df, docdest):
    df = df.copy()
    plt.figure()
    df.Weight_in_gms.plot.hist(
        title = "Shipped Weight Distribution",
        color = "tab:orange",
        edgecolor = "white",
    )

    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.savefig(os.path.join(docdest, "weight_distribution.png"))

def generate_html(docdest):
    html_content = """
    <!DOCTYPE html>
    <html>
        <body>
            <h1>Shipping Dashboard Example</h1>
            <div style="width:45%;float:left">
                <img src="shipping_per_warehouse.png" alt="Fig 1">
                <img src="mode_of_shipment.png" alt="Fig 2">
            </div>
            <div style="width:45%;float:left">
                <img src="average_customer_rating.png" alt="Fig 3">
                <img src="weight_distribution.png" alt="Fig 4">
            </div>
        </body>
    </html>
    """
    with open(os.path.join(docdest, "index.html"), "w") as f:
        f.write(html_content)

def pregunta_01():
    docdest = "docs"
    #   Create the directory if it doesn't exist
    if not os.path.exists(docdest):
        os.makedirs(docdest)
    
    df = load_data()
    create_visual_for_shipping_per_warehouse(df, docdest)
    create_visual_for_mode_of_shipment(df, docdest)
    create_visual_for_average_customer_rating(df, docdest)
    create_visual_for_weight_distribution(df, docdest)
    generate_html(docdest)

pregunta_01()








