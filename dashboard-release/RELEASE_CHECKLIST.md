# Release gate — Dreame Dashboard

- [x] Standalone `dist/dreame-device-card.js` copied unchanged from active development branch
- [x] Card-specific HACS manifest and root README prepared
- [x] Three **illustrative** visual previews included and explicitly labeled
- [x] English documentation and Hebrew quick start
- [x] Independent node test path prepared
- [ ] Card-only CI passes for the committed candidate
- [ ] Real Home Assistant browser / iOS layout and scroll tested
- [ ] H14 and H15 device selection tested on physical installations
- [ ] Safe commands and all maintenance confirmation flows tested with a real device
- [ ] Replace illustration previews with consented and redacted real screenshots, if available
- [ ] Create dedicated public repository named `dreame-device-card` (not supported by current GitHub connector actions)
- [ ] Copy *contents* of this folder to that repository **root**; do not copy the parent folder
- [ ] Configure repository description, license, topics and enable Issues
- [ ] Run HACS validation for **Dashboard** in the new root repository
- [ ] Tag/version and GitHub release after acceptance — deliberately not done yet
- [ ] Optional: request HACS default-list inclusion after release review

Do not remove the current `www/` source copy while the integration is under development. Do not release the integration or the XPENG project as part of this workflow.
