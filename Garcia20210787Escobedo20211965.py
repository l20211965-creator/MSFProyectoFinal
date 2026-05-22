# -*- coding: utf-8 -*-
"""
Práctica 4: Sistema endocrino

Departamento de Ingeniería Eléctrica y Electrónica, Ingeniería Biomédica
Tecnológico Nacional de México [TecNM - Tijuana]
Blvd. Alberto Limón Padilla s/n, C.P. 22454, Tijuana, B.C., México


Nombre del alumno: Alan Omar Garcia Toledo
Número de control: 20210787
Correo institucional: alan.garciat201@tectijuana.edu.mx


Asignatura: Modelado de Sistemas Fisiológicos
Docente: Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx
"""
# Librerías
import control as ctrl
import numpy as np
import matplotlib.pyplot as plt

# Configuración de tiempo
t0, tend, dt = 0, 15, 1e-3
N = round((tend - t0) / dt) + 1
t = np.linspace(t0, tend, N)

# Entrada escalón unitario en t = 1 s
u = np.zeros_like(t)
u[t >= 1] = 1.0

# Función de transferencia del sistema endocrino
def endocrino_tf(R1, R2, L, C):
    num = [L, R2]
    den = [C * L * R1, (C * R1 * R2) + L, R1 + R2]
    return ctrl.tf(num, den)

# Sistema Control (Basal)
R1_s, R2_s, L_s, C_s = 1e3, 100e3, 100e-3, 1e-6
sys_control = endocrino_tf(R1_s, R2_s, L_s, C_s)

# Sistema Caso Alterado
R1_c, R2_c, L_c, C_c = 1e3, 1e3, 100e-3, 1000e-6
sys_caso = endocrino_tf(R1_c, R2_c, L_c, C_c)

# Respuestas en lazo abierto
_, Vs_control = ctrl.forced_response(sys_control, t, u)
_, Vs_caso = ctrl.forced_response(sys_caso, t, u)

# Controlador PID
def controlador(kP, kI, kD, sys):
    Cr = 1e-6
    Re = 1 / (kI * Cr)
    Rr = kP * Re
    Ce = kD / Rr
    
    print(f"El valor de capacitancia Cr es de {Cr} Faradios.\n")
    print(f"El valor de capacitancia Ce es de {Ce} Faradios.\n")
    print(f"El valor de resistencia de Re es de {Re} Ohms.\n")
    print(f"El valor de resistencia de Rr es de {Rr} Ohms.\n")
    
    
    numPID = [Re * Rr * Ce * Cr, (Re * Ce + Rr * Cr), 1]
    denPID = [Re * Cr, 0]
    PID = ctrl.tf(numPID, denPID)
    return ctrl.feedback(ctrl.series(PID, sys), 1)

# PID aplicado al caso alterado
casoPID = controlador(1432.29305325518, 373031.6074, 0.32274, sys_caso)

# Respuesta con PID
_, PID_res = ctrl.forced_response(casoPID, t, Vs_control)



# -------- GRÁFICA ÚNICA --------
plt.figure(figsize=(10, 5))

plt.plot(t, Vs_control, linewidth=2, label='Control (Basal)')
plt.plot(t, Vs_caso, linewidth=2, linestyle='--', label='Caso Alterado')
plt.plot(t, PID_res, linewidth=2, linestyle=':', label='Caso con PID')

plt.title('Regulación Hormonal: Comparación en una sola gráfica')
plt.xlabel('Tiempo [s]')
plt.ylabel('Voltaje [V]')
plt.xlim(0, 15)
plt.ylim(-0.2, 1.4)
plt.legend()
plt.grid(False)

plt.tight_layout()
plt.show()