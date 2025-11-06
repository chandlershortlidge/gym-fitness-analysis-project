import pandas as pd
from pathlib import Path

def load_data(filepath):
    """Load data from CSV file."""
    # convert path to object if it's a string
    filepath = Path(filepath)

    #check file exits 
    if not filepath.exists():
        raise FileNotFoundError(f"Can't find file: {filepath}")
    
    df = pd.read_csv(filepath)

    return df 

    
def remove_outliers(df, columns, method='iqr'):
    """Remove outliers using specified method."""
    # Implementation

    
def create_features(df):
    """Create derived features."""
    # Implementation
    
def clean_pipeline(filepath):
    """Run full cleaning pipeline."""
    df = load_data(filepath)
    df = remove_outliers(df)
    df = impute_missing_values(df)
    df = create_features(df)
    return df