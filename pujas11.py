# -*- coding: utf-8 -*-
"""2114951030ps.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15u667u8XGvcaVdJfCONL8xqq9EUU-uj2

# Importing libraries and dataset
"""

import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import defaultdict

from google.colab import drive
drive.mount('/content/drive')

graph_df = pd.read_csv('/content/drive/MyDrive/dmproject/graph.csv')
content_df = pd.read_csv('/content/drive/MyDrive/dmproject/content.csv')

print(graph_df.head())
print(content_df.head())

"""Create a directed graph"""

web_graph = nx.DiGraph()

# Add edges to the graph from the DataFrame
for _, row in graph_df.iterrows():
    web_graph.add_edge(row["Source"], row["Target"])

# Create a dictionary to store content for each website
web_content = dict(zip(content_df["URL"], content_df["Content"]))

"""Load contents into a dictionary

# Task 02: Visualize the graph using networkx
"""

plt.figure(figsize=(10, 10))
nx.draw(web_graph, with_labels=True, node_size=1000, node_color="green", font_size=8, font_color="black", arrowsize=5)
plt.title("Web Graph Visualization")
plt.show()

"""# Task 03 (Bonus): Tokenize and clean contents"""

import nltk
nltk.download('stopwords')

nltk.download('punkt')

import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

url_to_content = dict(zip(content_df['URL'], content_df['Content']))

stop_words = set(stopwords.words('english'))
processed_content = {}

# Tokenize and remove stopwords
for url, content in url_to_content.items():
    tokens = word_tokenize(content.lower())  # Tokenize and convert to lowercase
    filtered_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]  # Remove stopwords and non-alphanumeric words
    processed_content[url] = filtered_tokens

"""# Task 04: Build an inverted index"""

def inverted_index(web_content):
    inverted_index = {}
    for website, content in web_content.items():
        for word in content:
            if word not in inverted_index:
                inverted_index[word] = []
            inverted_index[word].append(website)
    return inverted_index

# Build the inverted index for the cleaned content
index = inverted_index(cleaned_web_content)

# Print the inverted index for a sample word
print(f"Inverted index for the word 'python': {index.get('python', [])}")

"""# Task 05: Single word query-based search system"""

G = nx.DiGraph()

# Add edges to the graph based on the CSV data
for index, row in graph_df.iterrows():
    source = row['Source']  # Assuming 'Source' and 'Target' are the column names
    target = row['Target']
    G.add_edge(source, target)

# Compute the PageRank of all pages
pagerank = nx.pagerank(G)

# Sort the pages based on their pagerank values
sorted_pagerank = sorted(pagerank.items(), key=lambda x: x[1], reverse=True)

# Display the top 5 pages
top_pages = sorted_pagerank[:5]
print("Top pages based on PageRank:")
for page, rank in top_pages:
    print(f"Page: {page}, Rank: {rank}")

print(content_df.columns)

web_content = dict(zip(content_df['URL'], content_df['Content']))

# Print the web content dictionary
print(web_content)

# Tokenize and clean the first content
sample_content = web_content.get(content_df['URL'].iloc[0], "")
tokens = word_tokenize(sample_content.lower())  # Tokenize and convert to lowercase

# Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]

# Print filtered tokens
print(filtered_tokens)

import networkx as nx
import matplotlib.pyplot as plt

# Example graph (ensure you're creating a graph)
G = nx.Graph()

# Add nodes and edges
G.add_edge('Page 1', 'Page 2')
G.add_edge('Page 2', 'Page 3')

# Draw the graph
nx.draw(G, with_labels=True)
plt.show()

"""# Task 06 (Bonus): Bag of words query-based search system
