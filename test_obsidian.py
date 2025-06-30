#!/usr/bin/env python3
"""
Script de prueba para el servidor MCP de Obsidian
Demuestra las capacidades del servidor con tu vault
"""

import asyncio
from pathlib import Path

def test_obsidian_server():
    """Prueba las funcionalidades del servidor de Obsidian"""
    print("🧠 Probando Servidor MCP de Obsidian")
    print("=" * 50)
    
    try:
        # Importar el servidor
        import obsidian_mcp_server as obs
        
        print("✅ Servidor de Obsidian importado correctamente")
        print(f"📍 Vault configurado: {obs.OBSIDIAN_VAULT_PATH}")
        
        # Verificar que el vault existe
        vault_path = Path(obs.OBSIDIAN_VAULT_PATH)
        if not vault_path.exists():
            print(f"❌ El vault no existe en la ruta configurada")
            return False
        
        print("✅ Vault encontrado y accesible")
        
        # Mostrar herramientas disponibles
        print("\n🛠️ Herramientas disponibles:")
        tools = [
            "📚 listar_notas() - Lista todas las notas del vault",
            "📄 leer_nota(nombre) - Lee una nota específica",
            "🔍 buscar_en_notas(texto) - Busca contenido en las notas",
            "📅 buscar_notas_por_fecha(desde, hasta) - Busca por fechas",
            "✍️ crear_nota(titulo, contenido) - Crea nuevas notas",
            "➕ agregar_a_nota(archivo, contenido) - Agrega a notas existentes",
            "📊 estadisticas_vault() - Estadísticas del vault"
        ]
        
        for tool in tools:
            print(f"   {tool}")
        
        return True
        
    except ImportError:
        print("❌ Error al importar el servidor de Obsidian")
        return False
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return False

def show_vault_overview():
    """Muestra una vista general del vault"""
    print("\n📚 Vista General del Vault 'Secundo Selebro'")
    print("=" * 50)
    
    try:
        import obsidian_mcp_server as obs
        vault_path = Path(obs.OBSIDIAN_VAULT_PATH)
        
        # Contar archivos markdown
        md_files = list(vault_path.rglob("*.md"))
        print(f"📄 Total de notas: {len(md_files)}")
        
        # Contar carpetas
        folders = set()
        for file in md_files:
            parent = file.parent.relative_to(vault_path)
            if str(parent) != '.':
                folders.add(str(parent))
        
        print(f"📁 Carpetas principales: {len(folders)}")
        for folder in sorted(folders)[:10]:  # Mostrar las primeras 10
            folder_files = len(list((vault_path / folder).glob("*.md")))
            print(f"   📁 {folder} ({folder_files} notas)")
        
        # Archivos en la raíz
        root_files = [f for f in md_files if f.parent == vault_path]
        print(f"📄 Notas en la raíz: {len(root_files)}")
        
        # Mostrar algunas notas de ejemplo
        print(f"\n📄 Algunas notas de ejemplo:")
        for file in sorted(root_files)[:5]:
            size_kb = file.stat().st_size / 1024
            print(f"   📄 {file.name} ({size_kb:.1f}KB)")
        
        return True
        
    except Exception as e:
        print(f"❌ Error al analizar vault: {e}")
        return False

def show_usage_examples():
    """Muestra ejemplos de uso del servidor MCP de Obsidian"""
    print("\n💡 Ejemplos de Uso en Claude Desktop")
    print("=" * 50)
    
    examples = [
        {
            "titulo": "📚 Explorar el Vault",
            "comandos": [
                "Lista todas mis notas de Obsidian",
                "Muéstrame las notas en la carpeta 'Diario'",
                "¿Cuántas notas tengo en total?"
            ]
        },
        {
            "titulo": "🔍 Buscar Contenido",
            "comandos": [
                "Busca 'meditación' en todas mis notas",
                "Encuentra referencias a 'Marco Aurelio'",
                "¿En qué notas hablo sobre filosofía?"
            ]
        },
        {
            "titulo": "📄 Leer Notas Específicas",
            "comandos": [
                "Lee mi nota 'Meditaciones - Marco Aurelio'",
                "Muéstrame el contenido de 'Sobre la perspectiva'",
                "¿Qué escribí en 'Transformaciones estadísticas'?"
            ]
        },
        {
            "titulo": "✍️ Crear y Editar",
            "comandos": [
                "Crea una nota sobre lo que he aprendido de MCP",
                "Agrega una reflexión a mi nota sobre el tiempo",
                "Crea una nueva entrada en mi carpeta de aprendizaje"
            ]
        },
        {
            "titulo": "📊 Análisis del Vault",
            "comandos": [
                "Genera estadísticas de mi vault de Obsidian",
                "¿Cuáles son mis temas más frecuentes?",
                "Muéstrame mis notas más recientes"
            ]
        }
    ]
    
    for example in examples:
        print(f"\n{example['titulo']}:")
        for comando in example['comandos']:
            print(f"   💬 \"{comando}\"")

def show_integration_tips():
    """Muestra consejos para la integración con Claude Desktop"""
    print("\n🎯 Consejos para Usar el Servidor MCP de Obsidian")
    print("=" * 50)
    
    tips = [
        "🔄 Reinicia Claude Desktop después de agregar el servidor",
        "🧠 El servidor puede leer y crear notas en tu vault automáticamente",
        "🔍 Usa búsquedas específicas para encontrar información rápidamente",
        "📝 Puedes crear notas directamente desde conversaciones con Claude",
        "📊 Las estadísticas te ayudan a entender mejor tu vault",
        "🏷️ El servidor puede manejar etiquetas y metadatos de Obsidian",
        "📁 Respeta la estructura de carpetas de tu vault",
        "💡 Experimenta con diferentes tipos de consultas"
    ]
    
    for tip in tips:
        print(f"   {tip}")
    
    print("\n🚀 ¡Ahora tienes un asistente IA que puede interactuar con tu vault de Obsidian!")

def main():
    print("🧠 Test del Servidor MCP de Obsidian")
    print("🎯 Integrando tu vault 'Secundo Selebro' con Claude Desktop")
    print("=" * 70)
    
    # Ejecutar pruebas
    if not test_obsidian_server():
        print("\n❌ Fallo en las pruebas básicas del servidor")
        return
    
    if not show_vault_overview():
        print("\n❌ No se pudo analizar el vault")
        return
    
    show_usage_examples()
    show_integration_tips()
    
    print("\n" + "=" * 70)
    print("✅ ¡Servidor MCP de Obsidian listo para usar con Claude Desktop!")
    print("🔄 Recuerda reiniciar Claude Desktop para que detecte el nuevo servidor")

if __name__ == "__main__":
    main()
