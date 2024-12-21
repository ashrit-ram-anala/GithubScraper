# GithubScraper

## Description

Github Scraper for Internships. Reads from several ReadMEs and writes to a google sheet. Twillio notification integration coming soon.

## Tech Stack

Python, Flask, Google Sheets API, Gspread

## Installation

Create your own Google Cloud Services account with the Google Sheets API Service Account and credentials.json

Set up the Render hosting on Render.com

Add the Github Webhook to your repository

Get your own Google Sheets ID and add it to your own .env file


**Clone The Github Repository:**

```
git clone <SSH/HTTPS Key>
```

**Install Dependencies:**

```
pip install -r requirements.txt
```



**Run App With:**

This should be set up in Render during your hosting under Start Commands

```
python app.py
```