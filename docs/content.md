# Content rules

## Sources of truth

Every claim on the site comes from the chain repository at the revision in `src/site.json` (`revision`, `manifest`, `revision_date`). The main sources are the chain's `docs/` tree (architecture, protocol reference, decisions, security, operations), `configs/`, `internal/blockchain/protocol_manifest.go` and the user stories. When the chain moves, update `src/site.json` and re-check every number on the affected pages.

## Status badges

| Badge | Meaning |
| --- | --- |
| Implemented | In the reference implementation and tested |
| Experimental | In the implementation, behind an interlock, not for value |
| Proposed | Design or prototype only |
| Historical | True of an earlier revision |
| Internal | First-party evidence, not an external certification |
| Not implemented | Absent today |

## Rules

- Say what is true now and label what is not done. Prefer "measured" and "target" over promises.
- Wall-clock conversions are labelled "at the 2 s target"; block counts are the binding rule.
- Internal reviews are never called audits. Results qualify only the revision they ran on.
- Security findings: publish posture (counts, areas, whether they block a milestone) until fixes ship; publish details afterwards.
- No token, price or allocation language beyond "RSC is the protocol's native unit". No dates for launches.
- The chain repository is private: show file paths as `<code class="src">` text, never as links. When it becomes public, these can be turned into links in one pass.
