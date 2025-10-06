# Use a lightweight Python base image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy dependency list and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port used by Flask app
EXPOSE 5000

# Run the Flask app with Gunicorn (recommended for production)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "main:app"]
