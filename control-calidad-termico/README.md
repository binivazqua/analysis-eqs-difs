# Control de Calidad — Tratamiento Térmico de Piezas Mecánicas

Modelación del enfriamiento de una pieza de acero (Ley de Enfriamiento de Newton) para determinar el coeficiente de enfriamiento **k** y predecir el tiempo en que la pieza alcanza una temperatura segura de trabajo (27 °C), a partir de datos registrados por pirómetro óptico durante los primeros 20 minutos.

## Estructura del repositorio

```
control-calidad-termico/
├── documentation/   # Situación problema, datos registrados, notas y referencias
├── analysis/        # Scripts de Python: regresión lineal, cálculo de k, EDO
├── output/          # Gráficas y PDF final
└── report/          # Fuente LaTeX del reporte
```

- **documentation/** — enunciado del problema, tabla de datos registrados (pirómetro), bitácora de supuestos.
- **analysis/** — código de análisis: transformación ln(T−T_amb), regresión lineal para obtener k, solución de la EDO.
- **output/** — gráficas generadas y `reporte_control_calidad_termico.pdf` listo para entregar.
- **report/** — fuente LaTeX, logo y artefactos de compilación (ignorados por Git).

## Cómo colaborar en el reporte (report/main.tex)

### 1. Bajar los últimos cambios

```bash
git pull origin main
```

### 2. Compilar el LaTeX (local)

Requiere TeX Live con `latexmk` y `pdflatex`:

```bash
cd control-calidad-termico/report
latexmk -pdf -outdir=build main.tex
```

El PDF queda en `report/build/main.pdf`. Para limpiar los temporales: `latexmk -C -outdir=build`.

> Si no quieres instalar nada: el repo compila solo. Cada push a `main` dispara un GitHub Action que compila el reporte y deja el PDF actualizado — funciona como un Overleaf casero (ver sección abajo).

### 3. Flujo de trabajo para editar main.tex

Los artefactos de compilación ya están ignorados por Git (`report/.gitignore`); solo se versionan `main.tex` y `logo tec.png`. Para evitar conflictos:

```bash
# Antes de editar, siempre
git pull origin main

# Al terminar tus cambios
git add main.tex
git commit -m "report: <qué editaste>"
git push origin main
```

Tips:
- Edita secciones distintas entre integrantes cuando sea posible; si dos tocan la misma sección, avisen en el chat del equipo antes de hacer push.
- Si `git push` rechaza, es porque alguien subió cambios primero: `git pull --rebase origin main`, resuelve conflictos si los hay, y vuelve a intentar el push.
- Verifica que compila **antes** de hacer push (opción A o B).

## Overleaf casero (GitHub Actions)

No necesitamos Overleaf: el repo compila el reporte automáticamente.

- **Editar:** puedes modificar `report/main.tex` desde la web de GitHub (abre el archivo → lápiz → commit) o desde tu clon local como siempre.
- **Compilar:** cada push a `main` que toque `report/` dispara el workflow [`.github/workflows/compile-report.yml`](../../.github/workflows/compile-report.yml), que corre `latexmk` en la nube y sube el PDF como **artifact** de la ejecución.
- **Descargar el PDF:** pestaña **Actions** del repo → clic en la ejecución más reciente (✓ verde) → sección **Artifacts** → `reporte`. El PDF más reciente entregable siempre vive ahí.

## Datos base

Temperatura ambiente: 18 °C
Rango de datos: 97 °C → ~20 °C, en intervalos de 1 min durante 20 min.

Ver `documentation/datos_registrados.csv`.

## Equipo

Biniza Verónica Vázquez Moreno | A01737294
Joaquín Rosales González | A01771481
Flor Denisse Hinojosa Hernández | A00843678
