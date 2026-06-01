"""Sample runtime request packets built from display_core render plans."""

from __future__ import annotations

from typing import Any

from display_core import build_sample_view_model_render_plans_packet

from .earth_canvas import ContractOnlyEarthCanvasRuntimeAdapter
from .protocols import CanvasRuntimeRenderRequest
from .time_series_canvas import ContractOnlyTimeSeriesCanvasRuntimeAdapter


def build_sample_canvas_runtime_requests_packet() -> dict[str, Any]:
    render_plan_packet = build_sample_view_model_render_plans_packet()
    requests = []
    for plan in render_plan_packet["plans"]:
        request = CanvasRuntimeRenderRequest(
            canvas_type=plan["canvas_type"],
            view_model={
                "view_id": plan["view_id"],
                "canvas_type": plan["canvas_type"],
                "output_format": plan["output_format"],
            },
            render_plan=plan,
            runtime_options={
                "contract_only": True,
                "runtime_render_invoked": False,
            },
        )
        requests.append(request.to_packet())

    return {
        "schema": "rrkal_displaytools.sample_canvas_runtime_requests.v1",
        "source": "display_runtime.samples.build_sample_canvas_runtime_requests_packet",
        "status": "contract_ready",
        "request_schema": "rrkal_displaytools.canvas_runtime_render_request.v1",
        "render_plan_schema": render_plan_packet["schema"],
        "request_count": len(requests),
        "canvas_types": [request["canvas_type"] for request in requests],
        "requests": requests,
        "runtime_render_invoked": False,
        "boundary": "Samples bridge display_core render-plan metadata to display_runtime request packets without invoking renderer backends.",
    }


def build_sample_canvas_runtime_results_packet() -> dict[str, Any]:
    request_packet = build_sample_canvas_runtime_requests_packet()
    adapters = {
        "earth": ContractOnlyEarthCanvasRuntimeAdapter(),
        "time_series": ContractOnlyTimeSeriesCanvasRuntimeAdapter(),
    }
    results = []
    for request_data in request_packet["requests"]:
        request = CanvasRuntimeRenderRequest(
            canvas_type=request_data["canvas_type"],
            view_model=request_data["view_model"],
            render_plan=request_data["render_plan"],
            runtime_options=request_data["runtime_options"],
        )
        adapter = adapters[request.canvas_type]
        results.append(adapter.render(request).to_packet())

    return {
        "schema": "rrkal_displaytools.sample_canvas_runtime_results.v1",
        "source": "display_runtime.samples.build_sample_canvas_runtime_results_packet",
        "status": "contract_ready",
        "result_schema": "rrkal_displaytools.canvas_runtime_render_result.v1",
        "request_schema": request_packet["request_schema"],
        "result_count": len(results),
        "canvas_types": [result["canvas_type"] for result in results],
        "results": results,
        "runtime_render_invoked": any(result["runtime_render_invoked"] for result in results),
        "boundary": "Contract-only adapters return result packets without invoking renderer backends.",
    }
