# KomStAR

Komstar ist ein Akronym , das für -k-ommunales -St-ellen , -A-ufgaben und -R-essourcenmanagementverfahren steht . Zweck der Software ist es , einer kleinen oder mittleren Kommune zu ermöglichen , die Stellenplanung. Die Geschäftsverteilungsplanung und die Ressourcenzuordnung in einer Software zentralisiert zu verwalten. Es sind noch diverse Erweiterungen geplant , die über dieses Grundverfahren hinausgehen. So ist geplant , in einer weiteren Ausbaustufe einen Beurteilungsmanager dieser Software beizufügen.

## Verwendete Open Source Produkte.

Komstar ist eine [Python](https://www.python.org/) basierte Webanwendung , die unter Zuhilfename des [Django-Web-Framework](https://www.djangoproject.com/) erstellt worden ist. 

Die Software wurde so programmiert, dass sie grundsätzlich optimalerweise mit einer PostgreSQL Datenbank funktioniert. Für die Phase der Erstellung wurde mit SQLite gearbeitet. Diese Software kann auch weiterhin mit SQLite betrieben werden, wenn man das möchte.

Die Third Party Apps, die dieser Software zugrunde liegen, sind [Django-Tree-Beard](https://django-treebeard.readthedocs.io/en/stable/), [HTMX](https://htmx.org/) und [SortableJS](https://sortablejs.github.io/Sortable/).

## Aufbau der Software

Es wird die standardmäßige Django Architektur verwendet. 

Im Ordner "komstar" befinden sich die settings.py und die grundlegenden Dateien.
im Ordner "static" werden Javascript, Tailwind, CSS und Bilddateien abgelegt.
Es wurden folgende Apps angelegt:
- user
- personalstamm
- stellenplan
- orga
- core --> utility



