# Tutorial Básico de LangChain — LLM Chain

Este repositorio contiene la implementación del quickstart de LangChain. Se construye un agente conversacional que usa herramientas para consultar el clima según la ubicación del usuario, responde con juegos de palabras y recuerda el hilo de la conversación entre mensajes.

---

## ¿Cómo funciona?

El agente recibe un mensaje del usuario y decide, por sí solo, qué herramientas necesita llamar para responder. Una vez que obtiene la información, genera una respuesta usando el modelo de lenguaje.

```
Usuario
  │
  ▼
Agente LangChain ──► decide qué herramienta usar
  │
  ├──► get_user_location()        → devuelve la ciudad del usuario
  │
  └──► get_weather_for_location() → devuelve el clima de esa ciudad
  │
  ▼
Groq LLM (llama-3.3-70b-versatile)
  │
  ▼
Respuesta final (con memoria del hilo de conversación)
```

### Componentes principales

| Componente | Rol en el proyecto |
|---|---|
| **LangChain** | Orquesta el agente, las herramientas y el modelo |
| **Groq** | Proveedor gratuito del LLM (`llama-3.3-70b-versatile`) |
| **LangGraph** | Ejecuta el ciclo del agente y administra el estado |
| **InMemorySaver** | Permite al agente recordar mensajes anteriores |
| **@tool** | Decorador que expone funciones Python al agente |

---

## Requisitos previos

- Python 3.9+
- API Key de Groq (gratuita en [console.groq.com](https://console.groq.com))

---

## Pasos para ejecutar

**1. Instalar las dependencias necesarias:**

```bash
pip install langchain langchain-groq langgraph
```

**2. Agregar la API Key en `main.py`:**

```python
os.environ["GROQ_API_KEY"] = "api key"
```

**3. Correr el script:**

```bash
python main.py
```

---

## Resultado al ejecutar

El script envía dos mensajes al agente. El primero dispara el uso de las herramientas. El segundo mensaje demuestra que el agente mantiene el contexto de la conversación.

```
Respuesta 1:
Well, isn't that just a "ray" of sunshine! It looks like you're having a
"cloud"-less day in Florida!

Respuesta 2:
You're "weather" you are, I'm glad I could help! Have a "storm"-free day!
```

---

## Estructura del repositorio

```
Repo1/
├── main.py       # Código principal del agente
├── Images/       # Capturas de pantalla de la ejecución
└── README.md     # Este archivo
```

---

## Capturas de pantalla

![Ejecución del agente](Images/captura1.png)
