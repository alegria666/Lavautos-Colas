# Lavautos - Gestión de Vehículos

Este proyecto es una aplicación gráfica desarrollada en Python que permite gestionar los datos de un lavautos. 
Los vehículos se organizan y se "encolan" según su tipo, utilizando la estructura de datos 
*Colas*. El proyecto fue presentado como proyecto para la materia de **Estructuras de Datos**.

## Características
- Gestión de vehículos (dueño, placa, tipo).
- Organización de vehículos en una "cola lógica".
- Interfaz gráfica amigable usando **PyQt6**.
- Implementación de una Cola con Lista Simplemente Enlazada.

## Tecnologías Utilizadas
- **Python 3.10+**
- **PyQt6**: Para la interfaz gráfica de usuario.
- **Estructuras de Datos**: Implementación de Cola y Nodo con Lista Enlazada.

## Instrucciones de Instalación
1. Clona el repositorio o descarga el proyecto.
   ```bash
   git clone https://github.com/alegria666/Lavautos-Colas.git
   ```
2. Instala las dependencias necesarias.
   ```bash
   pip install PyQt6
   ```
3. Ejecuta la aplicación.
   ```bash
   python lavautos.py
   ```

## Uso
1. Inicia la aplicación ejecutando el archivo `lavautos.py`.
2. Ingresa los datos del vehículo (dueño, placa, tipo) en los campos correspondientes.
3. Observa cómo los vehículos se organizan en la cola lógica según su tipo.
4. Utiliza las funciones de la GUI para gestionar el flujo de vehículos.

## Estructura del Proyecto
```
Lavautos-Colas/
├── lavautos.py                    # Archivo principal
├── estructura/
│   └── secuenciales/
│       ├── cola.py               # Implementación de la Cola
│       └── __pycache__/          # Archivos compilados por Python
├── imagenes/                      # Recursos visuales
│   ├── acqua.png
│   ├── cola.png
│   ├── ingresar.png
│   ├── lista.png
│   ├── salida.png
│   └── welcome.png
```

## Créditos
- **Daniel Esteban Alegría Zamora** - Desarrollo, diseño e implementación de estructuras de datos.

## Notas
Este proyecto es una demostración académica y no está destinado para un uso en producción.
