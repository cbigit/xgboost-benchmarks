from sklearn.datasets import load_boston
import numpy as np
import xgboost as xgb

# Load Boston Housing dataset
X, y = load_boston(return_X_y=True)

# Label for the output
STATS = '#, median, mean, std_dev, min_time, max_time, quantile_10, quantile_90'


def get_test_data(size: int = 1):
    """Generates a test dataset of the specified size""" 
    num_rows = len(X)
    test_df = X.copy()

    while num_rows < size:
        test_df = np.append(test_df, test_df, axis=0)
        num_rows = len(test_df)

    return test_df[:size]

##CB
def cnvrg_log_stats(median, mean, std_dev, min_time, max_time, quantile_10, quantile_90):
    print("cnvrg_tag_mean: ",mean)
    print("cnvrg_tag_median: ",median)
    print("cnvrg_tag_std_dev: ",std_dev)
    print("cnvrg_tag_max_time: ",max_time)
    print("cnvrg_tag_min_time: ",min_time)
    print("cnvrg_tag_quantile_10: ",quantile_10)
    print("cnvrg_tag_quantile_90: ",quantile_90)
    
#def calculate_stats(time_list):
def calculate_stats(num_observations, time_list):
    """Calculate mean and standard deviation of a list"""
    time_array = np.array(time_list)

    median = np.median(time_array)
    mean = np.mean(time_array)
    std_dev = np.std(time_array)
    max_time = np.amax(time_array)
    min_time = np.amin(time_array)
    quantile_10 = np.quantile(time_array, 0.1)
    quantile_90 = np.quantile(time_array, 0.9)

    ##CB
    cnvrg_stats([num_observations, median, mean, std_dev, min_time, max_time, quantile_10, quantile_90])
    
    return [median, mean, std_dev, min_time, max_time, quantile_10, quantile_90]
    #return [median, mean, std_dev, min_time, max_time, quantile_10, quantile_90
        
def cnvrg_stats(in_list):
    metrics = ["#", "median", "mean", "std_dev", "min_time", "max_time", "quantile_10", "quantile_90"]
    num=in_list[0]
    
    mp = []
    print("cnvrg_tag_#: ", num);
    for idx, m in enumerate(metrics[1:]):
        print('cnvrg_tag_' + str(num) + '_' + m + ': ', in_list[idx]);
    return mp
    
