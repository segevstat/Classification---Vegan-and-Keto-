# Use an official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy source files
COPY app.py .
COPY diet_classifiers.py .
COPY templates/ ./templates

# Install Flask
RUN pip install flask

# Expose port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
