# -*- coding: utf-8 -*-
"""
Proyecto Final: Representación del Asma mediante un Circuito Eléctrico RLC

Departamento de Ingeniería Eléctrica y Electrónica, Ingeniería Biomédica
Tecnológico Nacional de México [TecNM - Tijuana]
Blvd. Alberto Limón Padilla s/n, C.P. 22454, Tijuana, B.C., México

Nombre del alumno: Alan Omar Garcia Toledo
Número de control: 20210787
Correo institucional: alan.garciat201@tectijuana.edu.mx

Nombre del alumno: Pamela Escobedo Sandoval
Número de control: 20211965
Correo institucional: pamela.escobedos201@tectijuana.edu.mx

Asignatura: Modelado de Sistemas Fisiológicos
Docente: Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx
"""

# Librerías
import control as ctrl
import numpy as np
import matplotlib.pyplot as plt

# ----------------------
# Configuración de tiempo (0 a 10 segundos)
# ----------------------
t0, tend, dt = 0, 10, 1e-3
N = round((tend - t0) / dt) + 1
t = np.linspace(t0, tend, N)

# Entrada escalón unitario en t = 0.5 s
u = np.zeros_like(t)
u[t >= 0] = 1.3

# ===== FUNCIÓN DE TRANSFERENCIA =====
# Deducida: Vs/Ve = Rp / (L*C*Rp * s^2 + (L + R*Rp*C) * s + (R + Rp))
def sistema_respiratorio(R, Rp, L, C):
    num = [Rp]
    den = [(L*C*Rp), (L + R*Rp*C), (R + Rp)]
    return ctrl.tf(num, den)

# ----------------------
# PARÁMETROS EXACTOS 
# ----------------------
# Sistema Sano / Control -> Valor final = 0.6
R_s, Rp_s, L_s, C_s = 2, 1, 0.5, 0.08
sys_control = sistema_respiratorio(R_s, Rp_s, L_s, C_s)

# Sistema Alterado / Asma -> Valor final = 0.33
R_c, Rp_c, L_c, C_c = 8, 12, 0.7, 0.03
sys_caso = sistema_respiratorio(R_c, Rp_c, L_c, C_c)

# Respuestas en lazo abierto
_, Vs_control = ctrl.forced_response(sys_control, t, u)
_, Vs_caso = ctrl.forced_response(sys_caso, t, u)

# ----------------------
# Controlador PID 
# ----------------------
def controlador(kP, kI, kD, sys):
    Cr = 1e-6
    Re = 1 / (kI * Cr)
    Rr = kP * Re
    Ce = kD / Rr
    
 
    print(f"Cr: {Cr} F")
    print(f"Ce: {Ce:.6e} F")
    print(f"Re: {Re:.2f} Ohm")
    print(f"Rr: {Rr:.2f} Ohm\n")
    
    numPID = [Re * Rr * Ce * Cr, (Re * Ce + Rr * Cr), 1]
    denPID = [Re * Cr, 0]
    PID = ctrl.tf(numPID, denPID)
    return ctrl.feedback(ctrl.series(PID, sys), 1)

# ESTAS SON LAS GANANCIAS NUEVAS Y AJUSTADAS 
casoPID = controlador(200.0, 50.0, 1.2, sys_caso)

# casoPID = controlador(1432.29305325518, 373031.6074, 0.32274 sys_caso)
# Respuesta con control (AHORA SÍ QUEDA EN MEDIO)
_, PID_res = ctrl.forced_response(casoPID, t, Vs_control)


# -------- GRÁFICA FINAL PERFECTA --------
plt.figure(figsize=(10, 5))

# Colores y líneas FINAS como en tu ejemplo
plt.plot(t, Vs_control, linewidth=1.5, color=[0, 153/255, 136/255], label='V(t): Control')
plt.plot(t, Vs_caso, linewidth=1.5, color=[204/255, 102/255, 0], linestyle='--', label='V(t): Caso')
plt.plot(t, PID_res, linewidth=1.5, color=[170/255, 51/255, 106/255], linestyle=':', label='PID(t)')

# Etiquetas
plt.title('Caso vs Control', fontsize=13)
plt.xlabel('Tiempo [s]', fontsize=11)
plt.ylabel('Voltaje [V]', fontsize=11)

# Ejes ajustados para ver los valores correctos
plt.xlim(0, 10)
plt.ylim(0, 1)

plt.legend(loc='best', fontsize=10, frameon=False)
plt.grid(False)

plt.tight_layout()

plt.show()