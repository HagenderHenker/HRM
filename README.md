# KomStAR

KomStAR ist ein Akronym, das für kommunales Stellen, Aufgaben und Ressourcenmanagementverfahren steht. Zweck der Software ist es , einer kleinen oder mittleren Kommune zu ermöglichen, die Stellenplanung, die Geschäftsverteilungsplanung und die Ressourcenzuordnung in einer Software zentralisiert auszuführen. Es sind noch diverse Erweiterungen geplant, die über dieses Grundverfahren hinausgehen. So ist geplant, in einer weiteren Ausbaustufe einen Beurteilungsmanager dieser Software beizufügen.

## Verwendete Open Source Produkte.

KomStAR ist eine Python basierte Webanwendung, die unter Zuhilfename des Django Web Framework erstellt worden ist . 

Die Software wurde so programmiert , dass sie grundsätzlich optimalerweise mit einer PostgreSQL Datenbank funktioniert. Für die Phase der Erstellung wurde mit SQLite gearbeitet. Diese Software kann auch weiterhin mit SQLite betrieben werden, wenn man das möchte. Aus Sicherheitsgründen wird empfohlen die Software innerhalb eines lokalen Netzwerks - abgeschottet vom bösen, weiten Internet, zu betreiben.

Die Third Party Apps , Die dieser Software zugrunde liegen , sind 
  -  Django-Tree-Beard
  -  Django-Tailwind-CLI
  -  Tailwind CSS-Framework und DaisyUI Komponenten
  -  HTMX.

## Aufbau der Software

Es wird die standardmäßige Django Architektur verwendet. 

Im Ordner "komstar" befinden sich die settings.py und die grundlegenden Dateien.
Es wurden folgende Apps angelegt:

- user
- personalstamm
- stellenplan
- orga
- core





