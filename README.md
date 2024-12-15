Final Project Proposal: Personal Finance Tracker
Hey there! So for my final project, I’ve decided to create something super practical—a Personal Finance Tracker. I thought this would be a fun way to combine everything we’ve learned so far and build an app that’s actually useful in real life. The idea is to create a web app where you can keep track of your money—like income, expenses, and savings—and even set goals for how much you want to save. Think of it as a budget app, but simpler and more personalized.

What’s the Plan?
Okay, so here’s the rundown of what I want to include in this app:

The Goal
Help users (like us!) track their money without needing to use complicated tools like spreadsheets or apps that are way too over-the-top. You’d log in, add your income and expenses, and see where your money is going—plus, get fun charts and progress bars for your savings goals.

Features for the App
Frontend Stuff
Homepage Dashboard
When you log in, you’ll land on a dashboard that gives you an overview of your finances. It’ll show stuff like:

Total income
Total expenses
How close you are to hitting your savings goals.
Add Transactions
There will be a form where you can quickly add things like:

Money you earned.
Money you spent (with categories like rent, food, and fun stuff).
And yeah, the form will look nice because I’ll be using Bootstrap. No ugly buttons here!
Charts and Visuals
What’s a finance app without some cool charts, right? I’m thinking of adding graphs that show:

How much you spend in each category (like a pie chart).
A bar graph of your spending habits over time.
Savings Goal Tracker
This is where you can set savings goals and track your progress. Like, if you’re saving for a vacation or a new laptop, you’ll see how much closer you are every time you save more.

Search and Filter
Need to find that one random coffee expense from two months ago? No worries—I’ll add search and filter features so you can easily find specific transactions.

Responsive Design
I’ll make sure it looks good on both your laptop and your phone (thanks, Bootstrap!).

Backend Magic
User Accounts
You’ll need to log in to access your data, so I’ll include a signup and login system. And yeah, passwords will be encrypted for safety.

Database
I’ll set up a database to store everything—your income, expenses, categories, and goals. Probably using SQLite or PostgreSQL.

Calculations
The backend will handle all the math, like summing up your income and expenses and calculating how much you’ve saved so far.

Downloadable Reports
If you want, you’ll be able to download a monthly summary as a PDF. I’ll use a library like WeasyPrint for that.

Why This Project?
Honestly, I picked this idea because I’ve always wanted a simple finance app that’s not overloaded with features I don’t need. Plus, I thought it’d be cool to build something that I (and other broke college students) could actually use to track where our money goes. It’s like combining useful skills with real-life problems.

How It’ll Look
Color Scheme and Design
I’m thinking of going for a clean, professional look with greens and blues (you know, “money” vibes).
Buttons and forms will be styled with Bootstrap so it feels modern and easy to use.
Page Layouts
Homepage:
A dashboard with quick stats and visual summaries.
Add Transaction Page:
A form for adding income/expenses with dropdowns for categories.
Reports Page:
A page for charts and progress bars, showing you the bigger picture of your finances.
Tools I’ll Use
Frontend:
HTML, CSS, Bootstrap for styling, and Chart.js for the graphs.
Backend:
Django with Django REST Framework (if I need an API).
Database:
SQLite or PostgreSQL.
Extras:
I might use BeautifulSoup to scrape financial news as an optional feature, and ReportLab or WeasyPrint for the PDF reports.
Reflection on Our Previous Projects
1. Mad Libs Generator
This one was so much fun! It was cool to see how we could take user input and turn it into a funny, interactive story. I really liked how creative it allowed us to be, and it taught me a lot about handling forms and templates. If I could add more, I’d probably include an option for users to create their own stories to share with friends.

2. Book API
The Book API project was a game-changer for me because it helped me understand how to work with APIs and serializers. I also loved learning about filtering and pagination—it’s such a satisfying feeling when things load correctly on a page! The only thing I didn’t like was adding the books manually, but that’s where automation made life easier.

GitHub Links
Mad Libs Generator: Mad Libs Repo
Book API: Book API Repo
Final Thoughts
I’m really excited about this finance tracker project because it’s something I’ve always wanted to build. Plus, it’s a great way to wrap up everything we’ve learned this semester—templates, forms, databases, you name it. And who knows? Maybe it’ll actually help someone save money (or at least keep track of where it’s going)!
