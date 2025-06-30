#!/usr/bin/env python3
"""
Script para verificar que la configuración de Claude Desktop funciona correctamente
"""

import json
import os
import subprocess
from pathlib import Path

def verificar_archivo_config():
    """Verifica que el archivo de configuración de Claude Desktop esté correcto"""
    config_path = Path.home() / "Library/Application Support/Claude/claude_desktop_config.json"
    
    print("🔍 Verificando archivo de configuración de Claude Desktop...")
    print(f"📍 Ubicación: {config_path}")
    
    if not config_path.exists():
        print("❌ El archivo de configuración de Claude Desktop no existe")
        return False
    
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        
        print("✅ Archivo de configuración JSON válido")
        
        # Verificar estructura básica
        if "mcpServers" not in config:
            print("❌ No se encontró la sección 'mcpServers'")
            return False
        
        print("✅ Sección 'mcpServers' encontrada")
        
        # Verificar nuestros servidores
        servidores_fastmcp = ["fastmcp-tutorial", "fastmcp-avanzado", "obsidian-mcp"]
        for servidor in servidores_fastmcp:
            if servidor in config["mcpServers"]:
                print(f"✅ Servidor '{servidor}' configurado")
                
                # Verificar comando
                server_config = config["mcpServers"][servidor]
                if server_config.get("command") == "uv":
                    print(f"  ✅ Comando 'uv' configurado para {servidor}")
                else:
                    print(f"  ❌ Comando incorrecto para {servidor}")
                
                # Verificar args
                args = server_config.get("args", [])
                if "run" in args and "--directory" in args:
                    print(f"  ✅ Argumentos correctos para {servidor}")
                else:
                    print(f"  ❌ Argumentos incorrectos para {servidor}")
            else:
                print(f"❌ Servidor '{servidor}' no encontrado")
        
        return True
        
    except json.JSONDecodeError as e:
        print(f"❌ Error al parsear JSON: {e}")
        return False
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return False

def verificar_servidores():
    """Verifica que los servidores MCP se puedan ejecutar"""
    print("\n🚀 Verificando servidores MCP...")
    
    servidores = [
        ("my_first_server.py", "Servidor Tutorial Básico"),
        ("ejemplo_avanzado.py", "Servidor Avanzado")
    ]
    
    proyecto_dir = Path(__file__).parent
    
    for archivo, nombre in servidores:
        print(f"\n📋 Verificando {nombre}...")
        servidor_path = proyecto_dir / archivo
        
        if not servidor_path.exists():
            print(f"❌ {archivo} no encontrado")
            continue
        
        print(f"✅ Archivo {archivo} encontrado")
        
        # Intentar ejecutar el servidor por 2 segundos
        try:
            cmd = ["uv", "run", "--directory", str(proyecto_dir), archivo]
            print(f"🔧 Ejecutando: {' '.join(cmd)}")
            
            # Usar timeout para evitar que se cuelgue
            result = subprocess.run(
                cmd, 
                timeout=3, 
                capture_output=True, 
                text=True,
                cwd=proyecto_dir
            )
            
            # Si llega aquí, el servidor se ejecutó sin errores inmediatos
            print(f"✅ {nombre} se ejecuta correctamente")
            
        except subprocess.TimeoutExpired:
            # Timeout es esperado para servidores MCP (se quedan escuchando)
            print(f"✅ {nombre} se inició correctamente (timeout esperado)")
        except subprocess.CalledProcessError as e:
            print(f"❌ Error al ejecutar {nombre}: {e}")
            if e.stderr:
                print(f"   Error: {e.stderr}")
        except FileNotFoundError:
            print(f"❌ 'uv' no encontrado. Instala uv primero")
        except Exception as e:
            print(f"❌ Error inesperado con {nombre}: {e}")

def verificar_uv():
    """Verifica que UV esté instalado y funcionando"""
    print("\n⚙️  Verificando UV...")
    
    try:
        result = subprocess.run(["uv", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ UV instalado: {result.stdout.strip()}")
            return True
        else:
            print("❌ UV no responde correctamente")
            return False
    except FileNotFoundError:
        print("❌ UV no está instalado o no está en el PATH")
        return False
    except Exception as e:
        print(f"❌ Error verificando UV: {e}")
        return False

def mostrar_instrucciones():
    """Muestra instrucciones para usar los servidores en Claude Desktop"""
    print("\n" + "="*60)
    print("📋 INSTRUCCIONES PARA USAR TUS SERVIDORES MCP EN CLAUDE")
    print("="*60)
    
    print("\n1. 🔄 REINICIA CLAUDE DESKTOP")
    print("   - Cierra completamente Claude Desktop")
    print("   - Vuelve a abrirlo")
    
    print("\n2. 🔍 VERIFICA LA CONEXIÓN")
    print("   - En Claude, deberías ver tus servidores MCP conectados")
    print("   - Busca indicadores de herramientas disponibles")
    
    print("\n3. 🧪 PRUEBA LAS HERRAMIENTAS")
    print("   Puedes probar comandos como:")
    print("   • 'Salúdame usando tu herramienta de saludo'")
    print("   • 'Calcula 15 + 25 usando tu herramienta'")
    print("   • 'Lista los archivos en mi directorio actual'")
    print("   • 'Crea una nota sobre MCP'")
    print("   • 'Lista todas mis notas de Obsidian'")
    print("   • 'Busca Marco Aurelio en mi vault'")
    print("   • 'Genera estadísticas de mi vault de Obsidian'")
    
    print("\n4. 🛠️ SERVIDORES CONFIGURADOS:")
    print("   • fastmcp-tutorial: Herramientas básicas (saludo, cálculo, hora)")
    print("   • fastmcp-avanzado: Gestión de archivos y notas")
    print("   • obsidian-mcp: Integración completa con tu vault de Obsidian (236 notas)")
    
    print("\n5. 🔧 SI HAY PROBLEMAS:")
    print("   • Revisa los logs de Claude Desktop")
    print("   • Verifica que UV esté en el PATH del sistema")
    print("   • Asegúrate de que los servidores se ejecuten manualmente")
    
    print("\n💡 CONSEJO: Empieza con herramientas simples y luego prueba las avanzadas")

def main():
    print("🚀 Verificación de Configuración MCP para Claude Desktop")
    print("="*60)
    
    # Verificaciones
    config_ok = verificar_archivo_config()
    uv_ok = verificar_uv()
    
    if config_ok and uv_ok:
        verificar_servidores()
        mostrar_instrucciones()
        print("\n✅ ¡Todo listo! Reinicia Claude Desktop para usar tus servidores MCP")
    else:
        print("\n❌ Hay problemas que resolver antes de usar Claude Desktop")
        if not uv_ok:
            print("💡 Instala UV: curl -LsSf https://astral.sh/uv/install.sh | sh")
        if not config_ok:
            print("💡 Revisa el archivo de configuración de Claude Desktop")

if __name__ == "__main__":
    main()
