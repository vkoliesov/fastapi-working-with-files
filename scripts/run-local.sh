#!/bin/bash

set -o errexit
set -o nounset

# apply alembic migrations
alembic upgrade head

# run server
uvicorn main:app --host 0.0.0.0 --port 8000 --log-level info --reload --workers 4