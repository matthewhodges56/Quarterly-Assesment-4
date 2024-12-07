# Imports
import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Access variables
newsAPI = os.getenv("NEWS_API_KEY")
geminiAPI = os.getenv("GEMINI_API_KEY")
mailgunEmail = os.getenv("MAILGUN_EMAIL")
mailgunPassword = os.getenv("MAILGUN_PASSWORD")
emailRecipients= os.getenv("EMAIL_RECIPIENTS").split(",")  # Split by commas

# Set up Gemini API
genai.configure(api_key=geminiAPI)
model = genai.GenerativeModel("gemini-1.5-flash")

# Request URL for news
url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       f'apiKey={newsAPI}')

# Fetch news articles
response = requests.get(url)
data = response.json()  # Parse JSON response
articles = data.get("articles", [])

# Summarize articles
summarizedArticles = []
for article in articles[:4]:  # Limit to top 4 articles
    title = article.get("title")
    description = article.get("description")
    author = article.get("author")
    url = article.get("url")
    published_at = article.get("publishedAt")

    # Create a template for summarization
    articleSummaryInput = f"""
    Title: {title}
    Author: {author}
    Description: {description}
    URL: {url}
    Published At: {published_at}
    
    Please summarize the above article in a concise and clear manner. 
    """
    
    # Generate summary using Gemini
    response = model.generate_content(articleSummaryInput)
    summary = response.text
    summarizedArticles.append(f"""
    <li>
        <strong>{title}</strong><br>
        <em>{summary}</em><br>
        <a href="{url}" target="_blank">Read more</a>
    </li>
    """)

# Compose email content as HTML
html_body = f"""
<html>
<head></head>
<body>
    <h2>Daily News Summaries</h2>
    <ul>
        {''.join(summarizedArticles)}
    </ul>
</body>
</html>
"""

# Compose email content
message = MIMEMultipart("alternative")
message["From"] = mailgunEmail
message["To"] = ", ".join(emailRecipients)
message["Subject"] = "Daily News Summaries"
message.attach(MIMEText(html_body, "html"))

# Send email
try:
    with smtplib.SMTP("smtp.mailgun.org", 587) as server:
        server.starttls()
        server.login(mailgunEmail, mailgunPassword)
        server.sendmail(mailgunEmail, emailRecipients, message.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"Error sending email: {e}")
