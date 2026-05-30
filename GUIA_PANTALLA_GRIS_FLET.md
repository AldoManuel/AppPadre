# Guía: Cómo evitar la pantalla gris en Flet 0.85.x

## Causa raíz

Usar **`ft.View`** dentro de `page.add()` o anidado dentro de `ft.Container`.  
`ft.View` en Flet 0.85.x solo funciona correctamente con el sistema de enrutamiento `page.views.append()` / `page.go()`. Si se usa fuera de ese contexto, no se renderiza y muestra una pantalla gris.

---

## Solución: Reemplazar `ft.View` por `ft.Container`

### Paso 1 — Cambiar el tipo de retorno de cada vista

**Antes (pantalla gris):**

```python
def dashboard_view(page):
    return ft.View(
        controls=[
            ft.Column(
                [
                    # ... contenido ...
                ],
                spacing=0,
                scroll=ft.ScrollMode.AUTO,
            )
        ],
        padding=0,
        bgcolor=LIGHT_GRAY,
    )
```

**Después (funciona):**

```python
def dashboard_view(page):
    return ft.Container(
        content=ft.Column(
            [
                # ... mismo contenido ...
            ],
            spacing=0,
            scroll=ft.ScrollMode.AUTO,
        ),
        expand=True,
        bgcolor=LIGHT_GRAY,
    )
```

> **Nota:** `ft.View` envuelve sus `controls` en una lista. `ft.Container` usa `content` como propiedad única. El `ft.Column` de `controls` pasa a ser el `content` del `ft.Container`.

### Paso 2 — Cambiar el sistema de navegación

**Antes (con `ft.View` y `page.views.append`):**

```python
def switch_content(route):
    page.views.clear()
    page.views.append(ft.View(controls=[get_view(route)]))
    page.update()
```

**Después (container-swapping):**

```python
current_content = ft.Container(expand=True)

def switch_content(route):
    current_content.content = get_view(route)
    page.update()
```

Luego en el layout principal, usas `current_content` directamente:

```python
main_layout = ft.Column(
    [
        app_bar,
        ft.Container(
            content=current_content,
            expand=True,
            bgcolor=LIGHT_GRAY,
        ),
        nav_bar,
    ],
    spacing=0,
    expand=True,
)
```

### Paso 3 — Scroll vertical único

- El `ft.Column` exterior (el que está dentro del `ft.Container`) debe tener **exactamente un** `scroll=ft.ScrollMode.AUTO`.
- Ningún `Column` anidado debe tener `scroll` vertical (solo causa conflictos de scroll).
- Los `Row` horizontales pueden tener `scroll=ft.ScrollMode.AUTO` sin problema.

### Paso 4 — Verificar `expand`

- El `ft.Container` que envuelve cada vista debe tener `expand=True`.
- El layout principal (`ft.Column` o `ft.Stack`) también debe tener `expand=True`.

---

## Resumen de cambios por archivo

| Archivo | Cambio |
|---|---|
| `views/*_view.py` | `ft.View(...)` → `ft.Container(content=..., expand=True, bgcolor=...)` |
| `app.py` (o archivo principal) | Eliminar `page.views.append()`. Usar `container.content = nueva_vista` |
| `app.py` (layout) | Agregar `ft.Container(content=current_content, expand=True)` |

---

## Checklist rápida

- [ ] ¿Ninguna vista devuelve `ft.View`?
- [ ] ¿Cada vista devuelve `ft.Container` con `expand=True`?
- [ ] ¿El `ft.Column` exterior tiene `scroll=ft.ScrollMode.AUTO`?
- [ ] ¿Ningún `Column` anidado tiene scroll vertical?
- [ ] ¿El layout principal usa container-swapping en lugar de `page.views`?
