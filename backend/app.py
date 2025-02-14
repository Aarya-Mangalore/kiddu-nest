from flask import Flask, request, jsonify
import pandas as pd
import os
from datetime import datetime

app = Flask(__name__)
FILE_PATH = "diary.xlsx"

# Initialize the Excel file if it doesn't exist
def init_excel():
    if not os.path.exists(FILE_PATH):
        df = pd.DataFrame(columns=["Date", "Text"])
        df.to_excel(FILE_PATH, index=False)

init_excel()

def load_notes():
    """Load notes from Excel."""
    return pd.read_excel(FILE_PATH)

def save_notes(df):
    """Save notes back to Excel."""
    df.to_excel(FILE_PATH, index=False)

@app.route("/notes", methods=["GET"])
def get_notes():
    """Get all notes."""
    df = load_notes()
    return jsonify(df.to_dict(orient="records"))

@app.route("/notes", methods=["POST"])
def add_note():
    """Add a new note."""
    data = request.json
    df = load_notes()
    new_note = {"Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Text": data["text"]}
    df = df.append(new_note, ignore_index=True)
    save_notes(df)
    return jsonify({"message": "Note added successfully!"}), 201

@app.route("/notes/<int:index>", methods=["PUT"])
def update_note(index):
    """Edit a note."""
    data = request.json
    df = load_notes()
    
    if index >= len(df):
        return jsonify({"error": "Note not found"}), 404

    df.at[index, "Text"] = data["text"]
    save_notes(df)
    return jsonify({"message": "Note updated successfully!"})

@app.route("/notes/<int:index>", methods=["DELETE"])
def delete_note(index):
    """Delete a note."""
    df = load_notes()
    
    if index >= len(df):
        return jsonify({"error": "Note not found"}), 404

    df = df.drop(index)
    df.reset_index(drop=True, inplace=True)
    save_notes(df)
    return jsonify({"message": "Note deleted successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
