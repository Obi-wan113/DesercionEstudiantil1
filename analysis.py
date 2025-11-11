def dropout_rate(df):
  total = len(df)
  dropped = len(df[df["status"] == "Dropped"])
  rate = dropped / total * 100
  return round(rate, 2)

def proporcion_desercion(df):
    dropped_df = df[df["status"] == "Dropped"]

    if dropped_df.empty:
        return 0, None 
    
    total = len(df)
    dropped = len(dropped_df)
    rate = round(dropped / total * 100, 2)

    common_cause = dropped_df["cause"].mode()[0]  

    return rate, common_cause