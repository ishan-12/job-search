# Image for generating resume PDFs from Markdown (Node + headless Chromium).
#
# Built entirely from the OFFICIAL Alpine base image (pinned by digest) plus
# Alpine-signed apk packages — no third-party images to trust. This is the same
# Chromium engine the popular zenika/alpine-chrome image uses, but under our own
# control and provenance. (The Debian `chromium` package crashes with SIGTRAP on
# arm64, which is why we use Alpine's build.)
#
# The generator script and resumes are bind-mounted at runtime (docker-compose.yml),
# so this image only needs the runtime + browser + fonts.
FROM alpine:3.21@sha256:48b0309ca019d89d40f670aa1bc06e426dc0931948452e8491e3d65087abc07d

RUN apk add --no-cache \
      chromium \
      nodejs \
      font-carlito \
      font-liberation \
      ca-certificates

ENV CHROME_PATH=/usr/bin/chromium-browser
# HOME on the in-memory tmpfs so Chromium's stray writes work under a read-only root fs.
ENV HOME=/tmp
WORKDIR /work

ENTRYPOINT ["node", "tools/md-to-pdf.mjs"]
CMD ["--all"]
