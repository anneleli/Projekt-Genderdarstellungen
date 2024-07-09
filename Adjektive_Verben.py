import pandas as pd
import spacy

# Lade das deutsche Sprachmodell
nlp = spacy.load("de_core_news_sm")

# Einlesen der Excel-Datei
def read_excel(file_path):
    df = pd.read_excel(file_path)
    return df

# Filtern nach Wortarten
def filter_words_by_pos(words, pos_tag_to_filter):
    doc = nlp(" ".join(words))
    filtered_words = [token.text for token in doc if token.pos_ == pos_tag_to_filter]
    return filtered_words

# Ergebnisse in eine neue Excel-Datei schreiben
def write_to_excel(adjectives, verbs, output_path):
    df_adjectives = pd.DataFrame(adjectives, columns=['Adjektive'])
    df_verbs = pd.DataFrame(verbs, columns=['Verben'])
    with pd.ExcelWriter(output_path) as writer:
        df_adjectives.to_excel(writer, sheet_name='Adjektive', index=False)
        df_verbs.to_excel(writer, sheet_name='Verben', index=False)

# Hauptfunktion
def main():
    # Pfad zur Excel-Datei
    file_path = '/Users/Computer/Documents/Studium/Master/2. Semester/Projekt/Kollokationen Mann/Kollokationen_Mann.xlsx'
    output_path = 'filtered_words.xlsx'
    
    # Einlesen der Excel-Datei
    df = read_excel(file_path)
    
    # Angenommen, die Wortliste befindet sich in der ersten Spalte
    words = df.iloc[:, 0].tolist()
    
    # Filtern nach Adjektiven (ADJ)
    adjectives = filter_words_by_pos(words, 'ADJ')
    print("Adjektive:", adjectives)
    
    # Filtern nach Verben (VERB)
    verbs = filter_words_by_pos(words, 'VERB')
    print("Verben:", verbs)
    
    # Ergebnisse in eine neue Excel-Datei schreiben
    write_to_excel(adjectives, verbs, output_path)

if __name__ == "__main__":
    main()
