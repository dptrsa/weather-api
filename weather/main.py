from argparse import ArgumentParser
from .weather import Weather

def main():
    pa = ArgumentParser()
    pa.add_argument('location', help='The location to lookup.')
    args = pa.parse_args()
    weather = Weather()
    loc = weather.lookup_by_location(args.location)
    condition = loc.condition()
    print("Weather report for %s" % loc.location()['city'])
    print("Condition: %s " % condition.text())
    print("Temperature: %s" % condition.temp())
        


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)