import pandas as pd

file_path = "./GPTStats.csv"
df = pd.read_csv(file_path, nrows=6)


print(df)


# get scaling laws plots
# combine inputs and scaling laws to get scaling laws x time plot


A_chinchilla = 406.4
B_chinchilla = 410.7
alpha_chinchilla = 0.34
beta_chinchilla = 0.28
E_chinchilla = 1.69


def loss_chinchilla(c_flop, D):
    # c_flop: max flop for the training run
    # D: max dataset size
    flop_per_datapoint_training = 6

    N = c_flop / (flop_per_datapoint_training * D)
    

    L = (
        A_chinchilla / N**alpha_chinchilla
        + B_chinchilla / D**beta_chinchilla
        + E_chinchilla
    )
    
