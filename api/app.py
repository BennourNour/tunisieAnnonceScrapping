from flask import Flask, jsonify
import pandas as pd


app = Flask(__name__)

# Read the CSV file into a DataFrame
def read_csv():
    try:
        df = pd.read_csv('../tunisie_annonce_listings.csv')  # Path to your CSV file
        return df
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        return None


@app.route('/annonces', methods=['GET'])
def get_annonces():
    df = read_csv()
    if df is not None:
        annonces = df.to_dict(orient='records')  
        return jsonify(annonces)
    else:
        return jsonify({"error": "Failed to read the CSV file"}), 500


@app.route('/scrape', methods=['POST'])
def scrape():
    
    return jsonify({"message": "Scraping triggered successfully!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
