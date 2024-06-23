# app.py
import os

import boto3
import jwt
from fastapi import FastAPI, HTTPException, Request
from mangum import Mangum
from starlette.responses import JSONResponse

app = FastAPI()

USER_POOL_ADMIN_GROUP_ID = os.environ.get("USER_POOL_ADMIN_GROUP_ID")
USER_POOL_ID = os.environ.get("USER_POOL_ID")


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    authorization_header = request.headers.get("Authorization")
    if not authorization_header:
        return JSONResponse(
            content={"error": "special-header missing"}, status_code=400
        )
    token = authorization_header.split(" ")[-1]
    decoded = jwt.decode(
        token, options={"verify_signature": False}
    )  # works in PyJWT >= v2.0
    cognito_client = boto3.client("cognito-idp")
    groups = cognito_client.admin_list_groups_for_user(
        UserPoolId=USER_POOL_ID, Username=decoded["cognito:username"]
    )
    for group in groups["Groups"]:
        if group["GroupName"] == "Administrators":
            request.scope["user"] = decoded
            return await call_next(request)
    return JSONResponse(content={"massage": "Permission denied"})


@app.get("/hello")
async def read_root(request: Request):
    return {"Hello": "Admin"}


handler = Mangum(app)
