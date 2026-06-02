from __future__ import annotations


def build_prepare_batch_cache_evidence(
    *,
    source: str,
    entries: int,
    limit: int,
    hits: int,
    misses: int,
    deferred: int,
    dirty_flags: dict[str, object],
    prepare_phase: str,
) -> dict[str, object]:
    return {
        "schema": "rrkal_displaytools.prepare_batch_cache_evidence.v1",
        "source": source,
        "status": "evidence_only",
        "entries": int(entries),
        "limit": int(limit),
        "hits": int(hits),
        "misses": int(misses),
        "deferred": int(deferred),
        "dirty_flags": dirty_flags,
        "prepare_phase": prepare_phase,
        "recommended_next_action": "measure_static_batch_reuse_candidate",
        "runtime_optimization_applied": False,
        "boundary": "Evidence packet only; does not decide cache reuse, read or write overlay arrays, mutate dirty flags, render frames, change metadata schema, or enable runtime merge.",
    }
