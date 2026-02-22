# UV python pack manager

CLI commands
    uv                                                                              - documentation

    uv python list                                                                  - list all available python versions
    uv run <script_name.py> (without '<>')                                          - run script
    uv run --python <python version you want to use> <script_name.py>               - run script with specified python verison

    uv run --with <script name>                                                     - run script with specified dependencies
    uv run --with <script name> --with <other script name>                          - run script with specified dependencies

    uv add --script <script_name.py> "dependency 1" "dependency 2"                  - add dependencies to initialized file
    uv remove                                                                       - remove dependencies

    uv init                                                                         - create new project with README, GIT
    uv init --script <script_name.py> --python <Python version>                     - 

    uv sync                                                                         - sync .venv directory with .toml file

Vocabulary
    .toml (tom's obvious minimal language)                                          - is a requirements.txt, but a lot more detailed
    .lock                                                                           - a package-json.lock, makes sure other devs can run app
