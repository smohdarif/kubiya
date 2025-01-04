# Flask Docker Application with CI/CD

This repository contains a simple Flask web application with Docker containerization and GitHub Actions CI/CD pipeline. The application provides basic endpoints for health checking and demonstrates automated testing and container deployment.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Local Development](#local-development)
- [Running Tests](#running-tests)
- [Docker Setup](#docker-setup)
- [CI/CD Pipeline](#cicd-pipeline)
- [API Endpoints](#api-endpoints)

## Prerequisites

- Python 3.9+
- Docker
- Git
- GitHub account with permissions to create packages

## Project Structure

```
.
├── .github/
│   └── workflows/
│       └── ci-cd.yml
├── app.py
├── test_app.py
├── requirements.txt
├── Dockerfile
└── README.md
```

## Local Development

1. Clone the repository:
```bash
git clone https://github.com/smohdarif/kubiya.git
cd kubiya
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # For Unix/macOS
# OR
.\venv\Scripts\activate   # For Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
OR
python3 -m pip install -r requirements.txt
python3 -m pip install pytest

```

4. Run the application:
```bash
python3 app.py
```

The application will be available at `http://localhost:5000`

## Running Tests

Execute the test suite using pytest:
```bash
python3 -m pytest test_app.py -v
```

Expected output for successful tests:
```
============================= test session starts ==============================
collecting ... collected 3 tests

test_app.py::TestFlaskApp::test_home_status_code PASSED           [ 33%]
test_app.py::TestFlaskApp::test_home_data PASSED                  [ 66%]
test_app.py::TestFlaskApp::test_health_check PASSED               [100%]

============================== 3 passed in 1.23s ==============================
```

## Docker Setup

1. Build the Docker image:
```bash
docker build -t flask-demo .
```

2. Run the container:
```bash
docker run -p 5000:5000 flask-demo
```

3. Access the application at `http://localhost:5000`

## CI/CD Pipeline

The GitHub Actions workflow (`ci-cd.yml`) automates the following:

1. Runs on push to main branch and pull requests
2. Sets up Python environment
3. Installs dependencies
4. Runs tests
5. If tests pass:
   - Logs into GitHub Container Registry
   - Builds Docker image
   - Pushes image to registry

### GitHub Setup Required:

1. Enable GitHub Actions in your repository
2. Configure repository secrets:
   - Go to Settings > Secrets and Variables > Actions
   - Add required secrets:
     - `GITHUB_TOKEN` (automatically provided)

3. Enable improved container support:
   - Go to Settings > Actions > General
   - Enable "Read and write permissions"

### Accessing the Docker Image

After successful pipeline execution:
```bash
docker pull ghcr.io/YOUR-USERNAME/REPO-NAME:latest
```

## API Endpoints

### 1. Root Endpoint
- URL: `/`
- Method: `GET`
- Response Example:
```json
{
    "message": "Hello, Docker World!",
    "hostname": "container-id"
}
```

### 2. Health Check
- URL: `/health`
- Method: `GET`
- Response Example:
```json
{
    "status": "healthy",
    "service": "Flask Demo App"
}
```

## Testing API Endpoints

Using curl:
```bash
# Test root endpoint
curl http://localhost:5000/

# Test health endpoint
curl http://localhost:5000/health
```

Or use your preferred API testing tool (Postman, Insomnia, etc.)

## Troubleshooting

1. If Docker build fails:
   - Ensure Docker daemon is running
   - Check Dockerfile syntax
   - Verify all required files are present

2. If tests fail:
   - Verify Python version (3.9+)
   - Confirm all dependencies are installed
   - Check test assertions match current application behavior

3. If GitHub Actions fail:
   - Check repository permissions
   - Verify secrets are properly configured
   - Review Actions logs for specific error messages

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

