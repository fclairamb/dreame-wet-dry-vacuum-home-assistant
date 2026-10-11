# Changelog

## Unreleased — standalone dashboard release candidate

- Package existing Dreame device Lovelace card as a standalone HACS Dashboard candidate.
- Add an English-first explanatory README with Hebrew quick start and three labeled illustrative previews.
- Reuse the existing Dreame integration brand icon in the release package and project README (`icon.png`, `icon@2x.png`).
- Ship the existing model-aware visual editor and 3-tab user experience without changing supported integration entity mappings.
- Keep the dashboard JavaScript byte-for-byte identical to the development implementation.
- Run the existing JavaScript behavior tests from a standalone `dist/` layout.
- Do not tag or publish a release before integration compatibility and Home Assistant manual checks are complete.
