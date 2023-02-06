# Use an official Python image as the base image
FROM python:3.10-alpine

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the application code to the container
COPY . .

# Set the environment variable for the application
ENV PYTHONPATH "${PYTHONPATH}:/app"

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
