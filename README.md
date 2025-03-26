# MCP Python SDK 
References
- https://modelcontextprotocol.io/introduction
- https://github.com/modelcontextprotocol/python-sdk
- 
Helpful community resources
- [Pamela Fox's live coding MCP session](https://www.youtube.com/watch?v=BXeCntNh6Mg)
- [Philipp Schmid's blog](https://www.philschmid.de/mcp-example-llama)
- [MCP in Production YouTube Video by Coding Crash Courses](https://www.youtube.com/watch?v=KRw4vVX9aHU) 

## MCP server sample
Notes of some hiccups running Anthropic's server sample:
### To run dev server
- With the command `mcp dev server.py`, you need to either 
  - name your server app `server.py`, or 
  - change the command to use your app file name (e.g. `mcp dev app.py`)
### To run the Inspector UI
- can't use Github Codespace out-of-the-box (probably need some container port forwarding and/or cross origin setups)
- need Node dependency (esp. `npx`) to run the MCP inspector UI
### To integrate with Desktop Claude
- Running `mcp install <server app file>` will make you use `uv`. You can edit the `claude_desktop_config.json` to change your command.
- Even you do use `uv`, you still need to edit the Claude Desktop config to change the `Command` from `uv` to the full path of where your `uv` is installed (e.g. `/Users/<username>/.local/bin/uv`), not sure if it's a Mac thing or Claude Desktop thing.
- The doc didn't mention it, but you need to restart Claude Desktop after adding or editing configs for your new MCP server 

## MCP client sample

### 
No hiccups here following the simplest stdio example.


## Thoughts
### Terminologies and Concept Shift
The "client, server, host" terminology triplet in the MCP doc can be pretty confusing to people with client-server application development expierences. To me, host is a machine, client is the application that interacts with the user, makes requests to the server application, and get response back to the user.

In the MCP world, however, the concept of them shifted. The general idea I got from Anthropic's MCP doc is that an **MCP host** is an application that interacts with the user, which typically has access to one LLM, and can manage multiple **MCP client**s. The MCP clients have 1:1 connection to **MCP server**s which provides tools, resources, prompts that can be used by an LLM application. 

To draw a comparison to the web application world:
- `MCP host` is your client application, with an LLM that can intelligently manage user interaction and server interaction to some extent so that you don't need to program every single logic
- `MCP client`s are the modules your application holds to connect to multiple microservices
- `MCP server`s are each microservice's backend. They might be a collection of tools, or connected to a database, a file system, an external API, or other services.

If you follow Anthropic's example with Claude Desktop, things might get more confusing. Claud Desktop basically act as all of the three: 
- First, it is a `host` application with a chat UI and access to the Claude LLM
- Secondly, it can run multiple `clients` internally to connect to the MCP servers, one for each MCP server 
- Thirdly, once you installed your MCP server (either by running `mcp install server.py` or adding your MCP server in Claude Desktop's Developer config), and restart, Claude Desktop will also run the servers locally (or in a Docker, depending on your configuration) for you.

### Production Readiness

#### Local

When installing my MCP server with Claude Desktop, I had to use an absolute path to my server app file. 

After that I've rename the file, moved it to another folder. With Claude Desktop still open, it could still use the tool but showed "local" in brackets. Then I restarted Claud Desktop, now it showed "failed" in the Developer Settings and asking about BMI no longer uses the tool.

So, Claude Desktop keeps a local cache of the MCP server while it is open, and every restart the cache will be flushed and Claude Desktop will try to reload the MCP server file from disk and run it. 

This is extremely fragile and I guess the production ready way of shipping a MCP local server is to package it in a container and instead of letting Claude Desktop or other MCP clients run the server app file directly, instruct them to run the MCP server in a Docker container.

#### Remote

The MCP specification defined two Transport mechanisms: `stdio` and `sse` (server-sent event, for streaming over HTTP). 

All the MCP server and client samples I've found are for local use only. Remote connections with authorization is still draft in the MCP protocol but Cloudflare has some docs about remote MCP servers.
