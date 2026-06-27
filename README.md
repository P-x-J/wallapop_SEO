# 🛍️ Wallapop SEO
![Project Logo](images/wallapop_SEO.png)

> **Boost your Wallapop listings to the front page without paying for it!**

Wallapop SEO is an intelligent automation tool that keeps your products fresh and visible on Wallapop by strategically updating them, making them appear as recently posted without spending a dime on promotions.

---

## ✨ Features

- 🤖 **Automated Product Updates** – Uses Selenium to edit and refresh your listings
- 📈 **Front-Page Visibility** – Makes your products appear "new" to buyers
- ⏰ **Scheduled Intervals** – Run updates at custom time intervals
- 🎯 **Batch Processing** – Update multiple products in one run
- 🔄 **No API Required** – Works directly with Wallapop's web interface

---

## 🎯 How It Works

Since Wallapop doesn't have a public API, this tool:

1. **Connects via Selenium** – Controls a real Chrome browser
2. **Edits Your Products** – Adds a dot to the description
3. **Removes the Dot** – Reverts the change (product now appears updated)
4. **Repeats** – Keeps your listings fresh on the front page

The key: Wallapop treats edited products as "new," pushing them up in search results.

---

## 📋 Prerequisites

Make sure you have installed:

- **Python 3.8+**
- **ChromeDriver** – Download from [chromedriver.chromium.org](https://chromedriver.chromium.org/)
- **Chromium/Chrome Browser**

Verify installation:

```bash
chromedriver --version
chromium --version
# or
google-chrome --version
