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
| **L** (Inercia del aire) | $0.5$ H | $0.7$ H | **Aumenta ligeramente** debido a que la reducción del calibre de las vías aéreas vuelve el flujo altamente turbulento. Al aumentar la resistencia, la masa de aire requiere una mayor diferencia de presión para acelerarse y mantener el flujo en movimiento. |
| **C** (Compliance / Compliancia) | $0.08$ F | $0.03$ F | **Disminuye drásticamente** debido al atrapamiento de aire (hiperinsuflación). Los alvéolos pierden su capacidad de distenderse de manera eficiente, volviendo al tejido pulmonar mecánicamente más rígido y difícil de expandir durante la inspiración. |
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

# Ecuaciones Principales del Sistema

$$
V_e(t) = R\ i_1(t) + L \frac{di_1(t)}{dt}+ \frac{1}{C} \int \left[i_1(t) - i_2(t)\right] dt
$$

$$
\frac{1}{C} \int \left[i_1(t) - i_2(t)\right] dt = R_p\ i_2(t)
$$

$$
V_s(t) = R_p\ i_2(t)
$$

---



# Transformada de Laplace

$$
V_e(s)=RI_1(s)+LsI_1(s)+\frac{I_1(s)-I_2(s)}{Cs}
$$

$$
\frac{I_1(s)-I_2(s)}{Cs}=R_pI_2(s)
$$
$$
V_s(t) = R_p\ i_2(t)
$$

---

# Desarrollo Algebraico

## Factorizando el término de salida \(Vs(s)\)

$$
V_e(s)=V_s(s)\left[\frac{(1+R_pCs)(Ls+R)}{R_p}+1\right]
$$

## Realizando el producto de binomios

$$
(1+R_pCs)(Ls+R)=Ls+R+R_pCLs^2+RR_pCs
$$

## Sustituyendo y agrupando términos semejantes

$$
V_e(s)=V_s(s)\left[\frac{R_pCLs^2+(L+RR_pC)s+R}{R_p}+1\right]
$$

$$
V_e(s)=V_s(s)\left[\frac{R_pCLs^2+(L+RR_pC)s+R+R_p}{R_p}\right]
$$

---

# Función de Transferencia

$$
\frac{V_s(s)}{V_e(s)}=
\frac{R_p}
{LCR_ps^2+(L+RR_pC)s+(R+R_p)}
$$

---


# Ecuaciones Integro-Diferenciales

$$
i_1(t)=\frac{1}{R}\left[V_e(t)-L\frac{di_1(t)}{dt}-R_p\,i_2(t)\right]
$$

$$
i_2(t)=\frac{1}{R_p}\left[\frac{1}{C}\int\left(i_1(t)-i_2(t)\right)dt\right]
$$

$$
V_s(t) = R_p\ i_2(t)
$$

---



# Coeficientes del Denominador

La ecuación característica del sistema es:

$$
(LCR_p)s^2 + (L + RR_pC)s + (R + R_p) = 0
$$

$$
a=LCR_p
$$

$$
b=L+RR_pC
$$

$$
c=R+R_p
$$


# Fórmula general

$$
\lambda_{1,2} =
\frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$

---
<div align="center">

| Parámetro | Caso Control | Caso Experimental |
|---|---|---|
| Raíces del sistema | $$\lambda_1 = -7.0437 + 5.4546j$$  $$\lambda_2 = -7.0437 - 5.4546j$$ | $$\lambda_1 = -8.25 + 2.63j$$  $$\lambda_2 = -8.25 - 2.63j$$ |
| Tipo de raíces | complejas conjugadas | complejas conjugadas|
| Estabilidad | Sistema estable | Sistema estable |
| Comportamiento | Subamortiguado | Subamortiguado |
| Error estacionario | $$e_{ss}=0.6$$ | $$e_{ss}=0.333$$ |
</div>
---

# Error en Estado Estacionario

$$
e_{ss}=\lim_{s\to0}sE(s)
$$
<div align="center">


  
| Caso Control | Caso (Asma) |
|---|---|
| $$e_{ss}=\frac{R_c}{R_c+R_p}$$ | $$e_{ss}=\frac{R_c}{R_c+R_p}$$ |
| $$e_{ss}=\frac{1}{1.5}$$ | $$e_{ss}=\frac{8.5}{16}$$ |
| $$e_{ss}=0.6667$$ | $$e_{ss}=0.33$$ |
  
</div>
# Analisis de estabilidad

## Conclusión

En ambos casos el sistema es **estable**, ya que las raíces obtenidas son reales y negativas.  
Además, el comportamiento del sistema es **subamortiguado**.  

El caso experimental presenta un menor error en estado estacionario:

$$
e_{ss}=0.333
$$

lo que indica una mejor respuesta respecto al caso control.

se concluye que la respuesta del sistema tiende al equilibrio conforme transcurre el tiempo, evitando oscilaciones crecientes o inestabilidad.

El sistema presenta raíces reales negativas repetidas, lo cual indica un comportamiento sobreamortiguado y estable, representando adecuadamente la dinámica respiratoria del modelo propuesto.



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

