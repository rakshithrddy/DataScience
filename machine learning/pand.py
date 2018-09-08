import pandas as pd

mel_file_path = "C:\\Users\\Rakshith\\Desktop\\melb_data.csv"
mel_data = pd.read_csv(mel_file_path)
mel_data.describe()
