
`nel-report-server`: NEL Reporting Server. For demo, it logs NEL level in stdout. However, in production, these events should be forwarded to stack like ELK, Splunk for processing.
`broswer-client`: A simple client server. Use to generate error in browser. It has two endpoints `test` which always return `200` and `/error` which return random error from `[400, 401, 403, 500, 502, 504]`


## SetUp

In Directory: `nel-report-server`

1. Start `nel-report-server`: `flask run --port 9000`
2. For exposing on trusted CA: `ngrok http 9000` (A browser can send NEL event on valid TLS endpoint only.)
3. Note the Ngrok URL. Something like `https://de34-49-207-197-21.in.ngrok.io`


In Directory: `broswer-client`

1. `export NEL_ENDPOINT="https://de34-49-207-197-21.in.ngrok.io/nel/report"`
2. Start `broswer-client`: `flask run --port 8000`
2. For exposing on trusted CA: `ngrok http 8000`
3. Note the Ngrok URL
3. Generate Errors `https://ngork_url/error`. Hit this URL from Browser


In `nel-report-server` logs, you will see that client side error has been reported by browser. For full set of errors: https://www.w3.org/TR/network-error-logging/#predefined-network-error-types
