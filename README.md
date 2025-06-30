# Tutorial de FastMCP

Este proyecto te ayudará a aprender los conceptos básicos de MCP (Model Context Protocol) usando FastMCP en Python.

## ¿Qué es MCP?

MCP (Model Context Protocol) es un protocolo estándar que permite a los modelos de IA interactuar con herramientas, recursos y servicios externos de manera consistente.

## ¿Qué es FastMCP?

FastMCP es una biblioteca de Python que simplifica la creación de servidores MCP, similar a como FastAPI simplifica la creación de APIs web.

## Conceptos Clave

### 1. **Herramientas (Tools)**
Son funciones que el modelo de IA puede llamar para realizar tareas específicas.

### 2. **Recursos (Resources)**
Proporcionan acceso a datos o información que el modelo puede consultar.

### 3. **Prompts**
Son plantillas predefinidas que ayudan a guiar las interacciones con el modelo.

## Estructura del Proyecto

```
fastmcp-tutorial/
├── my_first_server.py  # Servidor MCP de ejemplo
├── README.md          # Este archivo
└── pyproject.toml     # Configuración del proyecto
```

## Cómo Ejecutar el Servidor

1. **Ejecutar el servidor**:
   ```bash
   uv run my_first_server.py
   ```

2. **El servidor se ejecutará en modo stdio** (entrada/salida estándar), que es el protocolo estándar para MCP.

## Ejemplos en el Código

### Herramienta Simple
```python
@mcp.tool()
def saludo(nombre: str) -> str:
    """Saluda a una persona por su nombre"""
    return f"¡Hola {nombre}! Bienvenido al mundo de MCP"
```

### Herramienta con Múltiples Parámetros
```python
@mcp.tool()
def calcular(operacion: str, a: float, b: float) -> str:
    # Realiza operaciones matemáticas básicas
```

### Recurso
```python
@mcp.resource("configuracion")
async def obtener_configuracion() -> str:
    # Proporciona información de configuración
```

### Prompt
```python
@mcp.prompt()
def prompt_ayuda() -> str:
    # Plantilla de ayuda
```

## Próximos Pasos

1. **Experimenta** modificando las herramientas existentes
2. **Agrega** nuevas herramientas y recursos
3. **Integra** el servidor con un cliente MCP (como Claude Desktop)
4. **Explora** casos de uso más avanzados

## Recursos Adicionales

- [Documentación oficial de MCP](https://modelcontextprotocol.io/)
- [FastMCP en GitHub](https://github.com/jlowin/fastmcp)
- [Ejemplos de servidores MCP](https://github.com/modelcontextprotocol/servers)

## Consejos para Aprender

1. Comienza con herramientas simples
2. Agrega logging para entender el flujo de datos
3. Prueba diferentes tipos de parámetros
4. Experimenta con operaciones asíncronas
5. Conecta tu servidor con aplicaciones reales
