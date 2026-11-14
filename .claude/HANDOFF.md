# Overdracht

Bijgewerkt: 2026-11-14

## Stand

- De site staat live via GitHub Pages vanaf `main`: vier pagina's, de
  galerij en tien varianten.
- Alle 126 hashes in de 12 receipts kloppen (nagerekend op 2026-11-14).
- De ticket-werkwijze draait: het label `ready` bestaat en de geplande taak
  "Tickets duesight-geo-video-demo" kijkt om de twee uur (07:43 tot 21:43
  Nederlandse tijd) naar open issues met dat label. De werkafspraken staan
  in `.claude/CLAUDE.md`; een GitHub Action rekent de receipts na.

## Laatste wijziging

Issue #2: de werkafspraken onder Tickets beschrijven nu de tweeuurlijkse
ronde en de labels `ready` en `bezig`, en verwijzen voor de prompt naar de
geplande taak. Aan de site zelf is niets veranderd.

## Open punten voor de eigenaar

1. Beslissen hoe tickets over site-inhoud lopen. Nu geldt: Claude voert ze
   niet uit en meldt welke herbouw nodig is, omdat de builder niet in deze
   repo staat.

## Bekend

- `vendor/` (scripts en fonts) staat in geen enkele receipt, terwijl de
  README zegt dat de hashes over elk bestand gaan.
- Elke receipt meldt dezelfde waarschuwing: witte CTA-tekst op de accentkleur
  haalt 3,68:1 en niet de 4,5:1 voor contrast.
- Er is geen preview per pull request, omdat de site op GitHub Pages staat.
