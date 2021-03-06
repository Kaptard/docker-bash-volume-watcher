"""
A tool to notify Docker contianers about changes in mounts on Windows.
"""

import argparse
import logging

from docker_volume_watcher.container_monitor import ContainerMonitor


def main():
    """
    Parse command line arguments and start monitoring.
    """

    parser = argparse.ArgumentParser(
        description='A tool to notify Docker contianers about changes in mounts on Windows.'
    )
    parser.add_argument('container_pattern', metavar='CONTAINER_PATTERN', type=str, default='*',
                        nargs='?', help='pattern of container names to be notified (default: *)')

    parser.add_argument('watch_sub_dir', metavar='WATCH_SUB_DIR', type=str, default='', nargs='?')

    parser.add_argument('host_dir_pattern', metavar='HOST_DIR_PATTERN', type=str, default='*',
                        nargs='?', help='pattern of host directories to be monitored (default: *)')

    parser.add_argument("-v", "--verbose", help="increase output verbosity",
                        action="store_true")
    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.INFO)

    monitor = ContainerMonitor(args.container_pattern, args.host_dir_pattern, args.watch_sub_dir)
    try:
        monitor.find_containers()
        monitor.monitor()
    except KeyboardInterrupt:
        logging.info('Got KeyboardInterrupt. Exiting...')

    monitor.unwatch_all()

if __name__ == "__main__":
    main()
