# ⚽ FPL Stat Scraper & ROI Optimizer

![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-Automated-2088FF.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

An automated Python data pipeline that fetches live player statistics from the official **Fantasy Premier League (FPL) API**, calculates player profitability using **Return on Investment (ROI)** metrics, and ranks the most cost-effective assets across every position.

The repository uses **GitHub Actions** to automatically scrape, compute, and update the dataset every Thursday before the upcoming Gameweek deadline.

---

## 🚀 Key Features

* **Live FPL API Integration:** Connects directly to the official Fantasy Premier League `bootstrap-static` endpoint, bypassing Cloudflare/API rate protections using `cloudscraper`.
* **ROI Calculation Engine:** Evaluates player efficiency using the formula: `ROI = Total Points / Current Price (£m)`.
* **Positional Rankings:** Filters and ranks the **Top 5 players** across all four FPL positions: Goalkeepers (`GKP`), Defenders (`DEF`), Midfielders (`MID`), and Forwards (`FWD`).
* **Automated CSV Export:** Outputs structured, ready-to-analyze data into `fpl_top_players_all_positions.csv`[cite: 1].
* **CI/CD Weekly Automation:** A scheduled GitHub Actions workflow (`FPL Weekly Auto-Scraper`) runs every Thursday at **10:00 UTC**, automatically committing the freshest stats directly to the repository.

---

## 📊 Sample Output

When executed locally, `fpl_optimizer.py`[cite: 1] prints a clean summary to the terminal and updates the CSV file



## 📂 Project Structure

```text
fpl-stat-scraper/
├── .github/workflows/                 # GitHub Actions CI/CD workflow configuration
├── fpl_optimizer.py                   # Core Python scraper & ROI calculation script
├── fpl_top_players_all_positions.csv  # Auto-updated output dataset (All positions)
├── fpl_top_midfielders.csv            # Midfielders-specific historical output
├── requirements.txt                   # Python dependencies
└── README.md                          # Project documentation
```

---

## 🛠️ Local Installation & Usage

### 1. Clone the repository
```bash
git clone [https://github.com/noureddine1726/fpl-stat-scraper.git](https://github.com/noureddine1726/fpl-stat-scraper.git)
cd fpl-stat-scraper
```

### 2. Create and activate a virtual environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux / WSL / macOS
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the scraper
```bash
python fpl_optimizer.py
```

---

## ⚙️ Automated Workflow (GitHub Actions)

This project includes a fully automated workflow located in `.github/workflows/`[cite: 1]:
* **Schedule:** Runs automatically every **Thursday at 10:00 AM UTC** (`cron: '0 10 * * 4'`).
* **Manual Trigger:** Can be triggered at any time via the **Actions** tab using `workflow_dispatch`.
* **Bot Commit:** Automatically stages and pushes any changes in `*.csv` files back to the `master` branch.

---

## 👤 Author

**Noureddine Khelfaoui**
* GitHub: [@noureddine1726](https://github.com/noureddine1726)
