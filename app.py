from flask import Flask, jsonify, render_template_string
import os
import markdown

app = Flask(__name__)

# A simple string for a basic HTML template
# In a real app, this would be in a templates/ folder.
INDEX_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Children's Book Generator</title>
    <style>
        body { font-family: sans-serif; line-height: 1.6; padding: 2em; max-width: 800px; margin: auto; }
        h1, h2 { color: #333; }
        a { color: #007bff; }
        pre { background-color: #f4f4f4; padding: 1em; border-radius: 5px; }
        .file-link { font-size: 1.2em; margin-bottom: 0.5em; }
    </style>
</head>
<body>
    <h1>Children's Book Generator Project</h1>
    <p>This is a starting point for the platform. Below are the generated content and guide files:</p>

    <h2>Project Files</h2>
    <div class="file-link"><a href="/view/README.md">README.md</a></div>
    <div class="file-link"><a href="/view/book_BearsAndWildlife.md">book_BearsAndWildlife.md</a></div>
    <div class="file-link"><a href="/view/PUBLISHING_GUIDE.md">PUBLISHING_GUIDE.md</a></div>
    <div class="file-link"><a href="/view/PLATFORM_DEV_NOTES.md">PLATFORM_DEV_NOTES.md</a></div>
    <div class="file-link"><a href="/view/EXAMPLE_THEMES.md">EXAMPLE_THEMES.md</a></div>

</body>
</html>
"""

# HTML template for viewing a file
VIEW_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
    <style>
        body { font-family: sans-serif; line-height: 1.6; padding: 2em; max-width: 800px; margin: auto; }
        a { color: #007bff; }
    </style>
</head>
<body>
    <a href="/">&larr; Back to Home</a>
    <hr>
    {{ content|safe }}
</body>
</html>
"""

@app.route('/')
def index():
    """Serves the main index page."""
    return render_template_string(INDEX_HTML)

@app.route('/view/<path:filename>')
def view_file(filename):
    """A simple file viewer to display the content of the markdown files."""
    allowed_files = [
        'README.md',
        'book_BearsAndWildlife.md',
        'PUBLISHING_GUIDE.md',
        'PLATFORM_DEV_NOTES.md',
        'EXAMPLE_THEMES.md'
    ]
    if filename not in allowed_files:
        return "File not found", 404

    try:
        with open(filename, 'r') as f:
            content_md = f.read()
            content_html = markdown.markdown(content_md)
            return render_template_string(VIEW_HTML, title=filename, content=content_html)
    except FileNotFoundError:
        return "File not found", 404

if __name__ == "__main__":
    # Note: A production app would use a proper WSGI server instead of debug=True.
    app.run(host="0.0.0.0", port=8080, debug=True)
