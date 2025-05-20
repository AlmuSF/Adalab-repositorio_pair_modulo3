# Cantidad de nulos:

def null_inspect(df,ascending):
# % nulos
    nulos = df.isnull().sum()/df.shape[0]*100
# % nulos ordenados de mayor a menor
    nulos.sort_values(ascending=ascending)


#nulos>0
def non_zero_null():
    nulos = nulos[nulos > 0]
    nulos.sort_values(ascending=False)

