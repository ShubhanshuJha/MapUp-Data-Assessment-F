import pandas as pd


# For Question 1
def generate_car_matrix(df) -> pd.DataFrame:
    pivot_df = df.pivot(index='id_1', columns='id_2', values='car').fillna(0)
    for idx in pivot_df.index:
        pivot_df.loc[idx, idx] = 0
    return pivot_df


# For Question 2
def get_type_count(df) -> pd.DataFrame:
    def get_category(v) -> str:
        if v <= 15:
            return "low"
        elif v <= 25:
            return "medium"
        else:
            return "high"

    df['car_type'] = df['car'].apply(lambda val: get_category(val))
    return df


# For Question 3
def get_bus_indexes(df) -> list:
    mean = df['bus'].mean()
    indices = df[df['bus'] > 2 * mean].index.to_list()
    indices.sort()
    return indices


# For Question 4
def filter_routes(df) -> list:
    filtered_routes = df.groupby('route')['truck'].mean()
    filtered_routes = filtered_routes[filtered_routes > 7].index.tolist()
    filtered_routes.sort()
    return filtered_routes


# For Question 5
def multiply_matrix(df) -> pd.DataFrame:
    return df.applymap(lambda x: x * 0.75 if x > 20 else x * 1.25).round(1)


# For Question 6
def verify_completeness(df) -> pd.Series:
    return pd.Series("Sorry, but this question was not much clear to me.")


