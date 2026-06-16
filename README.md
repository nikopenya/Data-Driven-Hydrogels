# Automated Soft-Matter Synthesis & Characterization Lab 
**A Data-Driven, Self-Driving Lab Pipeline for Hydrogel Discovery**

This repository contains the complete ecosystem of Python scripts and automation protocols developed for a high-throughput, closed-loop materials discovery platform. The pipeline successfully integrates Design of Experiments (DoE), automated liquid handling, high-throughput mechanical characterization, and Explainable Machine Learning (XAI) to accelerate the design of biocompatible and semi-interpenetrated hydrogels.

---

## Repository Architecture

The codebase is modularized into four core operational phases, taking the user from theoretical experimental design to predictive physical modeling:

### Phase 1: Experimental Design (DoE)
Algorithms designed to map multi-component composition spaces using **Latin Hypercube Sampling (LHS)**. These scripts maximize formulation diversity while embedding strict rheological safety thresholds to prevent robotic pipetting jams.
* `LHSlap.py`: Generates the 2D sampling space for the baseline PEGDA/LAP hydrogel system.
* `LHSpva.ipynb`: Interactive notebook generating a 3D sampling space for viscoelastically-toughened PVA/PEGDA/LAP semi-IPNs, complete with Plotly 3D visualizations.
* `LHSriboflavin.py`: Maps the 3D sampling matrix for biocompatible Type II PEGDA/TEA/Riboflavin photopolymerizable systems.

### Phase 2: Automated Robotic Synthesis
**Opentrons Flex API v2.21** scripts programmed to command the robotic handler for accurate dispensing, mixing, and formulation into standard 96-well SBS microplates.
* `LAPoptimo_1.py`, `LAPoptimo_2.py`, `LAPoptimo_3.py`: Batch synthesis protocols (PEGDA/LAP) splitting 32 unique formulations (with 3 replicates each) across 3 microplates.
* `PVAoptimo_1.py`, `PVAoptimo_2.py`: Custom high-viscosity liquid-handling protocols optimized for PVA-containing arrays.
* `RFoptimo_1.py`, `RFoptimo_2.py`, `RFoptimo_3.py`: Formulation protocols for the kinetic-sensitive PEGDA/RF/TEA system.

### Phase 3: High-Throughput Characterization & Hardware Control
A suite of scripts to manage hardware diagnostics, positioning, and data acquisition for the Automated Soft Matter Indenter (ASMI).
* `button.py`: Diagnostic utility script designed to verify the hardware-software handshake prior to execution. It ensures correct serial communication and data streaming between the Vernier force sensor, the ASMI control framework, and the host computer.
* `home.py`: Positioning script that safely retracts and homes the CNC axes, returning the indenter to its absolute machine zero position to ensure safe loading/unloading of the microplates.
* `measure.py`: The core data-acquisition and control script. It interfaces asynchronously with the Vernier Go Direct® force sensor and commands the Genmitsu 3018-PRO CNC framework via GRBL (G-Code). It performs deterministic surface detection and automatically fits raw indentation curves to **Hertzian contact mechanics** (bulk range: 0.3–0.7 mm), generating real-time QC plots.

### Phase 4: Exploratory Data Analysis & Machine Learning
Jupyter Notebooks for data curation, metrological validation, and predictive modeling using tree-based ensembles (Random Forest, ExtraTrees, XGBoost) and GPR.

* `Analisis*.ipynb` (`LAP`, `PVA`, `RF`): **Data Curation & EDA**. Applies a strict ≤25% relative fit error threshold to clean raw data. Validates the hardware's inter/intra-session stability and maps the composition-property space using interactive 2D/3D Plotly surfaces.
* `ML_LAP_code_limpio_basico.ipynb`,   `ML_RF_code_limpio_basico.ipynb`,  `ML_PVA_code_limpio_basico.ipynb`: **Baseline Predictive Models**. Trains the algorithms using direct operational variables (absolute precursor concentrations and in water times) as the primary feature space and extracts **SHAP (SHapley Additive exPlanations)** values to translate the ML predictions into interpretable physical laws.
* `ML_LAP_code_limpio.ipynb`,  `ML_RF_code_limpio.ipynb`,  `ML_PVA_code_limpio.ipynb`: **Advanced XAI Models**. Implements Feature Engineering (e.g., stoichiometric ratios) and extracts **SHAP (SHapley Additive exPlanations)** values to translate the ML predictions into interpretable physical laws.

---

## Workflow Pipeline (Quickstart)

1. **Design:** Execute the target `LHS*.py` script to generate a balanced, non-overlapping chemical design space.
2. **Synthesize:** Load the resulting coordinates and volumes into the `*optimo*.py` Opentrons protocols to trigger autonomous microplate formulation.
3. **Characterize:** After UV curing, transfer the plates to the ASMI platform. Run `measure.py` to initiate the unattended mechanical mapping sequence.
4. **Model:** Run the `Analisis*.ipynb` notebooks to metrologically clean the raw Hertzian data, followed by the `ML*.ipynb` pipelines to train the predictive architectures and extract variable importance.

---
## Versión en Español
# Laboratorio Automatizado de Síntesis y Caracterización de Materia Blanda
**Una plataforma "Self-Driving Lab" guiada por datos para el descubrimiento de hidrogeles**

Este repositorio contiene el ecosistema completo de scripts de Python y protocolos de automatización desarrollados para una plataforma de descubrimiento de materiales de alto rendimiento y lazo cerrado (*closed-loop*). El flujo de trabajo integra con éxito el Diseño de Experimentos (DoE), el manejo automatizado de líquidos, la caracterización mecánica de alto rendimiento y el Aprendizaje Automático Explicable (XAI) para acelerar el diseño de hidrogeles biocompatibles y redes semi-interpenetradas.

---

### Arquitectura del Repositorio

El código está modularizado en cuatro fases operativas principales, guiando al usuario desde el diseño experimental teórico hasta el modelado físico predictivo:

### Fase 1: Diseño Experimental (DoE)
Algoritmos diseñados para mapear espacios composicionales multicomponente utilizando el **Muestreo por Hipercubo Latino (LHS)**. Estos scripts maximizan la diversidad de las formulaciones al tiempo que integran estrictos umbrales de seguridad reológica para evitar atascos de pipeteo en el robot.
* `LHSlap.py`: Genera el espacio de muestreo 2D para el sistema base de hidrogeles PEGDA/LAP.
* `LHSpva.ipynb`: Cuaderno interactivo que genera el espacio de muestreo 3D para redes semi-IPN de PVA/PEGDA/LAP reforzadas viscoelásticamente, incluyendo visualizaciones 3D con Plotly.
* `LHSriboflavin.py`: Mapea la matriz de muestreo 3D para los sistemas fotopolimerizables biocompatibles de Tipo II PEGDA/TEOA/Riboflavina.

### Fase 2: Síntesis Robótica Automatizada
Scripts de la **API v2.21 de Opentrons Flex** programados para comandar el robot manipulador de líquidos y realizar una dosificación, mezcla y formulación precisas en microplacas estándar SBS de 96 pocillos.
* `LAPoptimo_1.py`, `LAPoptimo_2.py`, `LAPoptimo_3.py`: Protocolos de síntesis por lotes (PEGDA/LAP) que dividen 32 formulaciones únicas (con 3 réplicas cada una) a lo largo de 3 microplacas.
* `PVAoptimo_1.py`, `PVAoptimo_2.py`: Protocolos de manejo de líquidos de alta viscosidad diseñados a medida y optimizados para matrices que contienen PVA.
* `RFoptimo_1.py`, `RFoptimo_2.py`, `RFoptimo_3.py`: Protocolos de formulación para el sistema PEGDA/RF/TEOA, altamente dependiente de la cinética.

### Fase 3: Caracterización de Alto Rendimiento y Control de Hardware
Un conjunto de scripts para gestionar el diagnóstico de hardware, el posicionamiento y la adquisición de datos para el Indentador Automatizado de Materia Blanda (ASMI).
* `button.py`: Script de utilidad y diagnóstico diseñado para verificar el protocolo de enlace (*handshake*) hardware-software antes de la ejecución. Asegura la correcta comunicación serial y el flujo de datos entre el sensor de fuerza Vernier, el entorno de control del ASMI y el ordenador anfitrión.
* `home.py`: Script de posicionamiento que retrae y devuelve de forma segura los ejes CNC a su posición de cero absoluto (*Home* de la máquina), garantizando una carga y descarga segura de las microplacas.
* `measure.py`: El script central de adquisición de datos y control. Se comunica de forma asíncrona con el sensor de fuerza Vernier Go Direct® y controla la estructura CNC Genmitsu 3018-PRO mediante GRBL (G-Code). Realiza una detección determinista de la superficie y ajusta automáticamente las curvas brutas de indentación a la **mecánica de contacto de Hertz** (rango efectivo: 0.3–0.7 mm), generando gráficos de control de calidad (QC) en tiempo real.

### Fase 4: Análisis Exploratorio de Datos y Machine Learning
Cuadernos de Jupyter para la curación de datos, validación metrológica y modelado predictivo utilizando ensamblados basados en árboles (Random Forest, ExtraTrees, XGBoost) y Regresión por Procesos Gaussianos (GPR).

* `Analisis*.ipynb` (`LAP`, `PVA`, `RF`): **Curación de Datos y EDA**. Aplica un estricto umbral que descarta errores relativos de ajuste ≤25 % para limpiar los datos brutos. Valida la estabilidad inter/intra-sesión del hardware y mapea el espacio composición-propiedad utilizando superficies interactivas 2D/3D de Plotly.
* `ML_*_code_limpio_basico.ipynb`: **Modelos Predictivos Base**. Entrena los algoritmos utilizando variables operativas directas (concentraciones absolutas de precursores y tiempo sumergido en agua) como espacio de características principal y extrae los valores **SHAP (*SHapley Additive exPlanations*)** para traducir las predicciones del modelo en leyes físicas interpretables.
* `ML_*_code_limpio.ipynb`: **Modelos Avanzados de XAI**. Implementa Ingeniería de Características (*Feature Engineering*, p. ej., ratios estequiométricos) y extrae los valores **SHAP** para desglosar la "caja negra" del algoritmo en principios físicos termodinámicos.

---

## Flujo de Trabajo (Guía Rápida)

1. **Diseñar:** Ejecuta el script `LHS*.py` correspondiente para generar un espacio de diseño químico equilibrado y sin solapamientos.
2. **Sintetizar:** Carga las coordenadas y volúmenes resultantes en los protocolos de Opentrons `*optimo*.py` para iniciar la formulación autónoma en las microplacas.
3. **Caracterizar:** Tras el curado UV, transfiere las placas a la plataforma ASMI. Ejecuta `measure.py` para iniciar la secuencia de mapeo mecánico desatendido.
4. **Modelar:** Ejecuta los cuadernos `Analisis*.ipynb` para limpiar metrológicamente los datos de Hertz brutos, seguido de los pipelines `ML*.ipynb` para entrenar las arquitecturas predictivas y extraer la importancia de las variables.

---

## Requisitos e Instalación

Para ejecutar localmente los scripts de diseño, control de hardware y machine learning, asegúrate de tener instalado el siguiente conjunto de librerías científicas:

```bash
pip install numpy pandas scipy matplotlib openpyxl plotly pyserial scikit-learn xgboost shap

## 📦 Requirements & Installation

To run the design, hardware control, and machine learning scripts locally, ensure you have the required scientific computing stack installed:

```bash
pip install numpy pandas scipy matplotlib openpyxl plotly pyserial scikit-learn xgboost shap
