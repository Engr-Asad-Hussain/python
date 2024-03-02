from config import Config


# Define the bind address and port for the server
bind = f"{Config.APP_HOST}:{Config.APP_PORT}"

# Limit the number of worker processes to mitigate excessive memory usage
max_workers = 2

# Time given for worker processes to complete tasks before shutdown
graceful_timeout = 30

# Define the access log location (use "-" for standard output)
accesslog = "-"

# Route error logs to stderr
errorlog = "-"

# Specify the logging level
loglevel = "info"
