
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load CSV file
def load(path):
    return pd.read_csv(path)

# Boxplots for metrics
def box(df, metrics):
    figs = []
    for metric in metrics:
        if metric in df.columns:
            fig, ax = plt.subplots(figsize=(8, 5))
            sns.boxplot(data=df, x='Country', y=metric, ax=ax)
            ax.set_title(f'{metric} Distribution by Country')
            ax.set_ylabel(f'{metric} (W/m²)')
            figs.append(fig)
    return figs

# Average GHI summary
def ghi(df_list):
    combined = pd.concat(df_list, ignore_index=True)
    if "GHI" in combined.columns:
        avg = combined.groupby('Country', as_index=False)['GHI'].mean().sort_values('GHI', ascending=False)
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.barplot(data=avg, x='Country', y='GHI', palette='viridis', ax=ax)
        ax.set_title('Average GHI by Country')
        ax.set_ylabel('GHI (W/m²)')
        ax.set_xlabel('Country')
        return fig
    return None

# Investment score summary
def score(df_list):
    def calc(df):
        df = df[(df["GHI"] > 0) & (df["DNI"] > 0)]
        return df["GHI"].mean() + df["DNI"].mean()
    scores = {df["Country"].iloc[0]: calc(df) for df in df_list}
    score_df = pd.DataFrame(list(scores.items()), columns=["Country", "Investment Score"])
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(score_df["Country"], score_df["Investment Score"], color=["#4C5B8A", "#2A8C8C", "#6BBF59"])
    ax.set_title("Strategic Investment Priority by Country")
    ax.set_xlabel("Country")
    ax.set_ylabel("Investment Score")
    return fig

# Monthly average GHI line chart
def monthly(df_list):
    def prep(df):
        df = df.copy()
        df = df[["Timestamp", "GHI", "DNI", "DHI", "Country"]]
        df = df[(df["GHI"] > 0) & (df["DNI"] > 0) & (df["DHI"] > 0)]
        df["Month"] = pd.to_datetime(df["Timestamp"]).dt.month
        return df
    cleaned = [prep(df) for df in df_list]
    combined = pd.concat(cleaned, ignore_index=True)
    monthly_avg = combined.groupby(["Country", "Month"])[["GHI", "DNI", "DHI"]].mean().reset_index()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(data=monthly_avg, x="Month", y="GHI", hue="Country", marker="o", ax=ax)
    ax.set_title("Monthly Average GHI by Country")
    ax.set_xlabel("Month")
    ax.set_ylabel("GHI (W/m²)")
    ax.grid(True)
    return fig
