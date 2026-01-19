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
        raise Exception("Domain uzantısı tespit edilemedi.")

def find_scan_api(args):
    try:
        if args.scan is not None:
            print(textwrap.dedent(f"{Fore.YELLOW}[!]{Fore.WHITE} '{args.scan}' tarama çalıştırılıyor."))
            api = wayback.api.find_scan_type(args.scan)
            return re.sub("example.com", args.url, api)
            
        else:
            print(textwrap.dedent(f"{Fore.YELLOW}[!]{Fore.WHITE} 'default' tarama çalıştırılıyor."))
            api = wayback.api.find_scan_type("default")
            return re.sub("example.com", args.url, api)
            
    except Exception as e:
        raise Exception(e)

def control_end_of_launch(args):
    if args.output:
        wayback.api.save_output(args.output)

def main():
    parser = argparse.ArgumentParser(description="Wayback OSINT")
    # // Argüman çekme
    parser.add_argument(
        "-u", "--url",
        help="Wayback'de taranacak URL",
        required=True
    )
    parser.add_argument(
        "-s", "--scan",
        help="Taranacak URL türleri."
    )
    parser.add_argument(
        "-o", "--output",
        help="Çıktı kaydetip kaydetme."
    )
    parser.add_argument(
        "--silent",
        action="store_true",
        help="Sade çıktı."
    )

    args = parser.parse_args()
    # // Argüman çekme
    control_args(args) # // Argümanların hatalı olup olmadığını kontro eder.
    print_figlet(figlet="Wayback", version="DEMO", args=args)
    api = find_scan_api(args)
    wayback.api.launch_scan(api) 
    control_end_of_launch(args) # # // Outputun kaydedilip kaydedilmeyeceğini vs. kontro leder.

if __name__ == "__main__":
    main()
