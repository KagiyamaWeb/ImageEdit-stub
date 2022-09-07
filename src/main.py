from watchdog.observers import Observer
import time
import logging
import config

from handlers import MyHandler


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, config.IMAGE_FOLDER, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()