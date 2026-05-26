[![Open in MATLAB Online](https://www.mathworks.com/images/responsive/global/open-in-matlab-online.svg)](https://matlab.mathworks.com/open/github/v1?repo=l20211965-creator/MSFPractica2)


# Proyecto Final : “Representación del Asma mediante un Circuito Eléctrico RLC” 

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/6682b132-ff02-4c44-ac13-fd3540e2df28" />



## Información de la estudiante

Pamela Escobedo Sandoval - l20211965@tectijuana.edu.mx

Alan Omar Garcia Toledo - Alan.garciat201@tectijuana.edu.mx

Modelado de Sistemas Fisiológicos

Ingeniería Biomédica

## Docente

Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx

Departamento de Ingeniería Eléctrica y Electrónica, Tecnológico Nacional de México/IT Tijuana, Blvd. Alberto Limón Padilla s/n, Tijuana, C.P. 22454, B.C., México.


## Descripción de la asignatura

El modelizado de sistemas fisiológicos es una herramienta importante en Ingeniería Biomédica, permite comprender el funcionamiento del cuerpo humano, así como diseñar y evaluar terapias y dispositivos médicos; se define como el proceso de formular modelos matemáticos o computacionales que representan el comportamiento y la interacción de los sistemas biológicos y fisiológicos. Esta asignatura pretende aportar al perfil del Ingeniero Biomédico la capacidad de realizar investigación científica en el área de Biología de Sistemas con la finalidad de dirigir y participar en equipos de trabajo interdisciplinarios en contextos nacionales e internacionales, así como de proporcionar soluciones informáticas para resolver problemas en el campo de la Ingeniería Biomédica con ética profesional; lo anterior al proporcionar al estudiante bases sólidas para modelizar sistemas y diseñar controladores para la solución de problemas en las áreas de atención médica y del sector industrial médico. La construcción de analogías entre circuitos eléctricos y sistemas fisiológicos para la formulación de modelos matemáticos y el diseño de controladores mediante la experimentación in silico brindan herramientas de gran aplicación en el quehacer profesional del Ingeniero Biomédico.

La asignatura de Modelado de Sistemas Fisiológicos forma parte del plan de estudios de la carrera en Ingeniería Biomédica con la siguiente competencia general del curso: Utiliza las propiedades de los circuitos RLC para describir la dinámica de sistemas fisiológicos, obtener modelos matemáticos y aplicar el control clásico, esto con el objetivo de integrar los principios de la Ingeniería de Control, la Electrónica Analógica y las Ciencias de la Computación con la Anatomía y Fisiología del cuerpo humano para proporcionar descripciones cuantitativas y cualitativas de sistemas fisiológicos complejos con el objetivo de modelizar, analizar, controlar, ilustrar y predecir su dinámica tanto en el corto como en el largo plazo.

## Objetivos


1. Modelar la presión respiratoria de inspiración mediante una fuente de voltaje Ve(t) que represente el estímulo respiratorio de entrada.
2. Representar la resistencia al flujo de aire en las vías respiratorias principales utilizando una resistencia eléctrica R.
3. Analizar el efecto de la inercia del aire en movimiento mediante una inductancia L dentro del modelo respiratorio.
4. Simular el almacenamiento temporal de aire en los pulmones mediante un capacitor C, asociado al compliance pulmonar.
5. Modelar la resistencia periférica de las vías respiratorias pequeñas mediante la resistencia Rp, evaluando su influencia en enfermedades obstructivas como asma o EPOC.
6. Estudiar el comportamiento de los flujos respiratorios de entrada Ie(t) y salida Is(t) dentro del sistema dinámico.
7. Obtener las ecuaciones diferenciales que describen el comportamiento dinámico del sistema respiratorio equivalente.

# Sistema Respiratorio: Modelo RLC

Este proyecto modela el sistema respiratorio mediante una analogía con un circuito RLC, enfocándose en la dinámica del flujo de aire y la mecánica pulmonar ante una patología obstructiva. El sistema respiratorio está formado por las vías aéreas superiores e inferiores, los alvéolos, la vasculatura pulmonar y los músculos respiratorios que generan los gradientes de presión necesarios para la ventilación.

El pulmón participa en el intercambio gaseoso y regula el paso del aire a través de la resistencia de los conductos y la elasticidad del tejido pulmonar. En condiciones normales (caso control), el sistema opera con una resistencia mínima y una alta adaptabilidad. Sin embargo, en una condición patológica como el asma, las vías respiratorias sufren bronconstricción, inflamación crónica y atrapamiento de aire, alterando drásticamente la resistencia central y periférica, la inercia del flujo y la compliancia elástica del órgano.

### Tabla 1. Parámetros del modelo RLC respiratorio y su Interpretación Fisiológica

| Parámetro | Caso Control (Pulmón Sano) | Caso Asma (Enfermedad) | Interpretación Fisiológica y Justificación del Cambio |
| :--- | :---: | :---: | :--- |
| **R** (Resistencia central) | 2 $\Omega$ | 8 $\Omega$ | **Aumenta significativamente** debido a la bronconstricción aguda en las vías aéreas principales de conducción. La contracción del músculo liso bronquial reduce el diámetro del conducto, oponiéndose severamente al flujo de aire inicial. |
| <span style="color:#d9381e">**Rp** (Resistencia periférica)</span> | <span style="color:#d9381e">1 $\Omega$</span> | <span style="color:#d9381e">12 $\Omega$</span> | **Aumenta de forma crítica** porque el proceso inflamatorio crónico, el edema de la mucosa y la hipersecreción de moco espeso obstruyen casi por completo la luz de los bronquiolos terminales y periféricos. |
| **L** (Inercia del aire) | 0.5 H | 0.7 H | **Aumenta ligeramente** debido a que la reducción del calibre de las vías aéreas vuelve el flujo altamente turbulento. Al aumentar la resistencia, la masa de aire requiere una mayor diferencia de presión para acelerarse y mantener el flujo en movimiento. |
| **C** (Compliance / Compliancia) | 0.08 F | 0.03 F | **Disminuye drásticamente** debido al atrapamiento de aire (hiperinsuflación). Los alvéolos pierden su capacidad de distenderse de manera eficiente, volviendo al tejido pulmonar mecánicamente más rígido y difícil de expandir durante la inspiración. |
| **Ve** (Voltaje de entrada) | 5 V | 5 V | **Se mantiene constante** como variable de control para simular que el esfuerzo muscular del paciente o el gradiente de presión externa aplicado por la caja torácica es idéntico en ambos escenarios, permitiendo evaluar el impacto real de la patología. |

> **Nota de Simulación:** La presión de entrada ($V_e$) se fija igual en ambos casos para aislar y comparar de forma justa cómo la obstrucción y rigidez del asma alteran el volumen, el flujo y el comportamiento dinámico del sistema pulmonar.


## Descripción detallada del sistema respiratorio

El sistema respiratorio permite el intercambio de gases mediante el movimiento de aire a
través de las vías respiratorias y los pulmones. Esta dinámica puede representarse de
forma simplificada mediante un circuito eléctrico de segundo orden, modelando los procesos
de flujo de aire, resistencia pulmonar y elasticidad respiratoria bajo las siguientes
suposiciones:
1. La presión respiratoria generada durante la inspiración se modela mediante una fuente de
voltaje de entrada Ve(t), que representa el estímulo inicial del sistema respiratorio
encargado de impulsar el flujo de aire hacia los pulmones.
2. El flujo de aire a través de las vías respiratorias principales se modela mediante una
resistencia R, asociada a la oposición al paso del aire en estructuras como la tráquea y los
bronquios principales.
3. La inercia del aire en movimiento se representa mediante una inductancia L, la cual
modela la dificultad que presenta el sistema respiratorio para modificar rápidamente la
velocidad del flujo de aire debido a la masa del aire y la dinámica pulmonar.
4. El almacenamiento temporal de aire dentro de los pulmones se representa mediante un
capacitor C, asociado al cumplimiento pulmonar (compliance), es decir, a la capacidad
elástica del pulmón para expandirse y almacenar aire durante la inspiración.
5. La resistencia de las vías respiratorias periféricas se modela mediante una segunda
resistencia Rp, la cual representa la oposición al flujo de aire en bronquiolos y vías
respiratorias pequeñas, siendo el principal sitio de obstrucción en enfermedades
respiratorias como el asma o la EPOC.
6. Se identifican los siguientes dos flujos en el sistema: el flujo de entrada de aire Ie(t), que
circula desde la fuente de entrada hacia el sistema respiratorio, y el flujo de salida o
distribución Is(t), asociado a la respuesta respiratoria efectiva en los pulmones.

<img width="1024" height="713" alt="image" src="https://github.com/user-attachments/assets/def9c633-42f5-4633-bea5-7d1e957435aa" />


## Modelo matemático del sistema

Se calculó de forma analítica la función de transferencia, el error en estado estacionario y el modelo de ecuaciones íntegro-diferenciales. Además, se consideran la estabilidad en lazo abierto para el caso control y el caso patológico (Asma).

### Ecuaciones principales del sistema

Las ecuaciones íntegro-diferenciales que describen el comportamiento del circuito RLC análogo al sistema respiratorio son:



### Ecuación principal

$$V_e(t) = R \, i_1(t) + L \frac{di_1(t)}{dt} + \frac{1}{\,C} \int (i_1(t) - i_2(t)) \, dt$$

$$\frac{1}{\,C} \int (i_1(t) - i_2(t)) \, dt = R_p \, i_2(t)$$

$$V_S = R_p \, i_2(t)$$
## Modelo de Ecuaciones íntegro-diferenciales

A partir del análisis del circuito RLC, las corrientes de malla y la salida se pueden expresar de la siguiente manera:

$$i_1(t) = \frac{1}{R} \left[ V_e(t) - L \frac{di_1(t)}{dt} - R_p \, i_2(t) \right]$$

$$i_2(t) = \frac{1}{R_p} \left[ \frac{1}{C} \int (i_1(t) - i_2(t)) \, dt \right]$$

$$V_S(t) = R_p \, i_2(t)$$

Donde $i_1(t)$ representa el flujo de aire o corriente de la malla izquierda asociada a las vías aéreas centrales y la inercia del gas, mientras que $i_2(t)$ representa la corriente de la malla derecha relacionada con la dinámica de la resistencia periférica y la distensibilidad pulmonar (compliancia) en los alvéolos.

### Función de transferencia

Sustituyendo estas relaciones en el modelo del circuito y aplicando la transformada de Laplace con condiciones iniciales cero, se obtiene la función de transferencia del sistema respiratorio:

$$G(s) = \frac{V_S(s)}{V_e(s)} = \frac{R_p}{L \cdot C \cdot R_p \cdot s^2 + (L + R \cdot R_p \cdot C) \cdot s + (R + R_p)}$$

## Error en estado estacionario

El error en estado estacionario se define como la diferencia entre la entrada y la salida de un sistema cuando el límite en el tiempo tiende a infinito. Este análisis solo es útil para sistemas estables, por lo que primero se debe determinar la estabilidad del sistema. Para sistemas en lazo abierto ante una entrada escalón unitario $V_e(s) = \frac{1}{s}$, el error en estado estacionario está dado por:

$$e(s) = \lim_{s \to 0} s \cdot V_e(s) \left[ 1 - G(s) \right]$$

### Error en estado estacionario para el sistema de control

#### Valores del sistema de control (Caso Control - Pulmón Sano)

| Condición | R | $R_p$ | L | C |
| :--- | :---: | :---: | :---: | :---: |
| **Control: Pulmón sano** | $2\ \Omega$ | $1\ \Omega$ | $0.5\ \text{H}$ | $0.08\ \text{F}$ |

Sustituyendo los valores en la función de transferencia:

$$G(s) = \frac{1}{(0.5)(0.08)(1)s^2 + \left(0.5 + (2)(1)(0.08)\right)s + (2 + 1)}$$

$$G(s) = \frac{1}{0.04s^2 + 0.66s + 3}$$

Desarrollando analíticamente el límite para el error:

$$e(s) = \lim_{s \to 0} s \left(\frac{1}{s}\right) \left[ 1 - \frac{R_p}{LCR_p s^2 + (L + RR_pC)s + (R + R_p)} \right]$$

$$e(s) = 1 - \frac{R_p}{R + R_p} = \frac{R}{R + R_p} = \frac{2}{2 + 1} = \frac{2}{3} \approx 0.667$$

Por lo tanto, el error en estado estacionario para el sistema de control es de **0.667**, lo que significa que la salida se estabiliza en un valor que es $\frac{1}{3}$ menor que la entrada.

### Error en estado estacionario para el sistema patológico

#### Valores del sistema patológico (Caso Asma - Enfermedad)

| Condición | R | $R_p$ | L | C |
| :--- | :---: | :---: | :---: | :---: |
| **Caso: Asma (Enfermedad)** | $8\ \Omega$ | $12\ \Omega$ | $0.7\ \text{H}$ | $0.03\ \text{F}$ |

Sustituyendo los valores en la función de transferencia:

$$G(s) = \frac{12}{(0.7)(0.03)(12)s^2 + \left(0.7 + (8)(12)(0.03)\right)s + (8 + 12)}$$

$$G(s) = \frac{12}{0.252s^2 + 3.58s + 20}$$

Desarrollando analíticamente el límite para el error en el caso patológico:

$$e(s) = \lim_{s \to 0} s \left(\frac{1}{s}\right) \left[ 1 - \frac{R_p}{LCR_p s^2 + (L + RR_pC)s + (R + R_p)} \right]$$

$$e(s) = 1 - \frac{R_p}{R + R_p} = \frac{R}{R + R_p} = \frac{8}{8 + 12} = \frac{8}{20} = \frac{2}{5} = 0.4$$

Por lo tanto, el error en estado estacionario para el sistema patológico es de **0.400**, lo que significa que la salida se ve afectada por la obstrucción pulmonar y se estabiliza en un valor menor que la entrada en menor proporción comparado con el caso control debido al drástico incremento de la resistencia periférica ($R_p$).

## Estabilidad del sistema en lazo abierto

Para analizar la estabilidad en lazo abierto se utiliza el denominador de la función de transferencia del sistema respiratorio:

$$G(s) = \frac{R_p}{LCR_p s^2 + (L + RR_pC)s + (R + R_p)}$$

Para determinar la estabilidad se calculan las raíces del denominador usando la fórmula general:

$$\lambda_{1,2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

Dónde los coeficientes dependen de los parámetros físicos del circuito:

$$a = LCR_p$$

$$b = L + RR_pC$$

$$c = R + R_p$$

---

### Estabilidad para el Control (Pulmón Sano)

Utilizando los valores del control ($R = 2\ \Omega$, $R_p = 1\ \Omega$, $L = 0.5\ \text{H}$, $C = 0.08\ \text{F}$), los coeficientes son:

$$a = (0.5)(0.08)(1) = 0.04$$

$$b = 0.5 + (2)(1)(0.08) = 0.66$$

$$c = 2 + 1 = 3$$

Sustituyendo en la ecuación cuadrática:

$$\lambda_{1,2} = \frac{-0.66 \pm \sqrt{(0.66)^2 - 4(0.04)(3)}}{2(0.04)}$$

$$\lambda_{1,2} = \frac{-0.66 \pm \sqrt{0.4356 - 0.48}}{0.08} = \frac{-0.66 \pm \sqrt{-0.0444}}{0.08}$$

Calculando las raíces complejas conjugadas:

$$\lambda_1 = -8.25 + 2.63j$$

$$\lambda_2 = -8.25 - 2.63j$$

Por lo tanto, el sistema es **estable** dado que la parte real de ambas raíces es negativa ($\text{Re}(\lambda) = -8.25$). Al tener componentes imaginarias, el sistema presenta un comportamiento **subamortiguado**.

### Estabilidad para el caso Patológico (Asma)

Utilizando los valores del caso patológico debido a la enfermedad ($R = 8\ \Omega$, $R_p = 12\ \Omega$, $L = 0.7\ \text{H}$, $C = 0.03\ \text{F}$), evaluamos los nuevos coeficientes del denominador:

$$a = LCR_p = (0.7)(0.03)(12) = 0.252$$

$$b = L + RR_pC = 0.7 + (8)(12)(0.03) = 0.7 + 2.88 = 3.58$$

$$c = R + R_p = 8 + 12 = 20$$

Sustituyendo estos coeficientes en la ecuación cuadrática general para obtener los polos del sistema ($\lambda_{1,2}$):

$$\lambda_{1,2} = \frac{-3.58 \pm \sqrt{(3.58)^2 - 4(0.252)(20)}}{2(0.252)}$$

$$\lambda_{1,2} = \frac{-3.58 \pm \sqrt{12.8164 - 20.16}}{0.504}$$

$$\lambda_{1,2} = \frac{-3.58 \pm \sqrt{-7.3436}}{0.504}$$

Calculando las raíces complejas conjugadas resultantes:

$$\lambda_1 = -7.10 + 5.38j$$

$$\lambda_2 = -7.10 - 5.38j$$

Por lo tanto, el sistema patológico sigue siendo **estable** ya que la parte real de ambas raíces se mantiene en el semiplano izquierdo de Laplace ($\text{Re}(\lambda) = -7.10$). Debido a la presencia de la componente imaginaria provocada por los severos cambios de resistencia y compliancia del asma, el sistema mantiene un comportamiento **subamortiguado**, pero con una frecuencia de oscilación mayor y una respuesta transitoria modificada en comparación con el caso control.


## Lista de archivos incluidos en el repositorio



1.Cuaderno computacional de MATLAB [.mlx].

2.Modelo de Simulink [.slx].

3.Archivos de Spyder [.py].

4.Imagen con los parámetros del controlador.

5.Imágenes de las simulaciones [.pdf].

6.Evidencia del análisis matemático: función de transferencia, modelo de ecuaciones integro-diferenciales, error en estado estacionario y estabilidad en lazo abierto.

7.Modelo fisiológico en Biorender o BioArt.

8.Ensayo gráfico.


## Referencias

\[1] P. A. Valle, Syllabus para Modelado de Sistemas Fisiológicos, Tecnológico Nacional de México / Instituto Tecnológico de Tijuana, Tijuana, B.C., México, 2025. Permalink: https://biomath.xyz/course/

\[2] M. C. Khoo, Physiological Control Systems Analysis Simulation, and Estimation, 2nd ed. Piscataway, New Jersey, USA: IEEE Press, 2018, Section 4, Page 93.

\[3] N. S. Nise, Control Systems Engineering, 8th ed. Hoboken, New Jersey, USA: John Wiley \& Sons, 2020.

\[4] T. Kind, T. J. Faes, J. W. Lankhaar, A. Vonk-Noordegraaf \& M. Verhaegen, "Estimation of three-and four-element Windkessel parameters using subspace model identification", IEEE Transactions on Biomedical Engineering, vol. 57, issue 7, pp. 1531-1538, Jul 2010. https://doi.org/10.1109/TBME.2010.2041351

