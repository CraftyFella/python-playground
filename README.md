# Python Workshop with GitHub Codespaces

This repository provides a ready-to-use Python development environment using GitHub Codespaces. Perfect for workshops, tutorials, or collaborative development - no local setup required!

## 🚀 Getting Started

### Step 1: Open in GitHub Codespaces

1. **Click the green "Code" button**
2. **Select the "Codespaces" tab**
3. **Click "Create codespace on main"**

### Step 2: Wait for Environment Setup

- The codespace will automatically start building
- Python 3.11 and dependencies will be installed
- VS Code will open in your browser
- **This takes 2-3 minutes on first run** ⏱️

### Step 3: Verify Everything Works

Once the codespace opens, you'll see VS Code in your browser with two files already open:
- `README.md` (this file)
- `hello_world.py` (our test script)

**Test the environment:**

1. **Open the Terminal** (if not already open):
   - Press `Ctrl+` ` (backtick) or
   - Menu: Terminal → New Terminal

2. **Run the hello world script:**
   ```bash
   python hello_world.py
   ```

3. **Expected output:**
   ```
   🐍 Hello from Python Workshop!
   ==================================================
   Python version: 3.11.x (main, ...)
   Platform: Linux-x.x.x-x86_64
   Python executable: /usr/local/bin/python
   ✅ Network connectivity: Working
   ✅ Requests library: Working
   ✅ Basic math: sum([1, 2, 3, 4, 5]) = 15
   ✅ List comprehension: squares = [1, 4, 9, 16, 25]
   ✅ NumPy: array sum = 15
   ✅ Pandas: DataFrame shape = (3, 2)
   ✅ Matplotlib: Plot creation working
   ✅ SciPy: Version x.x.x
   ✅ Scikit-learn: Version x.x.x
   ==================================================
   🎉 Workshop environment is ready!
   All data science libraries are working correctly!
   You can now start building amazing Python applications!
   ```

### Step 4: Start Coding!

Your Python environment is now ready! You can:
- Create new `.py` files
- Install packages with `pip install package-name`
- Use the integrated terminal
- Access Jupyter notebooks if needed

## 📁 What's Included

- **Python 3.11** runtime environment
- **Pre-installed packages:**
  - `requests` - HTTP library
  - `jupyter` - Interactive notebooks
  - `ipython` - Enhanced Python shell
  - `numpy` - Numerical computing
  - `pandas` - Data manipulation and analysis
  - `matplotlib` - Plotting library
  - `scipy` - Scientific computing
  - `scikit-learn` - Machine learning library
- **VS Code extensions:**
  - Python extension
  - Jupyter extension
- **Dev container configuration** for consistent environments

## 💡 Tips for Workshop Organizers

- **Share the fork link** with attendees: "Go to github.com/CraftyFella/python-playground and click Fork"
- **Each attendee uses their own free GitHub Codespaces hours** (15 GB-hours/month)
- **Codespaces auto-stop after 30 minutes** of inactivity to save resources
- **Workshop materials can be added** to this repository as needed

## 🔧 Technical Details

- **Base image:** Microsoft's official Python 3.11 devcontainer
- **Pre-installed packages:** requests, jupyter, ipython, numpy, pandas, matplotlib, scipy, scikit-learn
- **VS Code extensions:** Python, Jupyter
- **Auto-opens:** README.md and hello_world.py on startup

## 🛠 Customization

To modify the environment:
- **Add Python packages:** Edit `requirements.txt`
- **Change container settings:** Edit `.devcontainer/devcontainer.json`

## 🐛 Troubleshooting

**Codespace won't start:**
- Try creating a new codespace
- Check your GitHub Codespaces usage limits at github.com/settings/billing

**Slow performance:**
- Codespaces may take time to warm up on first use
- Try refreshing the browser if VS Code seems unresponsive

**Can't run Python:**
- Make sure the terminal is active (click in terminal area)
- Try typing `python --version` first to verify Python is available

## 📚 Next Steps

Your Python environment is ready! Consider adding:
1. Workshop exercises and examples
2. Data files for analysis
3. Additional Python packages in `requirements.txt`
4. Jupyter notebooks for interactive coding

**Happy coding!** 🎉
