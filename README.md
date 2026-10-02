# Ammonia Loading Process Study

**Status: conceptual study framework and a geometric calculation example.**

The first deliverable is a transparent estimate of the internal volume of straight pipe sections and their hypothetical liquid inventory. It is a starting point for documenting engineering assumptions, not a loading-system design or an operating procedure.

## Run the educational example

Run `python geometry.py` (Python 3.10+; standard library only). Inputs are in `example-input.json`. Diameters are **internal diameters in metres**, not nominal pipe sizes. Length is per line. Density is an explicit supplied assumption, not an ammonia property prediction.

For each section: volume = π × internal diameter² × length × number of lines / 4. Hypothetical inventory = volume × supplied density. The example assumes straight circular pipes with no fittings or equipment holdup and fully filled liquid volume.

## Included

- `geometry.py`: input validation, SI units and a section-level breakdown.
- `example-input.json`: invented example with no employer or project data.
- `study-basis.md`: questions and evidence needed for a future complete study.

## Scope limits

No pressure drop, vapor-liquid equilibrium, pump sizing, cooldown, displacement, relief sizing or safe loading rate is calculated. The example density does not establish a thermodynamic state. Ammonia is hazardous: this material cannot define field settings, equipment selection or work authorization. A real study requires verified properties, engineering review and site-specific procedures.

## Español

Ejemplo geométrico y bases de estudio para un portafolio académico. Usa diámetro interior real y unidades SI. No contiene condiciones de operación ni documentación de una instalación real. Los datos son inventados.
