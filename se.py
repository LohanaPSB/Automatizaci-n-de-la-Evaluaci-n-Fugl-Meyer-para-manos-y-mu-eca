import serial
import time
from numpy import interp

def mpu9250():
    ser = serial.Serial('COM8', 9600, timeout=1)
    angulos = {
        'roll': None,
        'yaw': None
    }
    
    try:
        # Lee los datos del puerto serial durante 5 segundos
        start_time = time.time()
        while time.time() - start_time < 5:
            if ser.in_waiting > 15:
                line = ser.readline().decode().strip()
                try:
                    if line.startswith("Roll:"):
                        parts = line.split(": ")
                        if len(parts) == 2:
                            angulos['roll'] = float(parts[1])
                            #print(f"Roll: {angulos['roll']}")
                    
                    elif line.startswith("Yaw:"):
                        parts = line.split(": ")
                        if len(parts) == 2:

                            angulos['yaw'] = float(interp(float(parts[1]) , [-22,-12.5,-2.7,7.9,17,27.5,37.5,50,61.5],[-30,-15,0.0,15.0, 30.0, 45.0, 60.0,75.0, 90.0]))
                            
                except ValueError as e:
                    print(f"Error de valor en la línea '{line}': {e}")
    except Exception as e:
        print(f"Error al leer datos: {e}")
    finally:
        # Cierra la conexión serial
        ser.close()
        return angulos  # Devuelve los ángulos leídos
