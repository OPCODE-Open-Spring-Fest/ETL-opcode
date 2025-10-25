from pathlib import Path
import pytest
import re
import pandas as pd
from app.etl.extract import extract

def test_empty_file_path():
    path = ""
    with pytest.raises(FileNotFoundError, match=f"❌ File not found: {path}"):
        extract(path)

def test_invalid_file_extension():
    path = "./tests/data/invalid_path.txt"
    with pytest.raises(ValueError, match="File must be a CSV"):
        extract(path)

def test_invalid_encoding(tmp_path):
    bad_file = tmp_path / "invalid_encoding.csv"
    bad_file.write_bytes(b"\xff\xfe\x00\x00\xff")
    encodings = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']
    with pytest.raises(ValueError, match=re.escape(f"Could not read CSV with tried encodings: {encodings}")):
        extract(bad_file)

def test_empty_file():
    path = "./tests/data/empty.csv"
    with pytest.raises(ValueError, match="File contains no data"):
        extract(path)

def test_valid_file(tmp_path):
    csv_file = tmp_path / "valid.csv"
    csv_data = "name,age,city\nAlice,25,Paris\nBob,30,London\n"
    csv_file.write_text(csv_data, encoding="utf-8")
    df = extract(csv_file)
    expected_df = pd.DataFrame({
        "name": ["Alice", "Bob"],
        "age": [25, 30],
        "city": ["Paris", "London"]
    })
    assert isinstance(df, pd.DataFrame)
    pd.testing.assert_frame_equal(df.reset_index(drop=True), expected_df)
