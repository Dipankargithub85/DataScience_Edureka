import pandas as pd
import matplotlib.pyplot as plt

def getdataframe():
    df = pd.read_csv("D:\\work\\Python\\python_for_edureka_doc\\Module_4\\574_m4_datasets_v3.0\\BigMartSalesData.csv")
    return df

def Plot_Total_Sales_Per_Month():
    dfplot = getdataframe()
    df_grouped_year = dfplot.query("Year == 2011").filter(
        ["Month", "Amount"]).groupby(["Month"], as_index=False).sum()

    # Plot Total Sales Per Month for Year 2011.
    x = df_grouped_year["Month"]
    y = df_grouped_year["Amount"]

    plt.plot(x, y)
    plt.xlabel("Month")
    plt.ylabel("Total Sales")
    plt.title("Month vs sales")
    plt.grid()
    plt.show()

def Plot_Total_Sales_Per_Month_bar():
    dfplotbar = getdataframe()
    df_grouped_year = dfplotbar.query("Year == 2011").filter(
        ["Month", "Amount"]).groupby(["Month"], as_index=False).sum()

    # Plot Total Sales Per Month for Year 2011 as Bar Chart.
    x = df_grouped_year["Month"]
    y = df_grouped_year["Amount"]

    plt.bar(x, y,width = 0.5)
    plt.xlabel("Month")
    plt.ylabel("Total Sales")
    plt.title("Month vs sales")
    plt.grid()
    plt.show()

def part_three_pie():
    dfpie = getdataframe()
    df_grouped_country = dfpie.query("Year == 2011").filter(
        ["Country", "Amount"]).groupby(["Country"], as_index=False).sum()

    plt.pie(df_grouped_country["Amount"],
            labels=df_grouped_country["Country"],
            autopct='%1.1f%%',
            shadow=True)

    plt.tight_layout()
    plt.show()

def part_four_Scatter():
    dfScatter = getdataframe()
    invoice_amounts = dfScatter.filter(["InvoiceDate", "Amount"]).groupby(
        "InvoiceDate", as_index=False).sum()

    plt.scatter(invoice_amounts["InvoiceDate"], invoice_amounts["Amount"])
    plt.ylim(20000, 100000)
    plt.show()


if __name__ == '__main__':
    Plot_Total_Sales_Per_Month()
    Plot_Total_Sales_Per_Month_bar()
    part_three_pie()
    part_four_Scatter()