# 🔍 Naukri Job Scraper

Automated web scraper that extracts job listings from Naukri.com based on search keywords.

## ✨ Features

- Search jobs by role (e.g., "Python Developer", "Data Analyst")
- Extract job details:
  - Job Title
  - Company Name
  - Job Description
  - Link
- Export to CSV with UTF-8 encoding
- Error handling for missing data
- Reusable helper functions for safe scraping

## 🛠️ Tech Stack

- **Python 3.x**
- **Playwright** - Browser automation
- **CSV** - Data export

## 📦 Installation
```bash
# Clone the repository
git clone https://github.com/Aditya01-crypto/Naukri-job-scraper.git
cd Naukri-job-scraper

# Install dependencies
pip install playwright

# Install browser
playwright install chromium
```

## 🚀 Usage
```bash
python scraper.py
```

The script will:
1. Open Naukri.com
2. Search for "Python Developer Or Any Job  Roles. (Just pass the role  in the function "search_job") "
3. Extract job details
4. Save the Details in CSV Files`

## 📊 Sample Output
```csv
Job Title,Company Name,Experience,Location,Gender Preference,Job Description,Link
Python Developer,TCS,4+,Bangalore Mumbai,No Data Found,Looking for Python developer with 2+ years...,https://naukri.com/...
Senior Python Engineer,Infosys,10+,Bangalore Mumbai,Preferred Female Candidates,Experience in Django and Flask required...,https://naukri.com/...
```

## 🔧 Customization

To search for different roles, modify line 92:
```python
search_job("Your Role Here")  # Change this
```

## ⚠️ Notes

- Script uses `slow_mo=300` for visibility (remove for faster scraping)
- Respects Naukri.com's structure (may need updates if site changes)
- For educational purposes only

## 🚧 Future Improvements

- [ ] Add pagination support (scrape multiple pages)
- [ ] Add command-line arguments for role input
- [ ] Implement headless mode for faster scraping
- [ ] Add duplicate detection

## 📝 License

MIT License - Feel free to use and modify

## 👤 Author

**[Aditya Padiyara]**
- GitHub: [@Aditya01-crypto]
- Learning web scraping and automation

---

⭐ Star this repo if you found it useful!
