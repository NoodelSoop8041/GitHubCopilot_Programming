# Project Reflection

Use evidence from your documented interactions with GitHub Copilot to complete each section. Keep responses specific to the work on the Morrow Goods storefront.

## 1. Project Goal and Problem Breakdown

What did you ask Copilot to help you build? How did you break down the problem?

**Evidence from interactions:**

Me:
"Help me create a basic Flask e-commerce web application using Python. Set up the project structure and create a simple homepage."

Copilot:
"I'll check the workspace's existing README and setup guidance first, then scaffold the smallest runnable Flask shop with a welcoming homepage and verify it starts."

**Reflection:**

To begin my programming experience, I began with a very broud request of creating a Flask e-commerce web app with Python. This request created a much larger amount of structure than I was expecting, developing a functional template of the website, albeit lacking multiple features.

I broke the project down by starting with this broad request, then worked to add additional features such as searching, or the cart page, one by one.

## 2. How Your Questions Evolved

How did your approach to asking questions change as you worked?

**Evidence from interactions:**

Me:
"alright, let's do one last check over the entire project to check for errors or bugs"

Copilot:
"I'll do a project-wide review: inspect the Flask routes, templates, styles, and setup docs, then run the available syntax and end-to-end checks."

**Reflection:**

At the beginning, my prompts were fairly broad because I was mainly trying to get the basic application structure created. I was asking Copilot to help me build features and establish the foundation of the project.

As the application became more complete, my questions became more focused on specific functionality and eventually on testing and debugging.

Instead of asking Copilot to create something new, I was asking it to evaluate what already existed and find problems. Copilot then checked the Flask routes, templates, styles, and setup documentation.

This showed me that my prompts became more specific as I understood the project better. I went from giving Copilot a general goal to asking it to investigate particular parts of an existing application.

## 3. Surprises During Development

What parts of the development process with GitHub Copilot surprised you?

**Evidence from interactions:**

Copilot:
"Pylance's only finding is an environment mismatch: VS Code is using the system Python, where Flask isn't installed, while this project has Flask in .venv."

Copilot:
"A consolidated Flask test-client check passed for search, all 10 product pages, cart updates/removal, invalid checkout input, order confirmation, totals, and clearing the cart."

**Reflection:**

One of the most surprising parts of developing with Copilot was the versatility the AI has. To begin with, I was expecting it to generate simple code snippets or recommendations. By the end of my experience, I found that Copilot was able to fully implement entire code blocks, and perform error checks and validation.

## 4. Technology and New Learning

What did you learn about the technology you used that you didn't know before?

**Evidence from interactions:**



**Reflection:**

Working on this assignment allowed me to learn more about Flask, and how it can be used to create an interactive web app with Python. One of the main things that I learned from this experience, is that Flask can be used to track information within a website, such as the shopping cart. Copilot explained that the bag functionality could update a Flask session so that the website would be interactive instead of being only a static webpage.

The finished application uses the session to keep track of cart quantities. The Flask application retrieves the cart from the session and calculates the number of items for display on the site.

I also learned that Flask's development approach is different from having a traditional database-backed e-commerce system. In this project, the shopping bag is stored in Flask's signed session cookie rather than using persistent order storage. The README explains that this is appropriate for the demonstration application but would not be sufficient for a real e-commerce system.

This helped me understand the difference between building a functional demonstration and building a production application.

## 5. What You Would Change Next Time

What would you do differently if you had to build this again?

**Evidence from interactions:**

Copilot:
"There's no automated test suite in the project, so the workflow checks were run ad hoc."

Copilot:
"Checkout has no CSRF protection, and customer/order details are stored in Flask's signed session cookie, which is readable by the client."

**Reflection:**

If I were to build the program again, I think that I would take more time to develop a preset structure, and plan out what I want to add. I also would create automated tests earlier on, so I don't have to rely on manual and ad hoc testing.

Despite the issues that were found with the final testing, they are not something that needs worked on for this current version of the website. This is due ot the fact that it is a demonstration, and not an actual store. If I were to build this app as an actual store, I would use a database to create persistent orders, utilize appropriate security proteactions, and create an automatic test suite.


