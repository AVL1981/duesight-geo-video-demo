# Overdracht

Bijgewerkt: 2026-11-14

## Stand

- De site staat live via GitHub Pages vanaf `main`: vier pagina's, de
  galerij en tien varianten.
- Alle 126 hashes in de 12 receipts kloppen (nagerekend op 2026-11-14).
- De ticket-werkwijze is toegevoegd: werkafspraken in `.claude/CLAUDE.md`,
  een issue-sjabloon en een GitHub Action die de receipts narekent.

## Laatste wijziging

Eerste inrichting van de werkwijze. Aan de site zelf is niets veranderd.

## Open punten voor de eigenaar

1. Het label `ready` aanmaken in de repo.
2. Op claude.ai/code/routines een geplande taak aanmaken met een
   GitHub-trigger op "issue gelabeld" met label `ready`, voor deze repo.
   De prompt staat in `.claude/CLAUDE.md` onder Tickets.
3. Beslissen hoe tickets over site-inhoud lopen. Nu geldt: Claude voert ze
   niet uit en meldt welke herbouw nodig is, omdat de builder niet in deze
   repo staat.

## Bekend

- `vendor/` (scripts en fonts) staat in geen enkele receipt, terwijl de
  README zegt dat de hashes over elk bestand gaan.
- Elke receipt waarschuwt dat witte CTA-tekst op de accentkleur de 4,5:1
  voor contrast niet haalt. De hoofdsite, de galerij en middernacht zitten
  op 3,68:1; de andere negen varianten lager, tot 1,53:1 bij signaal. De
  oplossing vraagt een herbouw; de uitwerking staat in issue #4.
- Er is geen preview per pull request, omdat de site op GitHub Pages staat.
