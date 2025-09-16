# Python Workshop with Dev Containers

This repository provides a ready-to-use Python development environment using Visual Studio Code Dev Containers. Perfect for workshops, tutorials, or collaborative development.

## 🚀 Quick Start

### Prerequisites

- [Visual Studio Code](https://code.visualstudio.com/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) for VS Code

### Getting Started

1. **Clone this repository:**
   ```bash
   git clone <your-repo-url>
   cd workshop
   ```

2. **Open in VS Code:**
   ```bash
   code .
   ```

3. **Reopen in Container:**
   - VS Code should automatically detect the dev container configuration
   - Click "Reopen in Container" when prompted, or
   - Use the Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`) and run "Dev Containers: Reopen in Container"

4. **Wait for setup:**
   - The container will build and install Python dependencies automatically
   - This may take a few minutes on first run

## 🧪 Testing the Environment

Once the dev container is running, verify everything works:

```bash
python hello_world.py
```

You should see output confirming:
- ✅ Python version and platform information
- ✅ Network connectivity
- ✅ External library functionality (requests)
- ✅ Basic Python operations

## 📁 What's Included

- **Python 3.11** runtime environment
- **Pre-installed packages:**
  - `requests` - HTTP library
  - `jupyter` - Interactive notebooks
  - `ipython` - Enhanced Python shell
- **VS Code extensions:**
  - Python extension
  - Jupyter extension
- **Dev container configuration** for consistent environments

## 🔧 Container Details

The dev container uses:
- **Base image:** `python:3.11-slim`
- **Workspace:** Mounted at `/workspaces/workshop`
- **Port forwarding:** 8888 (for Jupyter if needed)
- **Auto-setup:** Dependencies installed via `requirements.txt`

## 📝 Development Workflow

1. **Edit code** directly in VS Code
2. **Run Python scripts:** `python your_script.py`
3. **Install new packages:** `pip install package-name`
4. **Use terminal** for git, debugging, etc.
5. **Access Jupyter** at `http://localhost:8888` if needed

## 🛠 Customization

To modify the environment:

- **Add Python packages:** Edit `requirements.txt`
- **Change container settings:** Edit `.devcontainer/devcontainer.json`
- **Modify Docker setup:** Edit `.devcontainer/docker-compose.yml`

## 🐛 Troubleshooting

**Container won't start:**
- Ensure Docker Desktop is running
- Try "Dev Containers: Rebuild Container" from Command Palette

**Missing packages:**
- Check that `requirements.txt` includes all needed dependencies
- Rebuild container after changes

**Permission issues:**
- The container runs as user 1000:1000 by default
- Adjust user settings in `docker-compose.yml` if needed

## 📚 Next Steps

Now that your environment is working:
1. Explore the `hello_world.py` example
2. Create your own Python scripts
3. Add workshop materials to this repository
4. Share with participants via GitHub

Happy coding! 🎉