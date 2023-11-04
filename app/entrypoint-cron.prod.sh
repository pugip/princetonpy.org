#!/bin/sh

if [ -n "$UID" ] && [ -n "$GID" ]; then
    usermod -u "$UID" app
    groupmod -g "$GID" app
    chown -R "$UID":"$GID" "$HOME"
fi

exec "$@"
