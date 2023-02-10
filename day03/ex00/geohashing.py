import sys
import antigravity

def validate_args():
    if len(sys.argv) != 4:
       sys.exit("Geohash takes 4 arguments: <latitude> <longitude> " +
			"<YYYY-mm-dd-dowopening>.\nRespectively: a float, a float and a string.")

def is_float(nbr):
	try:
		cast = float(nbr)
		return cast
	except ValueError as e:
		sys.exit(e)

def is_string(arg):
	try:
		cast = str(arg)
		return cast
	except ValueError as e:
		sys.exit(e)

def main():
    validate_args()
    try:
        latitude = is_float(sys.argv[1])
        longitude = is_float(sys.argv[2])
        datedow = is_string(sys.argv[3])
        antigravity.geohash(latitude, longitude, datedow.encode())
    except ValueError:
        sys.exit("format for latitude/longitude wrong")
if __name__ == "__main__":
    main()

#37.421542 -122.085589 2005-05-26-10458.68