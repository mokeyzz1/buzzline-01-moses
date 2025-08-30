"""
basic_consumer_mk.py

Read a log file as it is being written and do simple real-time analytics.
Flags any line that contains 'MK-ALERT' and prints periodic stats.
"""

# -----------------------------
# Imports
# -----------------------------
import os
import time
import re

from utils.utils_logger import logger, get_log_file_path

# Compile once for speed
ALERT_PATTERN = re.compile(r"\bMK-ALERT\b")

# -----------------------------
# Core processing
# -----------------------------
def process_message(log_file) -> None:
    """
    Tail the log file and process each message in real time.

    Args:
        log_file (str): The path to the log file to read.
    """
    # live stats
    stats_total = 0
    stats_alerts = 0

    with open(log_file, "r") as file:
        # Move to the end of the file so we only read new lines
        file.seek(0, os.SEEK_END)
        print("MK Consumer is ready and waiting for new log messages...")

        while True:
            line = file.readline()

            if not line:
                time.sleep(1)  # wait for new log entry
                continue

            message = line.strip()
            print(f"Consumed log message: {message}")

            # --- MK analytics ---
            stats_total += 1

            # Alert on custom token
            if ALERT_PATTERN.search(message):
                stats_alerts += 1
                alert_text = f"[ALERT] Found MK-ALERT in: {message}"
                print(alert_text)
                logger.warning(alert_text)

            # Every 20 messages, print a tiny running summary
            if stats_total % 20 == 0:
                summary = f"[STATS] total={stats_total}, alerts={stats_alerts}"
                print(summary)
                logger.info(summary)
            # --------------------

# -----------------------------
# Entrypoint
# -----------------------------
def main() -> None:
    """Main entry point."""
    logger.info("START MK consumer...")
    log_file_path = get_log_file_path()
    logger.info(f"Reading file located at {log_file_path}.")

    try:
        process_message(log_file_path)
    except KeyboardInterrupt:
        print("User stopped the process.")
    finally:
        logger.info("END MK consumer.....")

if __name__ == "__main__":
    main()
