# ✅ TaskFlow — Sistema de Gestión de Tareas

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Django](https://img.shields.io/badge/Django-4.2-green?logo=django)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple?logo=bootstrap)
![License](https://img.shields.io/badge/License-MIT-yellow)

Aplicación web de gestión de tareas personal desarrollada con **Django** y **Bootstrap 5**. Permite a los usuarios registrarse, autenticarse y gestionar sus tareas con diferentes niveles de prioridad, estados y categorías personalizadas.

---

## 🚀 Características

- 🔐 **Autenticación completa** — Registro, login y logout de usuarios
- ✅ **CRUD de tareas** — Crear, leer, actualizar y eliminar tareas
- 🏷️ **Categorías personalizadas** — Organiza tus tareas con colores
- 🔍 **Búsqueda y filtros** — Filtra por estado, prioridad y categoría
- 📊 **Dashboard con estadísticas** — Resumen visual de tus tareas
- 📱 **Diseño responsive** — Adaptado para móvil, tablet y escritorio
- 🌗 **UI moderna** — Sidebar, tarjetas con prioridad visual, badges

---

## 🛠️ Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| **Python 3.10+** | Lenguaje de programación principal |
| **Django 4.2** | Framework web backend (MVT) |
| **SQLite** | Base de datos (incluida con Django) |
| **Bootstrap 5.3** | Framework CSS frontend |
| **Bootstrap Icons** | Íconos vectoriales |
| **JavaScript** | Interactividad del sidebar en mobile |
| **HTML5 + CSS3** | Estructura y estilos personalizados |

---

## 📁 Estructura del Proyecto

```
taskflow/
├── manage.py
├── requirements.txt
├── db.sqlite3               # Se genera al ejecutar migraciones
├── taskflow_project/        # Configuración principal
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── tasks/                   # App principal
│   ├── models.py            # Task, Category
│   ├── views.py             # Lógica de negocio
│   ├── forms.py             # Formularios Django
│   ├── urls.py              # Rutas de la app
│   └── templates/tasks/     # Templates HTML
├── templates/               # Templates globales
│   ├── base.html            # Layout principal
│   └── registration/        # Login y registro
└── static/                  # Archivos estáticos
```

---

## ⚙️ Instalación y ejecución

### Requisitos previos
- Python 3.10 o superior
- pip

### Pasos

```bash
# 1. Clonar el repositorio
git clone https://github.com/TU_USUARIO/taskflow.git
cd taskflow

# 2. Crear entorno virtual
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Aplicar migraciones
python manage.py makemigrations
python manage.py migrate

# 5. Crear superusuario (opcional)
python manage.py createsuperuser

# 6. Ejecutar el servidor
python manage.py runserver
```

### Acceder a la aplicación
Abre tu navegador en: **http://127.0.0.1:8000**

---

## 📸 Capturas de pantalla

> Las capturas de pantalla se encuentran en el documento PDF de la actividad evaluativa.

---

## 🗂️ Modelos de datos

### Task (Tarea)
| Campo | Tipo | Descripción |
|---|---|---|
| title | CharField | Título de la tarea |
| description | TextField | Descripción detallada |
| priority | CharField | Baja / Media / Alta |
| status | CharField | Pendiente / En Progreso / Completada |
| due_date | DateField | Fecha límite |
| category | ForeignKey | Categoría asignada |
| user | ForeignKey | Usuario propietario |

### Category (Categoría)
| Campo | Tipo | Descripción |
|---|---|---|
| name | CharField | Nombre de la categoría |
| color | CharField | Color hexadecimal |
| user | ForeignKey | Usuario propietario |

---

## 📚 Referencias

- Django Software Foundation. (2024). *Django documentation*. https://docs.djangoproject.com/
- Bootstrap Team. (2024). *Bootstrap 5 documentation*. https://getbootstrap.com/docs/5.3/
- Mozilla Developer Network. (2024). *Web technology for developers*. https://developer.mozilla.org/

---

## 👨‍💻 Autor

Desarrollado como actividad evaluativa del Eje 1 — Fundación Universitaria del Área Andina (AREANDINA).

---

## 📄 Licencia

MIT License — libre para uso académico.
