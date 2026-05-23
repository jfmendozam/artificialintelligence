# 📘 Inteligencia Artificial

<p align="center">
  <img src="book_cover.png" width="640">
</p>

<p align="center">
  <b>Repositorio oficial del libro</b><br>
  Talleres • Ejercicios • Recursos • Código fuente
</p>

---

## ✨ Descripción

Este repositorio contiene el material complementario del libro **Inteligencia Artificial**.

Aquí encontrarás:

- 📚 Talleres prácticos
- 💻 Ejercicios de programación
- 📓 Notebooks interactivos
- 📂 Datasets
- ✅ Soluciones
- 🔗 Recursos adicionales

---

# 🗂️ Tabla de Contenido

```text
CAPÍTULO DE GENERALIDADES   
Introducción al Espacio Académico
Presentación de los capítulos

CAPÍTULO 1. INTRODUCCIÓN A LA INTELIGENCIA ARTIFICIAL (IA)
1.1 Introducción
1.2 Resumen
1.3 Definición de IA
1.4 Historia de la IA
1.5 El Test de Turing
1.6 Identificación de Problemas Aptos para la IA
1.6.1 Diagnóstico Médico
1.6.2 Supermercados y Cajeros Automáticos
1.6.3 El Ajedrez como Laboratorio de IA
1.6.4 ¿Qué Tipos de Problemas Son Aptos para Sistemas Expertos?
1.7 Diversas disciplinas en IA
1.8 Importancia de la IA
1.9 Campos y Aplicaciones de la IA
1.10 Ramas de la IA
1.11 Tipos de IA
1.12 Solucionador General de Problemas (GPS)
1.13 Consideraciones Éticas de la IA
1.14 IA, Aprendizaje Automático y Aprendizaje Profundo
1.15 IA Generativa
```
1.15.1 Exploración de Herramientas IA: [![](https://img.shields.io/badge/PDF-150KB-FF61F6?logo=pdf&logoColor=white&style=for-the-badge)](workshops/pag47/guía_explorar_herramientas_IA.pdf)
```text
1.16 Algoritmos de Búsqueda
1.16.1 Algoritmos de búsqueda no informada
1.16.2 Búsqueda no informada versus informada
1.16.3 Trade-off entre memoria y tiempo en estos algoritmos
1.16.4 Limitaciones y consideraciones
1.16.5 Buscar un archivo específico dentro de un sistema de archivos
```
1.16.6 [Estructura general del código](workshops/pag57/IA_Guía_DFS_BFS.pdf), [![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](workshops/pag57/file_search.py) (file_search.py)
```text
1.16.7 Algoritmo Greedy Best-First Search (GBFS)
```
1.16.8 [Python Algoritmo GBFS](workshops/pag62/file_search_gbfs.py)
```text
1.16.9 Algoritmo A*
```
1.16.10 [Python Algorithmo A*](workshops/pag64/file_search_astar.py)
```text
1.17 Agentes basados en conocimiento
1.17.1 Lógica Proposicional: Lenguaje Formal del Conocimiento
1.17.2 Modelos y Mundos Posibles
1.17.3 Base de Conocimiento e Inferencia
1.17.4 Verificación de Modelos (Model Checking)
1.17.5 Hacia Agentes Basados en Conocimiento
```
1.17.6 Implementación de Bases de Conocimiento en Python: [logic.py](workshops/pag73/logic.py), [medico_o_clase.py](workshops/pag73/medico_o_clase.py) y [programando.py](workshops/pag73/programando.py)
```text
1.17.7 Inferencia en Agentes Basados en Conocimiento
```
1.17.8. Implementación de CNF en Python [logic.py](workshops/pag78/logic.py), [futbol.py](workshops/pag78/futbol.py) y [perdidos.py](workshops/pag78/perdidos.py)
```text

CAPÍTULO 2. APRENDIZAJE PROFUNDO (DEEP LEARNING)
2.1 Introducción
2.2 Resumen
2.3 Arquitectura de una red neuronal profunda
2.4 Tipos de Redes Neuronales Artificiales
2.5 Redes recurrentes y memoria temporal
2.6 Redes convolucionales para visión artificial
2.7 Arquitectura y Funcionamiento Básico de una Red Neuronal Totalmente Conectada (FCN)
2.7.1 Capas fundamentales
2.7.2 Conexiones y almacenamiento del conocimiento
2.7.3 Propagación hacia adelante
2.7.4 Cálculo del error
2.7.5 Retropropagación y ajuste de pesos
2.7.6 Proceso completo de aprendizaje
2.7.7 Limitación a funciones lineales
2.7.8 Ejemplo con una red neuronal de una sola neurona
2.8 Funciones de Activación en Redes Neuronales
2.8.1 Necesidad de no linealidad
2.8.2 Función lineal
2.8.3 Unidad Rectificada Lineal (ReLU)
2.8.4 ReLU con Fuga (Leaky ReLU)
2.8.5 Función Sigmoide
2.8.6 Función Tangente Hiperbólica (Tanh)
2.8.7 Función Softmax
2.8.8 Selección práctica de funciones de activación
```
2.9 Laboratorio para construir una Red Neuronal [![Notebook](https://img.shields.io/badge/Notebooks-Jupyter-orange)](workshops/pag99/mobile_price.ipynb)
```text
2.10 Redes Neuronales Recurrentes para Datos Secuenciales
2.10.1 Limitaciones de las redes feed-forward
2.10.2 Introducción del bucle de retroalimentación ("Feedback")
2.10.3 Operación matemática en un paso temporal
2.10.4 Estructura de la red recurrente
2.10.5 Memoria y contexto en aplicaciones prácticas
2.10.6 Estado oculto como resumen dinámico
2.10.7 Ventajas frente a arquitecturas tradicionales
2.10.8 Consideraciones en el diseño
2.11 Redes Convolucionales
2.11.1 Componentes fundamentales
2.11.2 Capa convolucional
2.11.3 Función de activación
2.11.4 Capa de pooling
2.11.5 Jerarquía de representaciones
2.11.6 Etapa de clasificación
2.11.7 Entrenamiento y optimización

CAPÍTULO 3. PROCESAMIENTO DE LENGUAJE NATURAL (NLP)
3.1 Introducción
3.2 Resumen
3.3 Evolución histórica de enfoques
3.4 Tareas principales en PLN
3.4.1 Desafíos persistentes
3.4.2 Pipeline típico de procesamiento
3.4.3 Aplicaciones cotidianas
3.4.4 Importancia como pilar de la IA generativa
3.5 Representaciones Vectoriales del Lenguaje: Los Embeddings
3.5.1 De la codificación simbólica a la representación distribuida
3.5.2 Captura de significado mediante contexto
3.5.3 Relaciones analógicas y estructura conceptual
3.5.4 Limitaciones de los embeddings estáticos
3.5.5 Extensiones a unidades mayores
3.5.6 Aplicaciones prácticas
3.5.7 Desafíos y consideraciones éticas
3.5.8 Técnicas de mitigación
3.5.9 Rol en la IA moderna
3.6 Ingeniería de Prompts
3.6.1 Técnicas de Ingeniería Prompt
3.6.2 El contexto en Ingeniería Prompt
3.7 Evaluación de Sistemas de IA Generativa
3.7.1 Categorías principales de métricas
3.7.2 Fluidez y naturalidad del lenguaje
3.7.3 Coherencia, relevancia y precisión factual
3.7.4 Creatividad, diversidad y equidad
3.7.5 Métricas automáticas específicas
3.7.6 Evaluación humana como estándar definitivo
3.7.7 Proceso iterativo y responsabilidad ética
3.8 Laboratorio NLP
3.9 Generación de Texto
3.9.1 Resumen de Contenido
3.9.2 Traducción Automática
3.9.3 Impacto Integrado y Desafíos
3.9.4 Laboratorio de Resumen de Texto y escritura creativa
3.10 Análisis de Sentimientos
3.10.1 Funcionamiento del Análisis de Sentimientos
3.10.2 Factores que contribuyen al Sesgo en el Análisis de Sentimientos
3.10.3. Laboratorio Análisis de Sentimientos

CAPÍTULO 4. VISIÓN POR COMPUTADOR Y ROBÓTICA
4.1 Introducción
4.2 Resumen
4.3 Visión por Computador
4.3.1 Definición y Principios Operativos
4.3.2 Relevancia en la Práctica Cotidiana
4.3.3. Aplicaciones Sectoriales
4.3.4 Perspectivas Emergentes
4.3.5 Funcionamiento de la Visión por Computador: Etapas Principales
4.3.6 Representación y Procesamiento de Imágenes Digitales
4.3.7 Filtrado y Realce de Imágenes en Procesamiento Digital
4.3.8 Características y Descriptores en Imágenes Digitales
4.3.9 Descriptores de Imagen y Emparejamiento de Características
4.3.10 Clasificación de Imágenes y Reconocimiento de Objetos
4.3.11 Detección y Localización de Objetos en Imágenes
4.3.12 Segmentación de Imágenes: Conceptos y Métodos
4.3.13 Métodos de Umbralización y Segmentación por Regiones
4.3.14 Laboratorio de Visión por Computador
4.4 Robótica
4.4.1 Introducción
4.4.2 Evolución de la Robótica Industrial
4.4.3 Sistema Operativo de Robots (ROS)
4.4.4 Madurez en Automatización
4.4.5 Laboratorio Robótica

CAPÍTULO 5. La IA GENERATIVA
5.1 Introducción
5.2 Resumen
5.3 Introducción a la IA Generativa
5.4 Tipos de Modelos Generativos
5.4.1 Redes Antagónicas Generativas
5.4.2 Autoencoders Variacionales
5.4.3 Modelos de Difusión
5.4.4 Modelos de Lenguaje a Gran Escala (LLM)
5.4.5 Comparación de Arquitecturas
5.4.6 Laboratorio de Introducción a la IA Generativa
5.5. LLMs
5.5.1 Introducción a los Modelos de Lenguaje a Gran Escala (LLMs)
5.5.2 La Atención
5.5.3 Tokens
5.5.4 Aplicaciones
5.5.5 Principales Modelos
5.5.6 Restricciones
5.5.7 Laboratorio de Introducción a los Modelos de Lenguaje a Gran Escala
5.6 Transformers
5.6.1 Codificador y Decodificador
5.6.2 El Mecanismo de Atención
5.6.3 Atención Multi-Cabezal (Multi-Head)
5.6.4 Capas de Atención
5.6.5 Ventajas de los Transformers
5.6.6 Laboratorio de Transformers
5.7 Datos de Entrenamiento y Tokenización
5.7.1 Composición y Alcance de los Datos de Entrenamiento
5.7.2 Desafíos Éticos y Técnicos en la Curación de Datos
5.7.3 Proceso y Variantes de Tokenización
5.7.4 Impacto de la Tokenización en el Rendimiento
5.7.5 Interdependencia entre Datos y Tokenización
5.7.6 Laboratorio de Transformers
5.8 Etapas de Desarrollo de Modelos de Lenguaje Extensos: Preentrenamiento y Ajuste Fino
5.8.1 Preentrenamiento: Construcción de la Base Lingüística
5.8.2 Ajuste Fino: Especialización Contextual
5.8.3 Aprendizaje por Refuerzo con Retroalimentación Humana
5.8.4 Complementariedad de las Fases
5.8.5 Ejemplos de Implementación Sectorial
5.8.6 Implicaciones Estratégicas
5.8.7 Laboratorio de Pre-Training y Fine-Tuning
5.9 Integración de Modelos de Lenguaje en Aplicaciones Prácticas
5.9.1 Arquitectura Modular de Aplicaciones
5.9.2 Asistentes Conversacionales
5.9.3 Herramientas de Síntesis Documental
5.9.4 Traducción Contextual Multilingüe
5.9.5 Asistentes de Redacción Creativa y Técnica
5.9.6 Desarrollo con Plataformas de Bajo Código
5.9.7 Principios de Diseño Responsable
5.9.8 Consideraciones Operativas y Éticas
5.10 Hugging Face: Ecosistema Abierto para la Democratización de la IA
5.10.1 Biblioteca Transformers: Acceso Simplificado a Modelos de Vanguardia
5.10.2 Pipelines: Prototipado Rápido de Aplicaciones
5.10.3 Tokenización Avanzada y Multilingüe
5.10.4 Alcance Multimodal
5.10.5 Datasets y Spaces: Infraestructura Colaborativa
5.10.6 Ejemplo Práctico: Resumidor de Informes
5.10.7 Ventajas Estratégicas del Ecosistema
5.10.8 Impacto en la Democratización del Conocimiento
5.11 Bases de Datos Vectoriales
5.11.1 Limitaciones de Bases de Datos Convencionales
5.11.2 Flujo Operativo de una Base Vectorial
5.11.3 Pinecone: Solución Gestionada en la Nube
5.11.4 FAISS: Eficiencia a Gran Escala de Código Abierto
5.11.5 Weaviate: Enfoque Híbrido Vectorial-Gráfico
5.11.6 Aplicaciones Sectoriales
5.11.7 Ventajas Estratégicas
5.11.8 Desafíos y Consideraciones de Diseño
5.12 Generación Aumentada por Recuperación: RAG
5.12.1 Problema de los Modelos de Lenguaje Convencionales
5.12.2 Mecanismo Operativo de RAG
5.12.3 Componentes: Recuperación y Generación
5.12.4 Comparación con Ajuste Fino
5.12.5 Ventajas Estratégicas de RAG
5.12.6 Ejemplo Práctico en Soporte Técnico
5.12.7 Reflexiones sobre Implementación
5.13 Arquitectura de Sistemas de Generación Aumentada por Recuperación
5.13.1 Componentes Fundamentales del Sistema
5.13.2 Funcionamiento del Recuperador
5.13.3 Estructura de la Base de Conocimiento
5.13.4 Rol del Generador
5.13.5 Flujo Operativo Integrado
5.13.6 Ventajas Estratégicas del Diseño
5.13.7 Consideraciones de Implementación
5.13.8 Ejemplo en Gestión de Conocimiento Corporativo
5.14 LangChain: Orquestación Modular para Sistemas de Generación Aumentada por Recuperación
5.14.1 Arquitectura Jerárquica de LangChain
5.14.2 Cadenas: Flujos Estructurados de Procesamiento
5.14.3 Agentes: Inteligencia Adaptativa
5.14.4 Memoria: Continuidad Contextual
5.14.5 Herramientas y Recuperadores: Conexión con el Entorno
5.14.6 Pipeline RAG Orquestado por LangChain
5.14.7 Ventajas Estratégicas de la Arquitectura
5.14.8 Consideraciones de Implementación
5.14.9 Caso Práctico en Análisis de Mercado
GLOSARIO
REFERENCIAS BIBLIOGRÁFICAS
```
---

# 🧪 Talleres

| Taller | Descripción | Enlace |
|---|---|---|
| Taller 01 | Explorar Herramientas de Inteligencia Artificial | [Ir al taller](workshops/pag47/guía_explorar_herramientas_IA.pdf) |
| Taller 02 | Algoritmos de búsqueda DFS y BFS | [Ir al taller](workshops/pag57/IA_Guía_DFS_BFS.pdf) <--> [Python](workshops/pag57/file_search.py) |
| Taller 03 | Algoritmo GBFS | [Python](workshops/pag62/file_search_gbfs.py) |
| Taller 04 | Algoritmo A* | [Python Algorithmo A*](workshops/pag64/file_search_astar.py) |
| Taller 05 | Bases de conocimiento | [logic.py](workshops/pag73/logic.py), [medico_o_clase.py](workshops/pag73/medico_o_clase.py) y [programando.py](workshops/pag73/programando.py) |
| Taller 06 | CNF | [logic.py](workshops/pag78/logic.py), [futbol.py](workshops/pag78/futbol.py) y [perdidos.py](workshops/pag78/perdidos.py) |
| Taller 07 | Red Neuronal | [![Notebook](https://img.shields.io/badge/Notebooks-Jupyter-orange)](workshops/pag99/mobile_price.ipynb) |


# 🚀 Cómo usar este repositorio

## 1. Clonar el repositorio

```bash
git clone https://github.com/usuario/nombre-repo.git
```

## 2. Entrar al proyecto

```bash
cd nombre-repo
```

## 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# 📁 Estructura del proyecto

```text
.
├── README.md
├── book_cover.png
├── workshops/
```

---

# 📓 Ejecutar notebooks

Puedes abrir los notebooks localmente usando:

- Jupyter Notebook
- VSCode
- Google Colab

---

# 🛠️ Tecnologías utilizadas

- Python
- Jupyter
- Pandas
- NumPy
- Scikit-Learn

---

# 🤝 Contribuciones

Si encuentras errores o deseas proponer mejoras:

1. Haz un fork
2. Crea una rama
3. Envía un Pull Request

---

# 📄 Licencia

Este proyecto está bajo la licencia MIT.

---

# 👨‍🏫 Autores

**Juan Francisco Mendoza Moreno**

**Luz Santamaría Granados**

- Sitio web: (https://santotovirtual.edu.co/especializacion-en-ciencia-de-datos/)
- LinkedIn: https://linkedin.com/in/jfmendozam
- GitHub: https://github.com/jfmendozam
