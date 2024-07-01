# fifa_tool
![Imagen de la aplicación](/image/inicio.jpeg)

## Descripción

**Football Metrics Search App** es una aplicación interactiva construida con Streamlit y Python, que permite a los usuarios buscar y visualizar métricas y perfiles de jugadores de fútbol. Los usuarios pueden buscar jugadores por nacionalidad, equipo y si están en el equipo nacional de su país.

![Imagen de equipo](/image/equipo.jpeg)
## Características

- **Búsqueda por Nacionalidad**: Encuentra jugadores de una nacionalidad específica.
- **Búsqueda por Equipo**: Filtra jugadores que pertenecen a un equipo determinado.
- **Búsqueda por Participación en el Equipo Nacional**: Identifica jugadores que son miembros del equipo nacional de su país.
- **Visualización de Métricas**: Muestra las estadísticas y métricas clave de los jugadores.

## Instalación

Para ejecutar esta aplicación en tu máquina local, sigue estos pasos:

1. **Clona el repositorio**:
   ```sh
   git clone https://github.com/tu_usuario/football-metrics-search-app.git
   cd football-metrics-search-app
   ```

2. **Crea un entorno virtual** (opcional pero recomendado):
   ```sh
   python -m venv env
   source env/bin/activate  # En Windows usa `env\Scripts\activate`
   ```

3. **Instala las dependencias**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Ejecuta la aplicación**:
   ```sh
   streamlit run app.py
   ```

## Uso

1. **Inicia la aplicación**: Ejecuta el comando `streamlit run app.py` en tu terminal.
2. **Interfaz de Usuario**: 
    - Selecciona la nacionalidad de los jugadores que deseas buscar.
    - Selecciona el equipo para filtrar jugadores por equipo.
    - Marca la opción si deseas buscar jugadores que están en el equipo nacional de su país.
3. **Resultados**: La aplicación mostrará una tabla con las métricas y perfiles de los jugadores que coinciden con los criterios de búsqueda.

## Estructura del Proyecto

```
football-metrics-search-app/
│
├── fifa_tool.py                   # Archivo principal de la aplicación Streamlit
├── fifa_code.ipynb         # Lista de dependencias necesarias
├── datos/                   # Carpeta para almacenar datos de jugadores (opcional)
│   └── Fifa 23 Players Data.csv     # Archivo CSV con datos de jugadores
└── README.md                # Este archivo
```


![Imagen de equipo](/image/venezuela_jugador.jpeg)