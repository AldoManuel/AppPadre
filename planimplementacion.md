Actúa como un desarrollador Senior especializado en aplicaciones móviles modernas utilizando Flet 0.85.2 y Python.

Necesito que generes el PLAN DE IMPLEMENTACIÓN COMPLETO junto con el CASCARÓN VISUAL (SIN FUNCIONALIDAD REAL) de una aplicación móvil educativa llamada:

"Sistema de Seguimiento de Tareas Escolares - App Padres de Familia"

La aplicación forma parte de un ecosistema multiplataforma compuesto por:

* Sistema Web Administrativo
* Aplicación móvil para Docentes
* Aplicación móvil para Padres de Familia

====================================================
OBJETIVO GENERAL

Desarrollar una aplicación móvil moderna, profesional y responsive enfocada en padres de familia para el monitoreo académico de sus hijos.

La aplicación debe permitir VISUALMENTE:

* Consultar tareas escolares
* Consultar asistencia
* Consultar puntualidad
* Consultar eventos escolares
* Consultar progreso académico
* Recibir notificaciones escolares

IMPORTANTE:

* NO implementar backend.
* NO conectar Supabase.
* NO consumir APIs reales.
* NO implementar autenticación funcional.
* SOLO generar frontend visual.
* Utilizar datos ficticios simulados.
* Preparar la aplicación para futura escalabilidad.

====================================================
VERSIÓN OBLIGATORIA DE FLET

Utilizar exclusivamente:

* Flet 0.85.2
* Python 3.12+

IMPORTANTE:

* Utilizar únicamente componentes compatibles con Flet 0.85.2
* NO utilizar componentes obsoletos
* NO utilizar código deprecated
* Aplicar buenas prácticas modernas de Flet

====================================================
PLAN DE IMPLEMENTACIÓN

Generar el proyecto dividido por etapas:

ETAPA 1 — Configuración del Proyecto

* Crear estructura modular profesional
* Configurar navegación principal
* Configurar tema global
* Configurar sistema responsive
* Configurar paleta de colores

ETAPA 2 — Diseño Base

* Crear Login responsive
* Crear Dashboard principal
* Crear navegación inferior
* Crear AppBar moderna
* Crear menú lateral adaptable

ETAPA 3 — Módulos Académicos

* Vista de tareas
* Vista de asistencia
* Vista de puntualidad
* Vista de eventos
* Vista de progreso académico

ETAPA 4 — Sistema Visual

* Notificaciones simuladas
* Cards reutilizables
* Widgets responsivos
* Gráficas simuladas
* Estados visuales

ETAPA 5 — Optimización Responsive

* Adaptación móvil
* Adaptación tablet
* Orientación vertical/horizontal
* Optimización de tamaños
* Scroll dinámico

====================================================
TECNOLOGÍAS OBLIGATORIAS

Utilizar:

* Python
* Flet 0.85.2

Componentes modernos de Flet:

* ft.View
* ft.Container
* ft.Card
* ft.ListView
* ft.GridView
* ft.ResponsiveRow
* ft.NavigationBar
* ft.NavigationDrawer
* ft.AppBar
* ft.BottomAppBar
* ft.Tabs
* ft.AlertDialog
* ft.SnackBar
* ft.NavigationRail
* ft.Stack
* ft.Column
* ft.Row

====================================================
DISEÑO VISUAL

Inspirarse visualmente en:

* Google Classroom
* Microsoft Teams
* Material Design 3
* Aplicaciones educativas modernas

====================================================
PALETA DE COLORES

Utilizar exactamente la misma línea visual del sistema web administrativo:

COLORES PRINCIPALES:

* Azul educativo → #2563EB
* Verde académico → #10B981
* Blanco → #FFFFFF
* Gris claro → #F3F4F6
* Gris oscuro → #1F2937

Características visuales:

* Bordes redondeados
* Sombras suaves
* Diseño minimalista
* Cards modernas
* Espaciado uniforme
* Íconos modernos
* Diseño limpio
* Tipografía moderna
* Animaciones suaves

====================================================
RESPONSIVE DESIGN

La aplicación DEBE adaptarse correctamente a:

* Smartphones pequeños
* Smartphones medianos
* Smartphones grandes
* Tablets Android
* iPad
* Orientación vertical
* Orientación horizontal

IMPORTANTE:

* Utilizar page.window.width
* Utilizar page.window.height
* Adaptar tamaños dinámicamente
* Evitar medidas fijas
* Utilizar expand=True correctamente
* Implementar scroll automático
* Mantener diseño móvil realista

Compatibilidad mínima:

* 360x640
* 390x844
* 412x915
* Tablets Android
* iPad

====================================================
ESTRUCTURA DEL PROYECTO

Generar estructura profesional:

/project
│
├── main.py
├── app.py
│
├── /views
│   ├── login_view.py
│   ├── dashboard_view.py
│   ├── tareas_view.py
│   ├── asistencia_view.py
│   ├── puntualidad_view.py
│   ├── eventos_view.py
│   ├── progreso_view.py
│   └── notificaciones_view.py
│
├── /components
│   ├── appbar.py
│   ├── navbar.py
│   ├── cards.py
│   ├── dialogs.py
│   ├── widgets.py
│   └── charts.py
│
├── /styles
│   ├── colors.py
│   ├── theme.py
│   └── responsive.py
│
├── /assets
│   ├── /images
│   └── /icons
│
└── requirements.txt

====================================================
PANTALLAS PRINCIPALES

1. LOGIN PADRES

Debe incluir:

* Logo institucional
* Inputs modernos
* Botón de acceso
* Fondo moderno
* Responsive
* Animaciones suaves
* Validaciones visuales simuladas

====================================================
2. DASHBOARD PRINCIPAL

Debe incluir:

* AppBar moderna
* NavigationBar inferior
* Tarjetas académicas
* Resumen del alumno
* Actividad reciente
* Notificaciones rápidas
* Eventos próximos
* Accesos rápidos

====================================================
3. MÓDULO TAREAS

Debe incluir:

* Lista de tareas
* Cards modernas
* Estados:

  * Pendiente
  * Entregada
  * Retrasada
* Diseño responsive
* Filtros visuales

====================================================
4. MÓDULO ASISTENCIA

Debe incluir:

* Historial de asistencia
* Indicadores visuales
* Porcentaje de asistencia
* Estados:

  * Presente
  * Ausente
  * Retardo

====================================================
5. MÓDULO PUNTUALIDAD

Debe incluir:

* Indicadores visuales
* Estadísticas simuladas
* Historial de puntualidad
* Gráficas simuladas

====================================================
6. MÓDULO EVENTOS

Debe incluir:

* Eventos escolares
* Cards informativas
* Fechas importantes
* Eventos destacados

====================================================
7. PANEL DE PROGRESO

Debe incluir:

* Progreso académico visual
* Estadísticas simuladas
* Rendimiento escolar
* Gráficas simuladas
* Indicadores de cumplimiento

====================================================
8. NOTIFICACIONES

Debe incluir:

* Alertas escolares
* Lista moderna
* Indicadores leídos/no leídos
* Tarjetas tipo mensaje

====================================================
REQUERIMIENTOS TÉCNICOS

* Código limpio y modular
* Componentes reutilizables
* Arquitectura preparada para MVC/MVVM
* Preparado para Supabase
* Navegación fluida
* Uso correcto de ResponsiveRow
* Uso correcto de expand=True
* Optimización visual móvil
* Implementar tema claro/oscuro visual
* Comentarios explicativos en el código

====================================================
SIMULACIONES VISUALES

Implementar únicamente simulaciones:

* Navegación visual
* Datos ficticios
* Alertas visuales
* Modales falsos
* Tabs
* Gráficas simuladas
* Cambios de pantalla
* Estados dinámicos simulados

NO implementar lógica real.


====================================================
OBJETIVO FINAL

El resultado debe parecer una aplicación móvil educativa profesional lista para producción, similar a Google Classroom o Microsoft Teams para padres de familia, aunque todavía sin funcionalidades reales.

La aplicación debe verse moderna, elegante, organizada, escalable y completamente responsive para dispositivos móviles actuales utilizando Flet 0.85.2.
