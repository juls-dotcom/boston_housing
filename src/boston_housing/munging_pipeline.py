import pandas as pd


# Start pipeline
def start_pipeline(dataf):
    """
    Start pipeline
    :param dataf: dataframe to make a copy from
    :return: copied dataframe
    """
    dataf = dataf.copy()
    return dataf


def rename_cols(dataf):
    """
    Renames columns in dataframe
    :param dataf: input dataframe
    :return: dataframe with renamed columns
    """
    dataf = dataf.rename(columns={0: 'crim',
                                  1: 'res_zone',
                                  2: 'indus',
                                  3: 'river',
                                  4: 'nox',
                                  5: 'rooms',
                                  6: 'age',
                                  7: 'distance',
                                  8: 'highways',
                                  9: 'tax',
                                  10: 'pupil_ratio',
                                  11: 'blacks',
                                  12: 'lstats',
                                  13: 'medv'}

                         )
    return dataf


def by_the_river(dataf):
    """
    Add river columns (1=by the river, 0=not by the river)
    :param dataf: dataframe input
    :return: dataframe output
    """
    river_dict = {0: 'Not_by_river',
                  1: 'By_river'}
    dataf['river'] = dataf['river'].map(river_dict)
    dataf['river'] = pd.Categorical(dataf['river'])
    return dataf
