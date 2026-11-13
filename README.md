::: {align="center"}
# 🖥️ LocalPort

### Find open ports. Identify local services. Debug your development environment.

A lightweight Windows command-line tool that lists listening network
ports, shows the local IP address and identifies the process using each
port. Quickly check whether a development server appears to be running
before opening its `localhost` URL in your browser.

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?logo=windows&logoColor=white)](https://www.microsoft.com/windows)
[![Dependency](https://img.shields.io/badge/Dependency-psutil-4B8BBE)](https://pypi.org/project/psutil/)
[![License:
MIT](https://img.shields.io/badge/License-MIT-2ea44f)](LICENSE)

[Features](#-features) · [Installation](#-installation) ·
[Usage](#-usage) · [How-it-works](#-how-it-works) ·
[Troubleshooting](#-troubleshooting) · [Contributing](#-contributing)
:::

------------------------------------------------------------------------

## 🎯 Why LocalPort?

During development, it is common to run several local services at the
same time:

-   Next.js or React development servers (`3000`, `5173`)
-   Node.js or Python backends (`5000`, `8000`)
-   Databases such as MySQL (`3306`) or PostgreSQL (`5432`)
-   Other tools that start local web servers

Sometimes a browser tab at `http://localhost:3000` stops responding, or
a new project cannot start because the port is already in use.

LocalPort gives you a quick view of the ports currently in the
**LISTEN** state and the process associated with each one. Use the port
number to identify the service you expect to be running.

> **Important:** LocalPort lists listening ports. It does not open a
> browser, send an HTTP request, or guarantee that a web page is
> healthy. A listening port is a useful indication that a service is
> accepting connections; open the matching `localhost` URL to check the
> application itself.

## ✨ Features

```{=html}
<table>
```
```{=html}
<tr>
```
```{=html}
<td width="50%" valign="top">
```
### 🔎 Open-port listing

Shows TCP/UDP internet endpoints that are in the `LISTEN` state.

```{=html}
</td>
```
```{=html}
<td width="50%" valign="top">
```
### 🧩 Process identification

Displays the process name and port, helping you find which application
is using a port.

```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td width="50%" valign="top">
```
### 🏠 Localhost visibility

Shows loopback addresses such as `127.0.0.1` and `::1`, as well as
wildcard listening addresses.

```{=html}
</td>
```
```{=html}
<td width="50%" valign="top">
```
### ⚡ One-command launch

After the optional PATH setup, run `ports` from any directory or VS Code
terminal.

```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
</table>
```
## 🚀 Installation

### Requirements

-   Windows 10 or Windows 11
-   Python installed and available as `py` or `python`
-   PowerShell or Command Prompt

### 1. Get the project

Clone the repository or download the source files, then open a terminal
in the project folder.

``` powershell
git clone https://github.com/YOUR_USERNAME/LocalPort.git
cd LocalPort
```

Replace the example repository URL with the actual repository URL after
publishing your project.

### 2. Install the dependency

``` powershell
py -m pip install psutil
```

### 3. Run the script

``` powershell
py ports.py
```

If your system uses `python` instead of `py`, run:

``` powershell
python ports.py
```

## 💻 Usage

Run the script from its folder:

``` powershell
py ports.py
```

Example output:

``` text
=== RUNNING LOCALHOST & OPEN PORTS ===

127.0.0.1            PORT: 3000   PROCESS: node.exe
127.0.0.1            PORT: 8000   PROCESS: python.exe
0.0.0.0              PORT: 5000   PROCESS: python.exe
::1                  PORT: 5432   PROCESS: postgres.exe

=== SCAN COMPLETED ===
```

The output above is an example; the ports and processes on your computer
will be different.

### Run it from anywhere with `ports`

You can make the script available as a global Windows command.

1.  Place `ports.py` and `ports.cmd` in a folder, for example:

    ``` text
    E:\CODER\Tools\
    ```

2.  Create `ports.cmd` in that folder with:

    ``` bat
    @echo off
    py "E:\CODER\Tools\ports.py" %*
    ```

3.  Add `E:\CODER\Tools` to your **User PATH**.

    In PowerShell:

    ``` powershell
    $userPath = [Environment]::GetEnvironmentVariable("Path", "User")

    if (($userPath -split ';') -notcontains 'E:\CODER\Tools') {
        [Environment]::SetEnvironmentVariable(
            "Path",
            (($userPath.TrimEnd(';') + ';E:\CODER\Tools').Trim(';')),
            "User"
        )
    }
    ```

4.  Close and reopen your terminal (and VS Code, if it was already
    open).

5.  Run this from any directory:

    ``` powershell
    ports
    ```

If Windows cannot find `py`, edit `ports.cmd` and replace `py` with
`python`.

## 🔄 How it works

1.  LocalPort asks `psutil` for internet network connections.
2.  It keeps entries whose status is `LISTEN`.
3.  It reads each entry's local IP address, port number and process ID.
4.  It looks up the process name and prints the results.

### Understanding the addresses

  -----------------------------------------------------------------------
  Address                             Meaning
  ----------------------------------- -----------------------------------
  `127.0.0.1`                         IPv4 loopback; the service listens
                                      on this computer only.

  `::1`                               IPv6 loopback; the service listens
                                      on this computer only.

  `0.0.0.0`                           Wildcard IPv4 address; the service
                                      listens on all IPv4 interfaces.

  `::`                                Wildcard IPv6 address; the service
                                      listens on all IPv6 interfaces.
  -----------------------------------------------------------------------

### Checking your local development project

For example, if your project normally runs at `http://localhost:3000`:

1.  Start the development server in your project terminal.
2.  Run `ports` in another terminal.
3.  Look for port `3000` and its process (often `node.exe` for a
    Node.js-based development server).
4.  Open `http://localhost:3000` in your browser.

If the expected port is not listed, the server may not have started, may
be using another port, or may be bound differently. If the port is
listed but the page does not load, check the server terminal for
application errors and verify the URL.

## 🔐 Privacy & permissions

-   The script runs locally on your Windows device.
-   It does not send scan results to a remote server.
-   It does not modify firewall rules or start/stop services.
-   It does not attempt to connect to or scan other devices.
-   Running the terminal as Administrator may reveal process details
    that are otherwise inaccessible. Some process names may still appear
    as `Unknown`.

## ⚠️ Limitations

-   It reports listening endpoints, not every established or closed
    connection.
-   A listening port does not prove that the application is responding
    correctly over HTTP.
-   It does not identify the exact browser tab or project associated
    with a port.
-   Process details can be unavailable because of permissions or
    processes that exit during the scan.
-   The current script uses `psutil.net_connections(kind="inet")`;
    results depend on the operating system's network information and
    permissions.

## 🛠️ Troubleshooting

  -----------------------------------------------------------------------
  Problem                             What to try
  ----------------------------------- -----------------------------------
  `ports` is not recognized           Check that the folder containing
                                      `ports.cmd` is in User PATH, then
                                      reopen the terminal.

  `No module named psutil`            Run `py -m pip install psutil`
                                      using the same Python installation
                                      that runs the script.

  Process shows as `Unknown`          Open PowerShell as Administrator
                                      and run the command again.

  Expected port is missing            Confirm the development server
                                      started and check which port it
                                      printed in its terminal.

  `py` is not recognized              Use `python` in `ports.cmd`, and
                                      confirm Python is on PATH.
  -----------------------------------------------------------------------

## 🤝 Contributing

Contributions, bug reports and suggestions are welcome.

1.  Fork the repository.
2.  Create a branch for your change.
3.  Make your changes and test them on Windows.
4.  Open a pull request with a clear description of the improvement.

Please keep the tool lightweight and avoid adding network scanning or
remote data collection without a clear need and documentation.

## 📄 License

This project is intended to be free and open source under the **MIT
License**. See the [`LICENSE`](LICENSE) file for details.

If you publish this repository, include an MIT `LICENSE` file in the
repository root.

------------------------------------------------------------------------

::: {align="center"}
**Built for developers who want to know what is running on their
localhost.**

If LocalPort helps your workflow, consider giving the project a ⭐ on
GitHub.
:::
