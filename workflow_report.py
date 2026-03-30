import datetime
import json
import sys

def run_workflow(data):
    # Forzar el reporte en Horario de Greenwich (GMT/UTC)
    now_gmt = datetime.datetime.now(datetime.timezone.utc)
    
    # Lógica de validación interna
    check_sum = data['promedio'] * data['recuento_num']
    is_valid = (check_sum == data['suma'])

    report = {
        "timestamp_gmt": now_gmt.strftime("%Y-%m-%d %H:%M:%S UTC"),
        "status": "OPERATIONAL" if is_valid else "DATA_MISMATCH",
        "analysis": {
            "efficiency": f"{(data['recuento_num'] / data['recuento'] * 100):.2f}%",
            "range_spread": data['maximo'] - data['minimo']
        },
        "raw_data": data
    }

    print("--- REPORTE DE FLUJO GMT ---")
    print(json.dumps(report, indent=4))
    
    if not is_valid:
        print("⚠️ Alerta: Los datos de suma y promedio no coinciden.")
        sys.exit(1)

if __name__ == "__main__":
    # Tus datos de entrada iniciales
    input_data = {
        "suma": 7,
        "promedio": 3.5,
        "recuento": 11,
        "recuento_num": 2,
        "maximo": 4,
        "minimo": 3
    }
    run_workflow(input_data)