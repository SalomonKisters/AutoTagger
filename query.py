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
    df['Tag'] = df['Tag'].apply(eval)  # Convert the Tag column to lists
    
    def calculate_match_score(tags):
        match_score = 0
        for tag in tags:
            tag_lower = tag.lower()
            if tag_lower.startswith(query):
                match_score += 1.5  # More weight if query is at beginning
            elif query in tag_lower:
                match_score += 1
        return match_score
    
    df['Match Score'] = df['Tag'].apply(calculate_match_score)
    df_filtered = df[df['Match Score'] > 0]
    
    # Sort by match score
    df_sorted = df_filtered.sort_values(by='Match Score', ascending=False)
    
    for index, row in df_sorted.iterrows():
        tags = ', '.join(row['Tag'])  # Convert list back to a comma-separated string for display
        print(f"File Path: {row['File Path']}, Tags: [{tags}]")
        
if __name__ == "__main__":
    query = input("Enter the search query: ")
    file_number = input("Enter the file number of the tsv you want to search: ")
    try:
        query_tsv(query, file_number)
    except Exception as e:
        print(f"An error occurred: {e}")
