# FastMCP Tutorial y Ejemplos Avanzados

¡Bienvenido! Este proyecto te guía desde los conceptos básicos hasta casos de uso avanzados de MCP (Model Context Protocol) usando FastMCP en Python.

## ¿Qué es MCP?
MCP (Model Context Protocol) es un estándar para que modelos de IA interactúen con herramientas, recursos y servicios externos de forma consistente y segura.

## ¿Qué es FastMCP?
FastMCP es una biblioteca Python que simplifica la creación de servidores MCP, similar a FastAPI para APIs web, permitiendo exponer funciones, recursos y prompts de manera modular y escalable.

---

## Estructura del Proyecto

```
fastmcp-tutorial/
├── my_first_server.py        # Ejemplo básico de servidor MCP
├── ejemplo_avanzado.py      # Servidor avanzado: gestión de archivos, notas, búsquedas
├── obsidian_mcp_server.py   # Integración avanzada con Obsidian Vault
├── README.md                # Esta guía
├── pyproject.toml           # Configuración del proyecto
└── ...
```

---

## Ejecución Rápida

1. **Instala dependencias:**
   ```bash
   pip install -r requirements.txt  # o usa pyproject.toml con tu gestor preferido
   ```
2. **Ejecuta un servidor MCP:**
   ```bash
   uv run my_first_server.py
   # o para el avanzado:
   uv run ejemplo_avanzado.py
   ```
   El servidor se ejecuta en modo stdio (entrada/salida estándar), compatible con clientes MCP.

---

## Tabla de Herramientas y Recursos

| Tipo        | Nombre                | Descripción breve                                      |
|-------------|-----------------------|--------------------------------------------------------|
| Herramienta | `saludo`              | Saluda a una persona por su nombre                     |
| Herramienta | `calcular`            | Operaciones matemáticas básicas                        |
| Herramienta | `listar_archivos`     | Lista archivos y carpetas en una ruta                  |
| Herramienta | `leer_archivo`        | Lee el contenido de un archivo de texto                |
| Herramienta | `crear_nota`          | Crea una nota en JSON o Markdown                       |
| Herramienta | `buscar_texto`        | Busca texto en archivos de un directorio               |
| Herramienta | `listar_notas`        | Lista notas Markdown en un vault Obsidian              |
| Herramienta | `leer_nota`           | Lee el contenido de una nota específica                |
| Herramienta | `buscar_en_notas`     | Busca texto o títulos en notas de Obsidian             |
| Recurso     | `configuracion`       | Configuración básica del servidor                      |
| Recurso     | `info_directorio_trabajo` | Info sobre el directorio de trabajo actual         |
| Recurso     | `configuracion_avanzada`  | Configuración avanzada y capacidades declaradas    |

---

## Ejemplos de Uso

### Herramienta Simple
```python
@mcp.tool()
def saludo(nombre: str) -> str:
    """Saluda a una persona por su nombre"""
    return f"¡Hola {nombre}! Bienvenido al mundo de MCP"
```

### Herramienta Avanzada
```python
@mcp.tool()
def listar_archivos(directorio: str = ".") -> str:
    # Lista archivos y carpetas en la ruta dada
```

### Recurso Asíncrono
```python
@mcp.resource("file://directorio_trabajo")
async def info_directorio_trabajo() -> str:
    # Devuelve información estructurada sobre el directorio actual
```

### Prompt Educativo
```python
@mcp.prompt()
def prompt_tutorial_mcp() -> str:
    # Explica objetivos y ejercicios sugeridos para aprender MCP
```

---

## Integración con Obsidian

El archivo `obsidian_mcp_server.py` permite interactuar con tu vault de Obsidian:
- Listar notas por carpeta o globalmente
- Leer el contenido completo de una nota
- Buscar texto en títulos o contenido de notas
- Crear y modificar notas con metadatos y etiquetas

Configura la variable `OBSIDIAN_VAULT_PATH` para apuntar a tu vault local.

---

## Consejos y Buenas Prácticas

- **Modulariza** tus herramientas y recursos para facilitar la extensión.
- **Usa funciones asíncronas** (`async def`) para operaciones de I/O intensivo.
- **Agrega docstrings claros** en español, explicando entradas, salidas y propósito.
- **Evita valores hardcodeados**: usa parámetros y variables configurables.
- **Maneja errores** de forma robusta y devuelve mensajes útiles.
- **Aprovecha prompts** para guiar la interacción y educar a los usuarios.
- **Integra logging** para depuración y trazabilidad.

---

## Próximos Pasos

1. **Experimenta** modificando y extendiendo las herramientas existentes.
2. **Agrega** nuevas funciones útiles para tu flujo de trabajo.
3. **Integra** el servidor con clientes MCP (ej: Claude Desktop, scripts propios).
4. **Explora** casos de uso avanzados: automatización, integración con otros sistemas, etc.

---

## Recursos y Enlaces

- [Documentación oficial de MCP](https://modelcontextprotocol.io/)
- [FastMCP en GitHub](https://github.com/jlowin/fastmcp)
- [Ejemplos de servidores MCP](https://github.com/modelcontextprotocol/servers)
- [Obsidian](https://obsidian.md/)

---

¿Dudas o sugerencias? ¡Modifica este README y contribuye a la documentación!
