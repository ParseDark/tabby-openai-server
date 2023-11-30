import logging
import os

from pydantic import ValidationError
from sanic import Sanic, Blueprint, Request
from sanic.response import json, empty

from src.completions import code_comp
from src.models import HealthResp, HealthVersion, EventReq, CompletionReq
from src.config import DEFAULT_LLM_MODEL

logger = logging.getLogger(__name__)

app = Sanic("tabby-openai-server")

v1 = Blueprint("v1", url_prefix="/v1")

app.blueprint(v1)


@v1.post("/completions", name="v1.completions")
async def completions(req: Request):
    try:
        req_data = CompletionReq.model_validate(req.json)
    except ValidationError as e:
        logger.error(f"post completions", exc_info=e, extra=req.json)

        return empty(status=400)
    else:
        resp_data = await code_comp(req_data)

        return json(resp_data.model_dump())


@v1.post("/events", name="v1.events")
async def events(req: Request):
    try:
        EventReq.model_validate(req.json)
    except ValidationError as e:
        logger.error(f"post events", exc_info=e, extra=req.json)

        return empty(status=400)
    else:
        return empty(status=200)


@v1.get("/health", name="v1.health")
async def health(_: Request):
    resp_data = HealthResp(
        model=os.getenv("model", DEFAULT_LLM_MODEL),
        device="",
        arch="",
        cpu_info="",
        cpu_count=0,
        cuda_devices=[],
        version=HealthVersion(
            build_date="", build_timestamp="", git_sha="", git_describe=""
        ),
    )

    return json(resp_data.json())
