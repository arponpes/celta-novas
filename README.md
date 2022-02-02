![healthchecks](https://healthchecks.io/badge/e02b0980-fe16-4326-90dd-0f50a6/fbxFeNvy-2.svg)
[![Tests](https://github.com/arponpes/celta-novas/actions/workflows/celta-novas-ci.yml/badge.svg)](https://github.com/arponpes/celta-novas/actions/workflows/celta-novas-ci.yml)

# Celta Novas

Celta novas gets the articles related to the Celta de Vigo football team from four different sources, and then stores the title and the url into the DB. You can access to the list of articles by accessing [celtanovas.dev](https://celtanovas.dev)


## API

[API documentation](https://celtanovas.dev/api/documentation/)


## Getting Started

### Production

docker-compose up --detach --build

### Local

docker-compose up --build

### Tests

With the application running in your local environment execute the following command:

`docker exec -it app pytest`
