import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Datei Pfad
file_path = '/Users/Computer/Documents/Studium/Master/2. Semester/Projekt/word2vec/Ähnlichkeiten/Ähnlichste Wörter_Neutral.xlsx'

# Laden der Excel Datei
excel_data = pd.read_excel(file_path, sheet_name=None)

# Netzwerk erstellen
G = nx.Graph()

# Hinzufügen der Hauptwörter und ihrer ähnlichen Wörter
hauptwoerter = set(excel_data.keys())
for sheet in excel_data.keys():
    data = excel_data[sheet]
    main_word = sheet  # Hauptwort ist der Name des Reiters
    G.add_node(main_word, color='yellow', size=300)
    for index, row in data.iterrows():
        similar_word = row[0]
        similarity = row[1]
        if similar_word not in hauptwoerter:  # Sicherstellen, dass ähnliche Wörter keine Hauptwörter sind
            G.add_node(similar_word, color='blue', size=1)
        G.add_edge(main_word, similar_word, weight=similarity)

# Farben und Größen der Knoten extrahieren
colors = [G.nodes[node]['color'] for node in G.nodes]
sizes = [G.nodes[node]['size'] for node in G.nodes]

# Anzahl der Hauptwörter überprüfen
num_hauptwoerter = sum(1 for node in G.nodes if G.nodes[node]['color'] == 'red')
print(f"Anzahl der Hauptwörter: {num_hauptwoerter}")

# Netzwerk zeichnen
pos = nx.spring_layout(G)  # Positionierung der Knoten

plt.figure(figsize=(15, 15))
nx.draw(G, pos, with_labels=True, node_color=colors, node_size=sizes, edge_color='grey', font_size=10, font_color='black')
plt.title("Ähnlichste Wörter Netzwerk")

# Speichern der Abbildung als PDF
plt.savefig('aehnlichste_woerter_netzwerk.pdf', format='pdf')
plt.show()
plt.close()
