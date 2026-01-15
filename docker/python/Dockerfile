FROM python:3.14

# Install system dependencies
# build-essential is for C-extensions, libpq-dev is for PostgreSQL
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Upgrade pip and install dependencies
# We copy requirements first to use Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the entire project code
COPY . .

# Set PYTHONPATH so 'app' can be imported as a module
ENV PYTHONPATH=/app

# Expose the port Uvicorn runs on
EXPOSE 8000

# Start Uvicorn with hot reload enabled for development
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]