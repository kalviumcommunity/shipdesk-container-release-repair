# ShipDesk Container Release Repair

Modules 3-4 combined CA: three intentional faults, four practical tasks.
Tools: Git, Docker, Python 3.10+ on host, GitHub Actions; Bash/Git Bash commands.
No Python packages, registry push, GCP billing, credentials or deployment.

## Contract

app.py is correct and listens on 0.0.0.0:8000. Candidate image shipdesk:1.1.0.
Host endpoint http://127.0.0.1:8080. Inject APP_MODE=production at runtime.
/health -> {"status":"ok"}; /config ->
{"service":"ShipDesk","mode":"production","version":"1.1.0"}.
JSON whitespace/key order irrelevant. EXPOSE documents port; does not publish it.

Repair only Dockerfile COPY source, container port in launch.txt, and missing
validation dependency on release-review in .github/workflows/release.yml.
Complete readiness.md. Keep app, smoke checker, environment injection, host
loopback binding, workflow validation, permissions and triggers unchanged.
Review job only prints status, never deploys or enforces human approval.
Missing dependency may let it run early; a green job alone is not safe ordering.

## Work in your own fork

Fork, enable Actions if prompted, clone YOUR fork, switch to fix/shipdesk-release.
Commands run from repo root. Use python3 below; Windows Git Bash may use python.
Before timer: Docker operational, base image pre-pulled, host 8080 free, Actions
available, screenshot/PDF tools ready. Do not remove unrelated containers.

```sh
docker pull python:3.12-alpine
docker build -t shipdesk:1.1.0 .
# After Dockerfile repair, build again; execute supplied launch command:
sh launch.txt
docker logs shipdesk-ca34
docker port shipdesk-ca34
curl --max-time 3 http://127.0.0.1:8080/health
# Remove only this assessment container before rerun after mapping repair:
docker rm -f shipdesk-ca34
sh launch.txt
python3 scripts/smoke.py
curl --fail --max-time 3 http://127.0.0.1:8080/health
curl --fail --max-time 3 http://127.0.0.1:8080/config
docker inspect --format '{{.Image}}' shipdesk-ca34
```

Capture original build failure and original unreachable-host symptom, then
repair diffs and real passing results. No application changes needed.
Add validation dependency to review job, complete readiness.md using supplied
hypothetical incident, commit ALL four changed files and push branch. Inspect
your fork Actions run: validate must succeed before release-review starts.
Failed validate must block review. No fake failed-run evidence required.

Wait for final branch commit run to pass, then create annotated tag v1.1.0 at
that same commit and push tag. Workflow intentionally triggers branches only:
tag push does not create duplicate run. Compare tag target, local HEAD and
successful branch run commit. Git tag identifies source, not image provenance;
local image ID need not match runner image ID across machines/architectures.

Final PDF: four labelled task sections, genuine screenshots, author, public
fork/branch, commit, tag and successful run URL, cause/fix/result notes. No PR,
video, ZIP or actual cloud deployment. Follow accompanying assessment rubric.
Cleanup after evidence: docker rm -f shipdesk-ca34 (only your own container).
