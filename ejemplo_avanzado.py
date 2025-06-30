#!/usr/bin/env python3
"""
Ejemplo más avanzado de servidor MCP con FastMCP
Este servidor incluye herramientas más prácticas y casos de uso reales
"""

import asyncio
import os
import json
from datetime import datetime, timedelta
from pathlib import Path
from fastmcp import FastMCP

# Crear el servidor MCP avanzado
mcp = FastMCP("Servidor MCP Avanzado")

# ========== HERRAMIENTAS DE SISTEMA ==========

@mcp.tool()
def listar_archivos(directorio: str = ".") -> str:
    """
    Lista los archivos y directorios en una ruta específica
    
    Args:
        directorio: Ruta del directorio a listar (por defecto: directorio actual)
    """
    try:
        path = Path(directorio)
        if not path.exists():
            return f"❌ El directorio '{directorio}' no existe"
        
        if not path.is_dir():
            return f"❌ '{directorio}' no es un directorio"
        
        archivos = []
        directorios = []
        
        for item in path.iterdir():
            if item.is_dir():
                directorios.append(f"📁 {item.name}/")
            else:
                size = item.stat().st_size
                archivos.append(f"📄 {item.name} ({size} bytes)")
        
        resultado = f"📂 Contenido de '{directorio}':\n\n"
        
        if directorios:
            resultado += "Directorios:\n"
            for dir_item in sorted(directorios):
                resultado += f"  {dir_item}\n"
            resultado += "\n"
        
        if archivos:
            resultado += "Archivos:\n"
            for archivo in sorted(archivos):
                resultado += f"  {archivo}\n"
        
        if not directorios and not archivos:
            resultado += "  (directorio vacío)"
        
        return resultado
        
    except Exception as e:
        return f"❌ Error al listar archivos: {e}"

@mcp.tool()
def leer_archivo(ruta: str, max_lineas: int = 50) -> str:
    """
    Lee el contenido de un archivo de texto
    
    Args:
        ruta: Ruta del archivo a leer
        max_lineas: Número máximo de líneas a mostrar (por defecto: 50)
    """
    try:
        path = Path(ruta)
        if not path.exists():
            return f"❌ El archivo '{ruta}' no existe"
        
        if not path.is_file():
            return f"❌ '{ruta}' no es un archivo"
        
        with open(path, 'r', encoding='utf-8') as file:
            lineas = file.readlines()
        
        total_lineas = len(lineas)
        
        if total_lineas > max_lineas:
            contenido = ''.join(lineas[:max_lineas])
            resultado = f"📄 Archivo: {ruta}\n"
            resultado += f"📊 Mostrando las primeras {max_lineas} de {total_lineas} líneas\n\n"
            resultado += contenido
            resultado += f"\n... ({total_lineas - max_lineas} líneas más)"
        else:
            contenido = ''.join(lineas)
            resultado = f"📄 Archivo: {ruta}\n"
            resultado += f"📊 Total: {total_lineas} líneas\n\n"
            resultado += contenido
        
        return resultado
        
    except UnicodeDecodeError:
        return f"❌ No se puede leer '{ruta}': archivo binario o codificación incompatible"
    except Exception as e:
        return f"❌ Error al leer archivo: {e}"

# ========== HERRAMIENTAS DE DATOS ==========

@mcp.tool()
def crear_nota(titulo: str, contenido: str) -> str:
    """
    Crea una nota en formato JSON en el directorio actual
    
    Args:
        titulo: Título de la nota
        contenido: Contenido de la nota
    """
    try:
        nota = {
            "titulo": titulo,
            "contenido": contenido,
            "fecha_creacion": datetime.now().isoformat(),
            "id": datetime.now().strftime("%Y%m%d_%H%M%S")
        }
        
        nombre_archivo = f"nota_{nota['id']}.json"
        
        with open(nombre_archivo, 'w', encoding='utf-8') as file:
            json.dump(nota, file, indent=2, ensure_ascii=False)
        
        return f"✅ Nota creada: {nombre_archivo}\n📝 Título: {titulo}\n📅 Fecha: {nota['fecha_creacion']}"
        
    except Exception as e:
        return f"❌ Error al crear nota: {e}"

@mcp.tool()
def buscar_texto(patron: str, directorio: str = ".", extension: str = ".txt") -> str:
    """
    Busca un patrón de texto en archivos de un directorio
    
    Args:
        patron: Texto a buscar
        directorio: Directorio donde buscar (por defecto: directorio actual)
        extension: Extensión de archivos a buscar (por defecto: .txt)
    """
    try:
        path = Path(directorio)
        if not path.exists():
            return f"❌ El directorio '{directorio}' no existe"
        
        resultados = []
        archivos_revisados = 0
        
        for archivo in path.glob(f"*{extension}"):
            if archivo.is_file():
                archivos_revisados += 1
                try:
                    with open(archivo, 'r', encoding='utf-8') as file:
                        lineas = file.readlines()
                    
                    for num_linea, linea in enumerate(lineas, 1):
                        if patron.lower() in linea.lower():
                            resultados.append({
                                "archivo": archivo.name,
                                "linea": num_linea,
                                "contenido": linea.strip()
                            })
                except:
                    continue
        
        if not resultados:
            return f"🔍 No se encontró '{patron}' en {archivos_revisados} archivos {extension} en '{directorio}'"
        
        resultado = f"🔍 Búsqueda de '{patron}' en {archivos_revisados} archivos:\n\n"
        
        for match in resultados[:20]:  # Limitar a 20 resultados
            resultado += f"📄 {match['archivo']} (línea {match['linea']}):\n"
            resultado += f"   {match['contenido']}\n\n"
        
        if len(resultados) > 20:
            resultado += f"... y {len(resultados) - 20} resultados más"
        
        return resultado
        
    except Exception as e:
        return f"❌ Error en búsqueda: {e}"

# ========== RECURSOS ==========

@mcp.resource("file://directorio_trabajo")
async def info_directorio_trabajo() -> str:
    """Información sobre el directorio de trabajo actual"""
    try:
        cwd = os.getcwd()
        path = Path(cwd)
        
        # Contar archivos y directorios
        archivos = sum(1 for x in path.iterdir() if x.is_file())
        directorios = sum(1 for x in path.iterdir() if x.is_dir())
        
        # Información del directorio
        info = {
            "directorio_actual": cwd,
            "total_archivos": archivos,
            "total_directorios": directorios,
            "espacio_total": "N/A",  # Requeriría shutil.disk_usage()
            "ultima_modificacion": datetime.fromtimestamp(path.stat().st_mtime).isoformat()
        }
        
        return json.dumps(info, indent=2, ensure_ascii=False)
        
    except Exception as e:
        return f"Error obteniendo información del directorio: {e}"

@mcp.resource("config://configuracion_avanzada")
async def configuracion_avanzada() -> str:
    """Configuración avanzada del servidor MCP"""
    config = {
        "servidor": {
            "nombre": "Servidor MCP Avanzado",
            "version": "2.0.0",
            "descripcion": "Servidor con herramientas prácticas para gestión de archivos y datos"
        },
        "herramientas": {
            "sistema": ["listar_archivos", "leer_archivo"],
            "datos": ["crear_nota", "buscar_texto"]
        },
        "recursos": ["info_directorio_trabajo", "configuracion_avanzada"],
        "capacidades": [
            "Gestión de archivos y directorios",
            "Lectura de archivos de texto",
            "Creación de notas en JSON",
            "Búsqueda de texto en archivos",
            "Información del sistema de archivos"
        ]
    }
    
    return json.dumps(config, indent=2, ensure_ascii=False)

# ========== PROMPTS ==========

@mcp.prompt()
def prompt_gestor_archivos() -> str:
    """Prompt especializado para gestión de archivos"""
    return """
    Eres un asistente especializado en gestión de archivos y directorios.
    
    Tienes acceso a las siguientes herramientas:
    
    🗂️ GESTIÓN DE ARCHIVOS:
    - listar_archivos(directorio): Lista contenido de directorios
    - leer_archivo(ruta, max_lineas): Lee archivos de texto
    - crear_nota(titulo, contenido): Crea notas en JSON
    - buscar_texto(patron, directorio, extension): Busca texto en archivos
    
    📋 CONSEJOS DE USO:
    - Siempre verifica que los archivos/directorios existan antes de operaciones
    - Usa rutas relativas cuando sea posible
    - Limita la lectura de archivos grandes especificando max_lineas
    - Para búsquedas específicas, ajusta la extensión de archivo
    
    ¿En qué puedo ayudarte con la gestión de archivos?
    """

@mcp.prompt()
def prompt_tutorial_mcp() -> str:
    """Prompt educativo sobre MCP"""
    return """
    ¡Bienvenido al tutorial avanzado de MCP (Model Context Protocol)!
    
    🎯 OBJETIVOS DE APRENDIZAJE:
    1. Entender cómo crear herramientas prácticas
    2. Implementar recursos que accedan a datos reales
    3. Usar prompts para guiar interacciones específicas
    4. Manejar errores de manera robusta
    
    🛠️ HERRAMIENTAS DISPONIBLES:
    - Gestión de archivos y directorios
    - Lectura de contenido de archivos
    - Creación de notas estructuradas
    - Búsqueda de texto en múltiples archivos
    
    💡 EJERCICIOS SUGERIDOS:
    1. Lista los archivos en tu directorio actual
    2. Crea una nota sobre lo que has aprendido de MCP
    3. Busca algún texto específico en tus archivos
    4. Lee el contenido de un archivo de configuración
    
    ¡Empieza a experimentar con estas herramientas!
    """

if __name__ == "__main__":
    # Ejecutar el servidor
    mcp.run()
