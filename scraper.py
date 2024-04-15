import requests
import pandas as pd

def fetch_gene_data(gene_id):
    url = f"https://specs.cmgg.be/gene_data/{gene_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None  # Return None if the request was unsuccessful

def process_gene_data(gene_data):
    if not gene_data:
        return None

    # Sort the data by specscore in descending order
    sorted_data = sorted(gene_data, key=lambda x: x['specscore'], reverse=True)
    
    # Prepare the data dictionary with the required fields
    result = {
        'ensembl_gene_id': sorted_data[0]['ensembl_gene_id'],
        'hgnc_symbol': sorted_data[0]['hgnc_symbol']
    }
    
    # Include up to top 5 tissues, handling cases where there may be less than 5
    for i in range(min(5, len(sorted_data))):
        result[f'tissue{i+1}'] = sorted_data[i]['tissue_type']
        result[f'specscore{i+1}'] = sorted_data[i]['specscore']
    
    return result

def main(gene_ids):
    results = []
    
    for gene_id in gene_ids:
        gene_data = fetch_gene_data(gene_id)
        processed_data = process_gene_data(gene_data)
        if processed_data:
            results.append(processed_data)
    
    # Create DataFrame from the results list
    df = pd.DataFrame(results)
    
    # Save the DataFrame to a CSV file
    df.to_csv('your_path', index=False)
    print("Data has been processed and saved to 'gene_data_results.csv'.")

# Gene IDs list
gene_ids = pd.read_csv('your_data.csv')['Ensemble_ID']

# Run the script
main(gene_ids)