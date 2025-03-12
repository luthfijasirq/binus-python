import pandas as pd

data = {
    "Country": ["Indonesia", "Japan", "India", "China", "United States", "Brazil", "Russia"],
    "Capital": ["Jakarta", "Tokyo", "New Delhi", "Beijing", "Washington DC", "Brasilia", "Moscow"],
    "Continent": ["Asia", "Asia", "Asia", "Asia", "America", "America", "Asia"],
    "Area": [1905, 377, 3287, 9597, 9834, 8515, 17098],
    "Population": [264, 143, 1252, 1357, 329, 210, 146]
}


df = pd.DataFrame(data)

file_csv = 'data_negara.csv'
df.to_csv(file_csv, index=False)

print(f"Berkas CSV telah ditulis dengan nama: {file_csv}")
    
