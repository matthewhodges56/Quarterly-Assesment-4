# Daily News Email Summarizer 📧 
This Python script automates the process of fetching, summarizing, and sending daily news updates to a list of recipients. It integrates various APIs and libraries for a seamless experience and uses Windows Task Scheduler for automation. Below is a detailed breakdown of the script and its functionality:

## Features 🚀
- Fetch Top News:
  - Utilizes the **NewsAPI** to retrieve the top headlines for the US.

- AI-Powered Summaries:
  - Employs **Google Gemini API (Generative AI)** to summarize each article into concise, reader-friendly snippets.

- Automated Email Delivery:
  - Sends an email with the top 4 summarized news articles using the **Mailgun SMTP** service.

- HTML Formatting:
  - Emails are formatted in a sleek, clean HTML design with clickable links to the original articles.

- Task Scheduler Compatibility:
  - Designed to run automatically at specified times using **Windows Task Scheduler**.

## Script Workflow 🔄
1. Environment Setup:
- Loads sensitive keys and configuration values using `.env` variables:
  - `NEWS_API_KEY`: API key for NewsAPI.
  - `GEMINI_API_KEY`: API key for Google Gemini API.
  - `MAILGUN_EMAIL`: Email address for Mailgun SMTP.
  - `MAILGUN_PASSWORD`: Password for Mailgun SMTP.
  - `EMAIL_RECIPIENTS`: Comma-separated list of recipient email addresses.

2. Fetching News:
- Queries **NewsAPI** for the top 4 headlines, including:
  - Title, author, description, URL, and publication date. 

3. Summarizing Articles:
  - Sends each article's content to the **Google Gemini API** for summarization.

4. Composing Email:
- Constructs an HTML email with:
  - Summarized articles formatted as a bulleted list.
  - Links to the full articles.

5. Sending Email:
- Logs in to **Mailgun's SMTP server** and sends the email to all recipients.

## `.env` File Setup 📂
Ensure the following variables are defined in a `.env` file:
```
NEWS_API_KEY=your_newsapi_key
GEMINI_API_KEY=your_gemini_api_key
MAILGUN_EMAIL=your_mailgun_email
MAILGUN_PASSWORD=your_mailgun_password
EMAIL_RECIPIENTS=recipient1@example.com,recipient2@example.com
```

## Prerequisites 🛠️
- **Python 3.8+** installed.
- Install the required dependencies using:
`pip install requests python-dotenv google-generativeai`
- Access to **NewsAPI**, **Google Gemini**, and **Mailgun** services.

## How It Works ⚙️
1. **NewsAPI** fetches the latest headlines.
2. **Google Gemini API** generates concise summaries for the articles.
3. A formatted HTML email is created with clickable links to the full articles.
4. The email is sent using **Mailgun's SMTP** server to the specified recipients.

## Automation with Windows Task Scheduler ⏰
- Schedule the script to run daily (or as needed) by configuring a task in Windows Task Scheduler.