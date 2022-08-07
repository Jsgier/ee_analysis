filename = "lightning_conn_params.txt"

#params is a dictionary composed of parameter names and values
params = {}

#write parameters to file
with open(filename, 'w') as f:
    for parameter in params:
        f.write(f"{} = {}\n", parameter, params[parameter])

