import pandas as pd


def load_temp_data(data_dir):
    """
    Load, format and rename columns from our raw chicago data
    """
    df = pd.read_csv(f"{data_dir}/ChicagoWeather2015.csv")
    df['temp_date'] = pd.to_datetime(df['DATE'])    
    df = (df.drop(columns=['STATION', 'NAME', 'DATE'])
          .rename(columns={'TMAX': 'temp_max',
                           'TMIN': 'temp_min'}))

    return df


def temp_max_min_by_month(df):
    """
    return the min and max temperature, by month and year
    """
    df['year'] = df['temp_date'].dt.year
    df['month'] = df['temp_date'].dt.month

    df = (df
          .groupby(['year', 'month'], as_index=False)
          .agg({'temp_max': 'max', 'temp_min': 'min'})
          .sort_values(['year', 'month'])
          )

    return df
