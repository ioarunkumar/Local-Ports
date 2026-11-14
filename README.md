 <div align="center">

# 🖥️ LocalPort

### Find open ports. Identify local services. Debug your development environment.

A lightweight Windows command-line tool that lists listening network ports, displays local IP addresses, and identifies the processes using each port.

Quickly check whether your development server appears to be running before opening its `localhost` URL in your browser.

<p>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white" alt="Python 3.8+"></a>
  <a href="https://www.microsoft.com/windows"><img src="https://img.shields.io/badge/Platform-Windows-0078D6?logo=windows&logoColor=white" alt="Windows"></a>
  <a href="https://pypi.org/project/psutil/"><img src="https://img.shields.io/badge/Dependency-psutil-4B8BBE" alt="psutil"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-2ea44f" alt="MIT License"></a>
</p>

<p>
  <a href="#-features">Features</a> ·
  <a href="#-installation">Installation</a> ·
  <a href="#-usage">Usage</a> ·
  <a href="#-how-it-works">How It Works</a> ·
  <a href="#-troubleshooting">Troubleshooting</a> ·
  <a href="#-contributing">Contributing</a>
</p>

</div>

---

## 🎯 Why LocalPort?

During development, it is common to run several local services at the same time:

- Next.js or React development servers (`3000`, `5173`)
- Node.js or Python backends (`5000`, `8000`)
- Databases such as MySQL (`3306`) or PostgreSQL (`5432`)
- Other tools that start local web servers

Sometimes a browser tab at `http://localhost:3000` stops responding, or a new project cannot start because the port is already in use.

**LocalPort gives you a quick view of listening ports and the processes associated with them.**

> **Important:** LocalPort lists listening ports. It does not open a browser, send HTTP requests, or guarantee that a web page is healthy. A listening port indicates that a service is listening for connections. Open the matching `localhost` URL to check the application itself.

## ✨ Features

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>🔎 Open-port listing</h3>
      <p>Displays listening TCP endpoints and their associated local addresses.</p>
    </td>
    <td width="50%" valign="top">
      <h3>🧩 Process identification</h3>
      <p>Displays the process name and port number, helping you identify which application is using a port.</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>🏠 Localhost visibility</h3>
      <p>Shows loopback addresses such as <code>127.0.0.1</code> and <code>::1</code>, along with wildcard listening addresses.</p>
    </td>
    <td width="50%" valign="top">
      <h3>⚡ One-command launch</h3>
      <p>Configure the optional PATH setup and run <code>ports</code> from any directory or VS Code terminal.</p>
    </td>
  </tr>
</table>

## 🚀 Installation

### Requirements

- Windows 10 or Windows 11
- Python 3.8 or later
- PowerShell or Command Prompt
- pip package manager

### 1. Get the project

Clone the repository or download the source files.

```powershell
git clone https://github.com/ioarunkumar/LocalPort.git
cd LocalPort
```


### 2. Install the dependency

```powershell
py -m pip install psutil
```

### 3. Run the script

```powershell
py ports.py
```

If your system uses `python` instead of `py`:

```powershell
python ports.py
```

## 💻 Usage

Run the script from its project directory:

```powershell
py ports.py
```

### Example Output

```text
=== RUNNING LOCALHOST & OPEN PORTS ===

127.0.0.1            PORT: 3000   PROCESS: node.exe
127.0.0.1            PORT: 8000   PROCESS: python.exe
0.0.0.0              PORT: 5000   PROCESS: python.exe
::1                  PORT: 5432   PROCESS: postgres.exe

=== SCAN COMPLETED ===
```

<p><em>Example output only. Actual ports and processes depend on the services running on your computer.</em></p>

### 🌐 Run LocalPort from Anywhere

You can configure LocalPort as a global Windows command.

**1. Place both files in a dedicated folder.**

```text
E:\CODER\Tools\
├── ports.py
└── ports.cmd
```

**2. Create `ports.cmd` with the following content.**

```bat
@echo off
py "E:\CODER\Tools\ports.py" %*
```

**3. Add the folder to your User PATH.**

Open PowerShell and execute:

```powershell
$userPath = [Environment]::GetEnvironmentVariable("Path", "User")

if (($userPath -split ';') -notcontains 'E:\CODER\Tools') {
    [Environment]::SetEnvironmentVariable(
        "Path",
        (($userPath.TrimEnd(';') + ';E:\CODER\Tools').Trim(';')),
        "User"
    )
}
```

**4. Restart your terminal.**

Close and reopen PowerShell, Command Prompt, or VS Code.

**5. Run LocalPort from any directory.**

```powershell
ports
```

> If Windows cannot find `py`, replace it with `python` inside `ports.cmd`.

## 🔄 How It Works

1. LocalPort requests internet network connections using `psutil`.
2. It filters entries whose status is `LISTEN`.
3. It retrieves the local IP address, port number, and process ID.
4. It identifies the process name using the process ID.
5. It displays the available information in the terminal.

### Understanding IP Addresses

<table>
  <thead>
    <tr>
      <th>Address</th>
      <th>Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>127.0.0.1</code></td>
      <td>IPv4 loopback. The service listens on this computer only.</td>
    </tr>
    <tr>
      <td><code>::1</code></td>
      <td>IPv6 loopback. The service listens on this computer only.</td>
    </tr>
    <tr>
      <td><code>0.0.0.0</code></td>
      <td>Wildcard IPv4 address. The service listens on all IPv4 interfaces.</td>
    </tr>
    <tr>
      <td><code>::</code></td>
      <td>Wildcard IPv6 address. The service listens on all IPv6 interfaces.</td>
    </tr>
  </tbody>
</table>

### 🧪 Check Whether Your Development Project Is Running

For example, suppose your project normally runs at `http://localhost:3000`.

1. Start the development server in your project terminal.
2. Open another terminal.
3. Execute `ports`.
4. Look for port `3000` and its associated process (often `node.exe`).
5. Open `http://localhost:3000` in your browser.

**Understanding the results:**

- **Port found:** A service is listening on that port.
- **Port not found:** The server may not have started or may be using another port.
- **Port found but website not loading:** Check the development server terminal for errors and verify the URL.

## 🔐 Privacy & Permissions

- Runs locally on your Windows computer.
- Does not send scan results to a remote server.
- Does not modify firewall rules.
- Does not start, stop, or modify services.
- Does not attempt to scan other devices.
- Administrator privileges may help reveal process details that would otherwise be inaccessible.

Some process names may still appear as `Unknown` because of permissions or processes that exit during execution.

## ⚠️ Limitations

- Reports listening endpoints, not every established or closed connection.
- A listening port does not guarantee that an application is responding correctly over HTTP.
- Does not identify the exact browser tab or project associated with a port.
- Process details may be unavailable because of permission restrictions.
- Uses `psutil.net_connections(kind="inet")`; results depend on operating-system network information and permissions.

## 🛠️ Troubleshooting

<table>
  <thead>
    <tr>
      <th>Problem</th>
      <th>What to Try</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>ports</code> is not recognized</td>
      <td>Check that the folder containing <code>ports.cmd</code> is included in User PATH. Restart your terminal.</td>
    </tr>
    <tr>
      <td><code>No module named psutil</code></td>
      <td>Run <code>py -m pip install psutil</code> using the same Python installation.</td>
    </tr>
    <tr>
      <td>Process shows as <code>Unknown</code></td>
      <td>Try running PowerShell as Administrator.</td>
    </tr>
    <tr>
      <td>Expected port is missing</td>
      <td>Verify that your development server started and check its terminal for the actual port.</td>
    </tr>
    <tr>
      <td><code>py</code> is not recognized</td>
      <td>Replace <code>py</code> with <code>python</code> in <code>ports.cmd</code> and verify Python is available in PATH.</td>
    </tr>
  </tbody>
</table>

## 🤝 Contributing

Contributions, bug reports, feature suggestions, and improvements are welcome!

1. Fork the repository.
2. Create a branch for your changes.
3. Make your changes and test them on Windows.
4. Open a pull request with a clear description.

Please keep LocalPort lightweight and focused on local development diagnostics.

## 📄 License

LocalPort is **free and open-source software**, distributed under the **MIT License**.

You are free to use, modify, distribute, and adapt this project for personal and commercial purposes, subject to the license terms.

See the [`LICENSE`](LICENSE) file for details.

---

<div align="center">

**Built for developers who want to know what's running on their localhost.**

If LocalPort helps your development workflow, consider giving this project a ⭐ on GitHub.

</div>
