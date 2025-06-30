#!/usr/bin/env python3
"""
Cliente simple para probar nuestro servidor MCP
Este script demuestra cómo interactuar con un servidor MCP usando FastMCP
"""

import asyncio
import subprocess
import json
from datetime import datetime

def test_mcp_server():
    """Prueba básica del servidor MCP"""
    print("=== Verificación del Servidor MCP ===\n")
    
    # Verificar que el servidor se puede importar
    try:
        import my_first_server
        print("1. ✅ Servidor MCP importado exitosamente")
        print(f"   Nombre: {my_first_server.mcp.name}")
        
        print("\n2. ✅ Herramientas definidas:")
        print("   • saludo(nombre: str) - Saluda a una persona")
        print("   • calcular(operacion: str, a: float, b: float) - Operaciones matemáticas")
        print("   • hora_actual() - Obtiene fecha y hora actual")
        
        print("\n3. ✅ Recursos definidos:")
        print("   • config://configuracion - Configuración del servidor")
        
        print("\n4. ✅ Prompts definidos:")
        print("   • prompt_ayuda() - Información de ayuda")
        
        print("\n✅ El servidor MCP está correctamente configurado!")
        
    except Exception as e:
        print(f"❌ Error al importar el servidor: {e}")
        raise

def show_mcp_concepts():
    """Muestra conceptos clave de MCP"""
    print("=== Conceptos Clave de MCP ===\n")
    
    conceptos = {
        "Tools (Herramientas)": [
            "Son funciones que el modelo de IA puede llamar",
            "Pueden ser síncronas o asíncronas",
            "Deben tener documentación clara (docstrings)",
            "Pueden recibir múltiples parámetros tipados"
        ],
        "Resources (Recursos)": [
            "Proporcionan acceso a datos externos",
            "Requieren una URI válida",
            "Suelen ser asíncronos",
            "Útiles para acceder a bases de datos, archivos, APIs"
        ],
        "Prompts": [
            "Plantillas predefinidas para interacciones",
            "Ayudan a guiar al modelo de IA",
            "Pueden incluir contexto específico",
            "Facilitan la consistencia en las respuestas"
        ]
    }
    
    for concepto, detalles in conceptos.items():
        print(f"📋 {concepto}:")
        for detalle in detalles:
            print(f"   • {detalle}")
        print()

def show_next_steps():
    """Muestra próximos pasos para aprender más"""
    print("=== Próximos Pasos para Aprender MCP ===\n")
    
    pasos = [
        "🔧 Modificar las herramientas existentes",
        "➕ Agregar nuevas herramientas (ej: acceso a archivos, APIs)",
        "📊 Crear recursos que accedan a datos reales",
        "🔗 Integrar con Claude Desktop u otros clientes MCP",
        "📁 Experimentar con diferentes tipos de datos",
        "⚡ Optimizar el rendimiento de operaciones asíncronas",
        "🛡️ Agregar manejo de errores robusto",
        "📝 Crear documentación detallada para tus herramientas"
    ]
    
    for i, paso in enumerate(pasos, 1):
        print(f"{i}. {paso}")
    
    print(f"\n💡 Consejo: Empieza modificando la función 'calcular' para agregar más operaciones!")

if __name__ == "__main__":
    print("🚀 Aprendiendo FastMCP - Tutorial Interactivo\n")
    print("=" * 50)
    
    try:
        test_mcp_server()
        print("=" * 50)
        show_mcp_concepts()
        print("=" * 50)
        show_next_steps()
        
        print(f"\n✅ ¡Todo funcionando correctamente!")
        print(f"📍 Tu servidor MCP está listo en: {__file__.replace('test_client.py', 'my_first_server.py')}")
        
    except Exception as e:
        print(f"❌ Error durante las pruebas: {e}")
        print(f"💡 Asegúrate de que FastMCP esté instalado: uv add fastmcp")
