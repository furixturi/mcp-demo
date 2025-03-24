# Walkthrough MCP Python SDK 
## Hiccup notes
### To run dev server
- With the command `mcp dev server.py`, you need to either 
  - name your server app `server.py`, or 
  - change the command to use your app file name (e.g. `mcp dev app.py`)
### To run the Inspector UI
- can't use Github Codespace out-of-the-box (probably need some container port forwarding and/or cross origin setups)
- need Node dependency (esp. `npx`) to run the MCP inspector UI
### To integrate with Desktop Claude
- have to use `uv`
- after `mcp install app.py`, need to edit the Claude Desktop config and change the `Command` from `uv` to the full path of it (e.g. `/Users/<username>/.local/bin/uv`)
- then need to restart Claude Desktop