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



## Descripción detallada del sistema

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




<img width="863" height="601" alt="Captura de pantalla 2026-05-22 162619" src="https://github.com/user-attachments/assets/134be0c0-5ab8-4f48-80eb-9fe4040b737d" /><br>
# Modelo Matemático del Sistema

$$
V_e(t) = R\, i_1(t) + L \frac{di_1(t)}{dt}+ \frac{1}{C} \int \left[i_1(t) - i_2(t)\right] dt
$$

$$
\frac{1}{C} \int \left[i_1(t) - i_2(t)\right] dt = R_p\, i_2(t)
$$

$$
V_s(t) = R_p\, i_2(t)
$$

---

# Modelo de Ecuaciones Íntegro-Diferenciales

$$
R i_1(t) =V_e(t) - L \frac{di_1(t)}{dt} - R_p i_2(t)
$$

$$
i_1(t) =\frac{1}{R}\left[V_e(t) - L \frac{di_1(t)}{dt} - R_p i_2(t)\right]
$$

$$
i_2(t) =\frac{1}{R_p}\left[\frac{1}{C}\int \left(i_1(t) - i_2(t)\right) dt\right]
$$

$$
V_s(t) = R_p i_2(t)
$$

---

# Función de Transferencia

$$
\boxed{\frac{V_s(s)}{V_e(s)} =\frac{R_p}{L C R_p s^2 + (L + R R_p C)s + (R + R_p)}}
$$

---



## Lista de archivos incluidos en el repositorio

1\. Cuaderno computacional de MATLAB \[.mlx].
2. Modelo de Simulink \[.slx].
3. Archivos de Spyder \[.py].
4. Imagen con los parámetros del controlador.
5. Imágenes de las simulaciones \[.pdf].
6. Evidencia del análisis matemático: función de transferencia, modelo de ecuaciones integro-diferenciales, error en estado estacionario y estabilidad en lazo abierto.

7\. Modelo fisiológico en Biorender o BioArt.

## Referencias

\[1] P. A. Valle, Syllabus para Modelado de Sistemas Fisiológicos, Tecnológico Nacional de México / Instituto Tecnológico de Tijuana, Tijuana, B.C., México, 2025. Permalink: https://biomath.xyz/course/

\[2] M. C. Khoo, Physiological Control Systems Analysis Simulation, and Estimation, 2nd ed. Piscataway, New Jersey, USA: IEEE Press, 2018, Section 4, Page 93.

\[3] N. S. Nise, Control Systems Engineering, 8th ed. Hoboken, New Jersey, USA: John Wiley \& Sons, 2020.

\[4] T. Kind, T. J. Faes, J. W. Lankhaar, A. Vonk-Noordegraaf \& M. Verhaegen, "Estimation of three-and four-element Windkessel parameters using subspace model identification", IEEE Transactions on Biomedical Engineering, vol. 57, issue 7, pp. 1531-1538, Jul 2010. https://doi.org/10.1109/TBME.2010.2041351

