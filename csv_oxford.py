from scipy.io import loadmat
import pandas as pd

data = loadmat(r"original_data\Oxford\Oxford_Battery_Degradation_Dataset_1.mat")
data = {k: v for k, v in data.items() if not k.startswith('_')}
myData = {k:{'t':[], 'v':[], 'a':[], 'T':[]} for k in data}

for key in data:
    cell1 = data[key][0, 0]
    field_names = cell1.dtype.names

    t = []
    v = []
    a = []
    T = []

    for name in field_names:
        cyc0000 = cell1[name][0, 0]

        first_entry = cyc0000[0][0]

        time_data = first_entry['t'][0][0]
        voltage_data = first_entry['v'][0][0]
        current_data = first_entry['q'][0][0]
        temperature_data = first_entry['T'][0][0]

        #print("Time:", time_data[0])
        #print("Voltage:", voltage_data[0])
        #print("Current:", current_data[0])
        #print("Temperature:", temperature_data[0])

        t.append(time_data[0])
        v.append(voltage_data[0])
        a.append(current_data[0])
        T.append(temperature_data[0])

    myData[key]['t'] = t
    myData[key]['v'] = v
    myData[key]['a'] = a
    myData[key]['T'] = T

for key in myData:
    df = pd.DataFrame({
        'Time': myData[key]['t'],
        'Voltage': myData[key]['v'],
        'Current': myData[key]['a'],
        'Temperature': myData[key]['T']
    })
    
    df.to_csv(f"csv_data/Oxford_LIB_Degradation/{key}.csv", index=False)