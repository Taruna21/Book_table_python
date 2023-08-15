import logging

# Configure the logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Example log messages
logging.debug("This is a debug message.")
logging.info("This is an info message.")
logging.warning("This is a warning message.")
logging.error("This is an error message.")
logging.critical("This is a critical message.")

'''

In Python, logging is a built-in module that provides a flexible and configurable framework for emitting log messages from your code. Logging is a critical aspect of software development as it helps you track and understand the behavior of your application, diagnose issues, and monitor its performance.

Logging offers several benefits over simple print statements:

Severity Levels: Logging supports different severity levels for messages, such as DEBUG, INFO, WARNING, ERROR, and CRITICAL. This allows you to categorize and prioritize log messages.

Configurability: Logging allows you to configure where log messages go (e.g., console, files, sockets), how they're formatted, and what level of messages to capture. This configurability is particularly useful for debugging, testing, and production environments.

Runtime Control: You can dynamically change logging behavior during runtime without modifying the code. This can be useful for diagnosing issues in production without redeploying the application.

Here's a simple example of how to use the logging module in Python:

'''