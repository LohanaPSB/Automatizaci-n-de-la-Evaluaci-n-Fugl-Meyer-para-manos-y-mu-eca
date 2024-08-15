import serial
import numpy as np
import time
from numpy import interp
from scipy.interpolate import interp1d
from scipy.signal import savgol_filter

# Configura la conexión serial
  # Reemplaza 'COM8' con el puerto serial correcto


def leer_angulo(mano):
    ser = serial.Serial('COM8', 9600)
    angulos = {
    'PD': None,
    'ID': None,
    'MD': None,
    'MI': None,
    'II': None,
    'PI': None,
    'Flex1': None,
    'Flex2': None,
    'Flex3': None,
    'Flex4': None
    }
    try:
        # Lee los datos del puerto serial durante 5 segundos
        start_time = time.time()
        while time.time() - start_time < 10:
            if ser.in_waiting > 0:
                line = ser.readline().decode().strip()
                try:
                    if line.startswith("A1:") :
                        parts = line.split(": ")
                        if len(parts) == 2 and parts[1].isdigit():
                            valor_digital1 = int(parts[1])
                            tension1 = (valor_digital1 / 1023) * 3.346
                            
                            angulos['PD'] =float(interp(tension1, [0.15,0.166,0.42,0.683,0.974,1.235,1.5],[0.0,15.0, 30.0, 45.0, 60.0,75.0, 90.0])) #tension1 / 0.0173
                            

                    elif line.startswith("A0:") :
                        parts = line.split(": ")
                        if len(parts) == 2 and parts[1].isdigit():
                            valor_digital2 = int(parts[1])
                            tension2 = (valor_digital2 / 1023) * 3.346
                            
                            angulos['ID'] = float(interp(tension2, [0,0.068,0.356,0.68,1.09,1.33,1.61],[0.0,15.0, 30.0, 45.0, 60.0,75.0, 90.0]))#tension2 / 0.0178
                            

                    elif line.startswith("A6:") :
                        parts = line.split(": ")
                        if len(parts) == 2 and parts[1].isdigit():
                            valor_digital3 = int(parts[1])
                            tension3 = (valor_digital3 / 1023) * 3.346
                            
                            angulos['MD'] = float(interp(tension3, [0.16,0.464,0.775,1.05,1.38,1.61],[0.0, 30.0, 45.0, 60.0,75.0, 90.0]))#tension3 / 0.0153
                            

                    elif line.startswith("A9:"):
                        parts = line.split(": ")
                        if len(parts) == 2 and parts[1].isdigit():
                            valor_digital4 = int(parts[1])
                            tension4 = (valor_digital4 / 1023) * 3.346
                            
                            angulos['MI'] = float(interp(tension4, [0.055,0.28,0.647,0.97,1.242,1.547],[0.0, 30.0, 45.0, 60.0,75.0, 90.0]))#tension4 / 0.0194   Corregido para usar tension4
                            

                    elif line.startswith("A8:") :
                        parts = line.split(": ")
                        if len(parts) == 2 and parts[1].isdigit():
                            valor_digital5 = int(parts[1])
                            tension5 = (valor_digital5 / 1023) * 3.346
                            
                            angulos['II'] = float(interp(tension5, [0.16,0.37,0.575,0.85,1.08,1.35,1.5],[0.0,15.0, 30.0, 45.0, 60.0,75.0, 90.0]))#tension5 / 0.0184
                            

                    elif line.startswith("A7:"):
                        parts = line.split(": ")
                        if len(parts) == 2 and parts[1].isdigit():
                            valor_digital6 = int(parts[1])
                            tension6 = (valor_digital6 / 1023) * 3.346
                            
                            angulos['PI'] = float(interp(tension6, [0.137,0.4,0.768,1.134,1.46,1.74],[0.0, 30.0, 45.0, 60.0,75.0, 90.0]))#tension6 / 0.0173
                            
                            
                    elif line.startswith("A10:"):
                        parts = line.split(": ")
                        if len(parts) == 2 and parts[1].isdigit():
                            valor_digital7 = int(parts[1])
                            tension7 = (valor_digital7 / 1023) * 3.346
                            #angulo10 = (tension7 -1.379)/ 0.005
                            #array10.append(tension7)
                            #mv10 = np.convolve(array10, np.ones(len(array10)), 'valid')/ len(array10)
                            angulos['Flex1']= float(interp(tension7, [1.4,1.759],[0.0, 90.0]))
                            

                    elif line.startswith("A11:"):
                        parts = line.split(": ")
                        if len(parts) == 2 and parts[1].isdigit():
                            valor_digital8 = int(parts[1])
                            tension8 = (valor_digital8 / 1023) * 3.346
                            #angulo11 = (tension8-1.6148) / 0.0015
                            #array11.append(tension8)
                            #mv11 = np.convolve(array11, np.ones(len(array11)), 'valid')/ len(array11)
                            angulos['Flex2']= float(interp(tension8, [1.587,1.729],[0.0, 90.0]))
                            

                    elif line.startswith("A12:") :
                        parts = line.split(": ")
                        if len(parts) == 2 and parts[1].isdigit():
                            valor_digital9 = int(parts[1])
                            tension9 = (valor_digital9 / 1023) * 3.346
                            print(tension9)
                            angulos['Flex3']= float(interp(tension9, [1.08,1.15,1.39, 1.44, 1.50, 1.534],[-30.0,0.0,15.0, 30.0, 60.0, 90.0]))
                            #[1.44,1.496, 1.592, 1.6304, 1.65,1.666, 1.687]

                    elif line.startswith("A13:") :
                        parts = line.split(": ")
                        if len(parts) == 2 and parts[1].isdigit():
                            valor_digital10 = int(parts[1])
                            tension10 = (valor_digital10 / 1023) * 3.346
                            print(tension10)
                            angulos['Flex4']= float(interp(tension10, [1.06, 1.19,1.38, 1.44, 1.50, 1.53],[-30.0,0.0,15.0, 30.0,60.0, 90.0]))
                    
                except ValueError as e:
                        print(f"Error de valor en la línea '{line}': {e}")
    finally:
        # Cierra la conexión serial
        ser.close()

    if mano == 'izquierda':
        return {
            'MI': angulos['MI'],
            'II': angulos['II'],
            'PI': angulos['PI'],
            'Flex3': angulos['Flex3'],
            'Flex4': angulos['Flex4']
            }
            
    elif mano == 'derecha':
        return {
            'PD': angulos['PD'],
            'ID': angulos['ID'],
            'MD': angulos['MD'],
            'Flex3': angulos['Flex3'],
            'Flex4': angulos['Flex4']
            }

    else:
        return angulos  # Por defecto, devuelve todos los ángulos
