[![Open in MATLAB Online](https://www.mathworks.com/images/responsive/global/open-in-matlab-online.svg)](https://matlab.mathworks.com/open/github/v1?repo=c22211520-Alvarez/MSFPF)

# Proyecto Final: Modelado y control del sistema gastrointestinal - Gastroparesia Diabética

Repositorio académico de la asignatura **Modelado de Sistemas Fisiológicos**, correspondiente al programa de **Ingeniería Biomédica** del Tecnológico Nacional de México / Instituto Tecnológico de Tijuana. Este proyecto final integra el modelado matemático mediante analogías eléctricas, el análisis de estabilidad, el diseño de controladores clásicos y la experimentación *in silico* (Simulink y Python) enfocada en la dinámica del sistema gastrointestinal.

El caso de estudio representa el vaciamiento gástrico mediante un circuito eléctrico equivalente, comparando la respuesta de un individuo sano (control) frente a un caso simulado de Gastroparesia Diabética, y aplicando un controlador para mitigar la diferencia entre ambas respuestas.

**Docente:** Dr. Paul Antonio Valle Trujillo  
**Correo:** paul.valle@tectijuana.edu.mx  
**Departamento:** Ingeniería Eléctrica y Electrónica  
**Institución:** Tecnológico Nacional de México / Instituto Tecnológico de Tijuana  
**Asignatura:** Modelado de Sistemas Fisiológicos  
**Programa:** Ingeniería Biomédica  

**Integrantes del equipo:**
- Álvarez García Gabriela Gissele · C22211520
- Bonilla Martínez Nayeli · 22212381
- Díaz de León Bernal David Emiliano · C23211564

**Repositorio de la asignatura:** https://github.com/DrPaulValle/MSF-IBF1020  
**Sede:** Blvd. Alberto Limón Padilla s/n, Tijuana, C. P. 22454, B. C., México.

---

<a id="contenido"></a>
## Contenido

1. [Resumen](#resumen)
2. [Competencia y objetivos](#objetivos)
3. [Relación con el temario](#temario)
4. [Modelo físico y analogía eléctrica](#analogia)
5. [Formulación matemática](#modelo)
6. [Análisis temporal y de estabilidad](#analisis)
7. [Señales de entrada y condiciones de simulación](#senales)
8. [Implementación en MATLAB, Simulink y Python](#implementacion)
9. [Control en lazo cerrado y sintonización](#pid)
10. [Resultados](#resultados)
11. [Diagrama Fisiológico (BioRender)](#biorender)
12. [Limitaciones del modelo](#limitaciones)
13. [Referencias](#referencias)

---

<a id="resumen"></a>
## Resumen

El modelado de sistemas fisiológicos permite comprender la dinámica del cuerpo humano y evaluar estrategias de control. En este proyecto, se analiza una representación fenomenológica del vaciamiento gástrico mediante una red RLC. El sistema considera una señal de entrada que estimula la llegada de alimento, resistencias que representan la oposición al flujo (esfínteres y viscosidad), un capacitor que simula la acomodación gástrica y un inductor que representa la inercia del contenido.

Mediante la **analogía eléctrica**, se evalúan dos condiciones fisiológicas: un individuo sano (control) y un caso simulado de Gastroparesia Diabética. Utilizando la respuesta del individuo sano como referencia, se diseña un controlador para reducir el error. El desarrollo se realiza exclusivamente *in silico* mediante MATLAB/Simulink y Python, complementado con un diagrama fisiológico elaborado en BioRender.

**Palabras clave:** Gastroparesia Diabética; Vaciamiento gástrico; Sistema gastrointestinal; Modelado fisiológico; Analogía eléctrica; Circuito RLC; Simscape Electrical; Python; BioRender.

[Volver al contenido](#contenido)

---

<a id="objetivos"></a>
## Competencia y objetivos

### Competencia a desarrollar
Modeliza sistemas fisiológicos mediante analogías eléctricas, ecuaciones diferenciales y funciones de transferencia para analizar su comportamiento dinámico y diseña estrategias de control mediante técnicas de control clásico.

### Objetivos específicos
- Analizar la fisiopatología del vaciamiento gástrico y proponer su circuito eléctrico equivalente.
- Obtener el modelo de ecuaciones integro-diferenciales y la función de transferencia del control y del caso.
- Evaluar la estabilidad y el error en estado estacionario de ambos escenarios.
- Implementar el modelo en Simulink (ecuaciones, función de transferencia y circuito) y Python.
- Sintonizar un controlador para reducir la diferencia entre el caso alterado y la referencia sana.
- Elaborar un diagrama biológico del sistema en BioRender.

[Volver al contenido](#contenido)

---

<a id="temario"></a>
## Relación con el temario

El proyecto integra contenidos correspondientes a tres unidades de la asignatura **Modelado de Sistemas Fisiológicos (IBF-1020)**:
- **Unidad I (Sistemas de control retroalimentados):** Análisis de error, estabilidad y diagramas de bloques.
- **Unidad II (Modelado matemático):** Analogía eléctrica del sistema gastrointestinal, leyes de Kirchhoff y función de transferencia.
- **Unidad III (Controladores):** Diseño y sintonización de controladores clásicos.

[Volver al contenido](#contenido)

---

<a id="analogia"></a>
## Modelo físico y analogía eléctrica

El sistema gastrointestinal se aproxima mediante un circuito eléctrico de topología en escalera. Las equivalencias principales son:

| Parámetro | Control (Sano) | Caso (Gastroparesia) | Interpretación Fisiológica |
| :--- | :---: | :---: | :--- |
| **\(V_e(t)\)** | Pulso 1V | Pulso 1V | Estímulo de ingesta (llegada de alimento). |
| **\(R_a\) (Esfínter)** | \(1\ \text{k}\Omega\) | \(10\ \text{k}\Omega\) | Resistencia proximal al tránsito. |
| **\(R_v\) (Viscosidad)** | \(1\ \text{k}\Omega\) | \(10\ \text{k}\Omega\) | Pérdidas viscosas o amortiguamiento. |
| **\(C\) (Complianza)** | \(100\ \mu\text{F}\) | \(100\ \mu\text{F}\) | Acomodación / almacenamiento gástrico. |
| **\(L\) (Inercia)** | \(100\ \text{mH}\) | \(500\ \text{mH}\) | Inercia efectiva del contenido (quimo). |
| **\(R_p\) (Peristalsis)** | \(1\ \text{k}\Omega\) | \(20\ \text{k}\Omega\) | Oposición efectiva al transporte propulsivo. |
| **\(R_f\) (Reflujo)** | \(100\ \text{k}\Omega\) | \(30\ \text{k}\Omega\) | Vía alternativa de descarga (derivación a tierra). |
| **\(R_b\) (Píloro)** | \(10\ \text{k}\Omega\) | \(100\ \text{k}\Omega\) | Resistencia de salida asociada al esfínter pilórico. |

*La modificación de los parámetros en el caso busca reflejar la reducción de la motilidad y el aumento de la resistencia al vaciamiento.*

[Volver al contenido](#contenido)

---

<a id="modelo"></a>
## Formulación matemática

A partir del análisis del circuito equivalente, aplicando las leyes de Kirchhoff (LVK por mallas), se obtienen las ecuaciones integro-diferenciales que rigen el sistema.

**Ecuaciones de malla:**
$$
V_e = R_a I_1 + R_v (I_1 - I_2) + \frac{1}{C} \int (I_1 - I_2) \, dt
$$

$$
0 = L \frac{dI_2}{dt} + R_T I_2 + R_v (I_2 - I_1) + \frac{1}{C} \int (I_2 - I_1) \, dt
$$
*(Donde \(R_T = R_p + R_{eq}\) y \(R_{eq} = R_f \parallel R_b\))*

**Ecuación de salida:**
$$
V_s = R_{eq} I_2
$$

### Procedimiento Algebraico (Transformada de Laplace)
Aplicando Laplace con condiciones iniciales nulas y agrupando términos, se obtiene:

$$
V_e(s) = R_a I_1(s) + \left( R_v + \frac{1}{sC} \right) (I_1(s) - I_2(s))
$$

$$
0 = sL I_2(s) + R_T I_2(s) + \left( R_v + \frac{1}{sC} \right) (I_2(s) - I_1(s))
$$

Despejando y simplificando, se llega a la **Función de Transferencia** final:

$$
G(s) = \frac{V_s(s)}{V_e(s)} = \frac{R_{eq} (1 + s C R_v)}{L C (R_a + R_v) s^2 + [L + C(R_a(R_v + R_p + R_{eq}) + R_v(R_p + R_{eq}))] s + (R_a + R_p + R_{eq})}
$$

### Ecuación Diferencial (EDO)
Invirtiendo la función de transferencia, la EDO que rige la dinámica del voltaje de salida \(V_s(t)\) es un sistema de segundo orden con un cero en el origen.

[Volver al contenido](#contenido)

---

<a id="analisis"></a>
## Análisis temporal y de estabilidad

- **Polos y estabilidad:** El denominador de la función de transferencia es de segundo grado. Al sustituir los valores de los componentes para ambos casos, los polos se encuentran en el semiplano izquierdo del plano complejo \(s\), garantizando un sistema estable. Para el control, \(\lambda_1 \approx -5.25\) y \(\lambda_2 \approx -105908\); para el caso, \(\lambda_1 \approx -0.55\) y \(\lambda_2 \approx -96163\). El caso presenta un polo mucho más cercano al origen, indicando una respuesta más lenta.
- **Error en estado estacionario:** Al evaluar el límite de \(sG(s)\) cuando \(s \to 0\), el sistema se comporta como un integrador, pero debido a la topología de las resistencias, existe un error estacionario teórico del \(18.03\%\) para el control y del \(56.52\%\) para el caso, reflejando una menor capacidad de vaciamiento en el escenario alterado.

[Volver al contenido](#contenido)

---

<a id="senales"></a>
## Señales de entrada y condiciones de simulación

Se seleccionó una señal de entrada tipo **pulso rectangular unitario**, la cual se define como:

$$
V_e(t) = \begin{cases} 1, & 1 \le t < 4 \text{ s}, \\ 0, & \text{en otro caso.} \end{cases}
$$

Esta señal representa un estímulo alimentario delimitado. El intervalo de simulación es de \(0\) a \(10\) s. La amplitud y el tiempo son normalizados y exclusivamente académicos, permitiendo observar tanto el ascenso durante la excitación como la relajación posterior.

[Volver al contenido](#contenido)

---

<a id="implementacion"></a>
## Implementación en MATLAB, Simulink y Python

Se construyeron las siguientes representaciones equivalentes:
1. **Ecuaciones integro-diferenciales:** Mediante bloques de suma, ganancia e integración.
2. **Función de transferencia:** Usando el bloque `Transfer Fcn` con la ecuación obtenida.
3. **Circuito equivalente:** Mediante componentes eléctricos en `Simscape Electrical`.
4. **Python:** Implementación de las funciones de transferencia y simulación del lazo cerrado utilizando la librería `control`.

[Volver al contenido](#contenido)

---

<a id="pid"></a>
## Control en lazo cerrado y sintonización

Se implementó un controlador en Simulink con retroalimentación negativa. La señal de error se define como:
$$
e(t) = V_{s,\text{control}}(t) - V_{s,\text{caso}}(t)
$$

**Ganancias Sintonizadas:**
*(Nota: Agregar aquí las ganancias finales \(k_P\), \(k_I\) y \(k_D\) obtenidas en la herramienta Tune de Simulink).*

[Volver al contenido](#contenido)

---

<a id="resultados"></a>
## Resultados

- **Línea Control (Sana):** Asciende con rapidez y se estabiliza visualmente cerca de 0.82 durante el estímulo.
- **Línea Caso (Gastroparesia):** Comienza alrededor de 0.24 y aumenta lentamente hasta cerca de 0.40 antes de \(t=4\) s.
- **Línea Tratamiento (Caso con Controlador):** Logra estabilizarse y acerca la respuesta del caso a la referencia impuesta por el control, demostrando la eficacia del lazo cerrado.
- Se verificó que las gráficas obtenidas en MATLAB, Simulink y Python son consistentes entre sí, validando el modelo matemático antes de la implementación.

[Volver al contenido](#contenido)

---

<a id="biorender"></a>
## Diagrama Fisiológico (BioRender)

Se elaboró un diagrama del sistema gastrointestinal utilizando la plataforma **BioRender**. 
En este diagrama se ilustra:
- El estómago (fondo y antro) y el píloro.
- El flujo de alimento y la resistencia al vaciamiento.
- El mapeo de los componentes: \(V_e\) (estímulo), \(R_a\) (esfínter proximal), \(C\) (complacencia), \(L\) (inercia), \(R_p\) (peristalsis), \(R_b\) (píloro) y \(R_f\) (vía alternativa).

*El archivo PDF original del diagrama se encuentra anexado en este repositorio.*

[Volver al contenido](#contenido)

---

<a id="limitaciones"></a>
## Limitaciones del modelo

La red no incorpora geometría gástrica, trituración de sólidos, coordinación antroduodenal, ondas lentas, control vagal, reflejos entéricos, señales hormonales ni glucemia. Sus elementos son lineales y constantes. Tampoco hay una correspondencia dimensional comprobada entre voltios/segundos y presión, caudal, volumen o minutos de vaciamiento. La rama \(R_f\) no constituye un conducto retrógrado y la rama \(R_b\) no es la única salida; esta limitación topológica impide interpretar literalmente el circuito como una anatomía exacta del estómago. El modelo aporta una demostración conceptual, no un modelo clínicamente validado.

[Volver al contenido](#contenido)

---

<a id="referencias"></a>
## Referencias

[1] Camilleri, M., Kuo, B., Nguyen, L., Vaughn, V. M., Petrey, J., Greer, K., Yadlapati, R., & Abell, T. L. (2022). ACG clinical guideline: Gastroparesis. *American Journal of Gastroenterology*, 117(8), 1197–1220. https://doi.org/10.14309/ajg.0000000000001874
[2] Bharucha, A. E., Kudva, Y. C., & Prichard, D. O. (2019). Diabetic gastroparesis. *Endocrine Reviews*, 40(5), 1318–1352. https://doi.org/10.1210/er.2018-00161
[3] Du, P., Poh, Y. C., Lim, J. L., Gajendiran, V., O’Grady, G., Buist, M. L., Pullan, A. J., & Cheng, L. K. (2011). A preliminary model of gastrointestinal electromechanical coupling. *IEEE Transactions on Biomedical Engineering*, 58(12), 3491–3495. https://doi.org/10.1109/TBME.2011.2166155
[4] P. A. Valle, *Syllabus para Modelado de Sistemas Fisiológicos*, Tecnológico Nacional de México / Instituto Tecnológico de Tijuana, Tijuana, B.C., México, 2026.
