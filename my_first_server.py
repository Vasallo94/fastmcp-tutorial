#!/usr/bin/env python3
"""
Mi primer servidor MCP con FastMCP
Este ejemplo muestra los conceptos básicos de MCP:
- Herramientas (tools)
- Recursos (resources)
- Prompts
"""

import asyncio
from datetime import datetime
from fastmcp import FastMCP

# Crear el servidor MCP
mcp = FastMCP("Mi Primer Servidor MCP")

# Ejemplo 1: Herramienta simple
@mcp.tool()
def saludo(nombre: str) -> str:
    """Saluda a una persona por su nombre"""
    return f"¡Hola {nombre}! Bienvenido al mundo de MCP"

# Ejemplo 2: Herramienta con múltiples parámetros
@mcp.tool()
def calcular(operacion: str, a: float, b: float) -> str:
    """
    Realiza operaciones matemáticas básicas
    
    Args:
        operacion: Tipo de operación (suma, resta, multiplicacion, division)
        a: Primer número
        b: Segundo número
    """
    operaciones = {
        "suma": a + b,
        "resta": a - b,
        "multiplicacion": a * b,
        "division": a / b if b != 0 else "Error: División por cero"
    }
    
    resultado = operaciones.get(operacion.lower())
    if resultado is None:
        return f"Operación '{operacion}' no soportada. Usa: suma, resta, multiplicacion, division"
    
    return f"{a} {operacion} {b} = {resultado}"

# Ejemplo 3: Herramienta asíncrona
@mcp.tool()
async def hora_actual() -> str:
    """Obtiene la fecha y hora actual"""
    await asyncio.sleep(0.1)  # Simular una operación asíncrona
    return f"Fecha y hora actual: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

# Ejemplo 4: Recurso simple
@mcp.resource("config://configuracion")
async def obtener_configuracion() -> str:
    """Configuración del servidor MCP"""
    config = {
        "nombre": "Mi Primer Servidor MCP",
        "version": "1.0.0",
        "herramientas_disponibles": ["saludo", "calcular", "hora_actual"],
        "descripcion": "Servidor de ejemplo para aprender FastMCP"
    }
    return str(config)

# Ejemplo 5: Prompt personalizado
@mcp.prompt()
def prompt_ayuda() -> str:
    """Muestra información de ayuda sobre el servidor"""
    return """
    Bienvenido al servidor MCP de ejemplo.
    
    Herramientas disponibles:
    - saludo(nombre): Saluda a una persona
    - calcular(operacion, a, b): Realiza operaciones matemáticas
    - hora_actual(): Obtiene la fecha y hora actual
    
    Recursos disponibles:
    - configuracion: Muestra la configuración del servidor
    
    ¡Empieza a experimentar con MCP!
    """

if __name__ == "__main__":
    # Ejecutar el servidor
    mcp.run()
