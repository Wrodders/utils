import zmq
import argparse
import time
import lorem
from logger import getmylogger


log = getmylogger(__name__)
def main():
    parser = argparse.ArgumentParser(description="Test Publisher with Command Line Arguments")
    parser.add_argument("--socket", type=str, default="ipc://SHARED", help="Socket file to bind to (default: ipc://SHARED)")
    parser.add_argument("--duration", type=int, default=60, help="Duration of publishing in seconds (default: 60)")
    parser.add_argument("--interval", type=float, default=1.0, help="Interval between messages in seconds (default: 1.0)")
    args = parser.parse_args()

    log.info(f"Starting Publish on {args.socket} for {args.duration} seconds at {args.interval} intervals")

    ctx = zmq.Context()
    pub = ctx.socket(zmq.PUB)
    pub.bind(args.socket)


    start_time = time.time()
    elapsed_time = 0

    try:
        while elapsed_time < args.duration:
            message = lorem.sentence()
            pub.send(message.encode())
            time.sleep(args.interval)
            elapsed_time = time.time() - start_time
    except KeyboardInterrupt:
        pass
    except Exception as e:
        log.error("Exeption: ",e)
    finally:
        log.info("Closing Publisher")
        pub.close()

if __name__ == "__main__":
    main()
