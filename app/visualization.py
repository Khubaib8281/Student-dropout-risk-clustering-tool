import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_score_dist(df):
    fig, ax = plt.subplots(figsize=(8,4))
    sns.histplot(df['total_score'], bins=30, kde=True, ax= ax)
    ax.set_title('Distribution of Total Scores')
    fig.tight_layout()
    return fig


def plot_attendance_vs_score(df):
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.scatterplot(x = df['attendance_percentage'], y = df['total_score'], hue = df['risk_label'], palette='Set2', ax= ax)
    ax.set_title('Attendance Percentage vs Total Score')
    ax.set_xlabel('Attendance Percentage')
    ax.set_ylabel('Total Score')
    fig.tight_layout()
    return fig


import seaborn as sns
import matplotlib.pyplot as plt

def plot_cluster_pca(df):
    fig, ax = plt.subplots(figsize=(8, 4))

    # Plot points by risk label (cluster)
    sns.scatterplot(
        x=df['pca_x'],
        y=df['pca_y'],
        hue=df['cluster'],
        palette='Set1',
        ax=ax,
        edgecolor='black'
    )

    # Add density contours per cluster
    for label in df['risk_label'].unique():
        subset = df[df['risk_label'] == label]
        sns.kdeplot(
            x=subset['pca_x'],
            y=subset['pca_y'],
            hue = df['risk_label'],
            ax=ax,
            levels=1,
            color='black',
            linewidths=1.2,
            linestyle='--'
        )

    ax.set_title('Students Cluster PCA (2D)')
    ax.set_xlabel('Principal Component 1')
    ax.set_ylabel('Principal Component 2')
    fig.tight_layout()
    return fig
