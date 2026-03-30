import datetime
import json
import csv
import os

def run_workflow(data):
    now_gmt = datetime.datetime.now(datetime.timezone.utc)
    check_sum = data['promedio'] * data['recuento_num']
    is_valid = (check_sum == data['suma'])
    
    timestamp = now_gmt.strftime("%Y-%m-%d %H:%M:%S UTC")
    
    # Datos para el CSV
    row = [
        timestamp, 
        data['suma'], 
        data['promedio'], 
        data['recuento'], 
        "VALID" if is_valid else "INVALID"
    ]

    # Crear o añadir al archivo historico.csv
    file_exists = os.path.isfile('historico.csv')
    with open('historico.csv', mode='a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['Timestamp', 'Suma', 'Promedio', 'Recuento', 'Status'])
        writer.writerow(row)

    print(f"✅ Registro guardado en historico.csv: {row}")

if __name__ == "__main__":
    input_data = {"suma": 7, "promedio": 3.5, "recuento": 11, "recuento_num": 2, "maximo": 4, "minimo": 3}
    run_workflow(input_data)