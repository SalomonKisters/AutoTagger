import pandas as pd
import os

def load_tsv(file_number):
    file_path = f"results/image_analysis_results_{file_number}.tsv"
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    return pd.read_csv(file_path, sep='\t')

def query_tsv(query, file_number):
    df = load_tsv(file_number)
    
    query = query.lower()
    df['File Path'] = df['File Path'].astype(str).str.lower()
    df['Parsed Answer'] = df['Parsed Answer'].astype(str).str.lower()

    df['Match Score'] = df.apply(lambda row: (query in row['File Path']) + (query in row['Parsed Answer']), axis=1)
    df_filtered = df[df['Match Score'] > 0]
    
    # Sort by match score
    df_sorted = df_filtered.sort_values(by='Match Score', ascending=False)
    
    for index, row in df_sorted.iterrows():
        print(f"File Path: {row['File Path']}, Parsed Answer: {row['Parsed Answer']}")
        
if __name__ == "__main__":
    query = input("Enter the search query: ")
    file_number = input("Enter the file number of the tsv you want to search: ")
    try:
        query_tsv(query, file_number)
    except Exception as e:
        print(f"An error occurred: {e}")
