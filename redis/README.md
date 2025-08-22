# Redis for FastAPI

- install on mac
    - brew install redis

- start redis server
    - redis-server

- open new terminal and run redis-cli
    - set <key> <value> (for example: `set name kar`)
    - get <key> (for example: `get name` # output -> "kar")
    - del <key> (for example: `del name` # output -> 1)
    - exists <key> (for example: `exists name` # output -> 1)
    - expire <key> <seconds> (for example: `expire name 10`)
    - setex <key> <seconds> <value> (for example: `setex name 10 kar` ) 
