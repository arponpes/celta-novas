## Getting Started

### Production

docker-compose -f docker-compose.prod.yml up --detach --build

### Local

docker-compose up --build

### Tests

pip install tox
tox
