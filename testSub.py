import zmq
import argparse
from logger import getmylogger

log = getmylogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Test Subscriber")
    parser.add_argument("--socket", type=str, default="ipc://SHARED", help="Socket file to connect to (default: ipc://SHARED)")
    parser.add_argument("--filter", type=str, default="", help="Filter string for zmq.SUBSCRIBE (default: '')")
    args = parser.parse_args()

    ctx = zmq.Context()
    sub = ctx.socket(zmq.SUB)
    sub.connect(args.socket)
    sub.setsockopt(zmq.SUBSCRIBE, args.filter.encode())
    log.info(f"Begin Test Sub (Socket: {args.socket}, Filter: {args.filter}")

    try:
        while True:
            try:
                data = sub.recv().decode()
                print(data)
            except Exception as e:
                log.error(f"Exception in testSub: {e}")
                break
    except KeyboardInterrupt:
            pass
    except Exception as e:
         log.error("Exception ",e)
    finally:
        log.info("Exit test SUB")
        sub.close()


if __name__ == "__main__":
    main()
