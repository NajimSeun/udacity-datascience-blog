

def get_incomp_cols(df):
    return [col for col in df.columns if df[col].count() < df.shape[0]]
