<div align="center">

<img src="./logo.svg" alt="flask-hexagonal" width="180">

_Flask-Hexagonal is an opinionated study-oriented implementation of Python REST API using Hexagonal Architecture design._

</div>

### Features

- Built with Python 🐍 
- Allows switching Web Frameworks interchangeably (Flask <> Falcon)
- Allows switching Databases (Postgres <> Redis)
- Tooling for code styling 
- Automated Testing


## Getting Started

To get a local copy up and running follow the **Prerequisites** and **Setup** sections. After that, you can start to build the new service.

### Prerequisites

Make sure you have a properly Python & Poetry environment.

### Setup

1. Clone the repo
   ```sh
   gh repo clone victormartinez/flask-hexagonal
   ```

2. Install the dependencies
    ```sh
    cd flask-hexagonal/
    poetry install
    ```


## Usage

### Run in development mode

1. Edit flask_hexagonal/main.py and choose the web framework

2. Run project
    ```sh
    make run
    ```


### Run unit tests
```sh
make unit-test
```

### Run system tests
```sh
make integration-test
```

### Help

```sh
make help
```

## Contributing

### Requirements
Pull requests are welcome! Before you open a pull request, make sure the code follow our code style and tests are passing:

```sh
make format
make unit-test
make integration-test
```

### Commit recommendations
Please, use [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) as framework to build commit messages.
