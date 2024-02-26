FROM docker.io/jetpackio/devbox:latest
USER ${DEVBOX_USER}:${DEVBOX_USER}
WORKDIR /app
COPY --chown=${DEVBOX_USER}:${DEVBOX_USER} . .
RUN devbox run rye sync
