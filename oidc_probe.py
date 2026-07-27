import base64, json, os, urllib.request
url = os.environ.get("ACTIONS_ID_TOKEN_REQUEST_URL")
tok = os.environ.get("ACTIONS_ID_TOKEN_REQUEST_TOKEN")
if not url or not tok:
    print("RESULT: NO_OIDC_ENV"); raise SystemExit(0)
req = urllib.request.Request(url + "&audience=h1-research-larocas",
                             headers={"Authorization": "bearer " + tok})
try:
    body = urllib.request.urlopen(req).read().decode()
except Exception as e:
    print("RESULT: MINT_BLOCKED", type(e).__name__, str(e)[:200])
    try: print("RESULT_BODY:", e.read().decode()[:300])
    except Exception: pass
    raise SystemExit(0)
t = json.loads(body)["value"]
p = t.split(".")[1]; p += "=" * (-len(p) % 4)
c = json.loads(base64.urlsafe_b64decode(p))
print("RESULT: MINTED")
print("SUB_CLAIM:", c.get("sub"))
print("AUD:", c.get("aud"))
print("REF:", c.get("ref"), "ENVIRONMENT:", c.get("environment"), "ACTOR:", c.get("actor"))
print("REPOSITORY:", c.get("repository"), "WORKFLOW_REF:", c.get("job_workflow_ref"))
