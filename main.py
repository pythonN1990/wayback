from colorama import Fore
import textwrap
import pyfiglet
import argparse
import wayback
import re

def print_figlet(figlet, version, args):
    if args.silent is False:
        figlet_text = pyfiglet.figlet_format(figlet)
        print(Fore.WHITE, figlet_text)
        print(version)

def control_args(args):
    if "." not in args.url:
        raise Exception("Domain extension could not be detected.")

def find_scan_api(args):
    try:
        if args.scan is not None:
            print(textwrap.dedent(
                f"{Fore.YELLOW}[!]{Fore.WHITE} Running '{args.scan}' scan."
            ))
            api = wayback.api.find_scan_type(args.scan)
            return re.sub("example.com", args.url, api)

        else:
            print(textwrap.dedent(
                f"{Fore.YELLOW}[!]{Fore.WHITE} Running 'default' scan."
            ))
            api = wayback.api.find_scan_type("default")
            return re.sub("example.com", args.url, api)

    except Exception as e:
        raise Exception(e)

def control_end_of_launch(args):
    if args.output:
        wayback.api.save_output(args.output)

def main():
    parser = argparse.ArgumentParser(description="Wayback OSINT Tool")

    parser.add_argument(
        "-u", "--url",
        help="Target URL to scan using Wayback Machine",
        required=True
    )
    parser.add_argument(
        "-s", "--scan",
        help="Scan type to run (defined in wayback_api.json)"
    )
    parser.add_argument(
        "-o", "--output",
        help="Save output to file"
    )
    parser.add_argument(
        "--silent",
        action="store_true",
        help="Disable banner and non-essential output"
    )

    args = parser.parse_args()

    control_args(args)
    print_figlet(figlet="Wayback", version="DEMO", args=args)
    api = find_scan_api(args)
    wayback.api.launch_scan(api)
    control_end_of_launch(args)

if __name__ == "__main__":
    main()
