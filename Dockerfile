# --- Builder ---
# specific Python 'slim' version
FROM python:3.12-slim as builder

WORKDIR /app
RUN python -m venv .venv
ENV PATH="/app/.venv/bin:$PATH"

# Python dependencies
COPY Egypt_Pharaoh_Hieroglyphs/requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
# rest of app source code
# current dir in project to work dir in image
COPY Egypt_Pharaoh_Hieroglyphs/. .

# --- Prod Image ---
# start from clean base image
FROM python:3.12-slim
WORKDIR /app

# non-root user
RUN useradd --create-home --shell /bin/bash appuser

# copy app code, set ownership
COPY --from=builder --chown=appuser:appuser /app/.venv ./.venv
COPY --from=builder --chown=appuser:appuser /app/src ./src
COPY --from=builder --chown=appuser:appuser /app/data ./data
COPY --from=builder --chown=appuser:appuser /app/dashboard ./dashboard
COPY --from=builder --chown=appuser:appuser /app/config ./config

# non-root user switch
USER appuser

# python virtual env default
ENV PATH="/app/.venv/bin:$PATH"

# container listens on Gunicorn port
EXPOSE 8000
# container default: apps WSGI server run
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "src.main:server"]