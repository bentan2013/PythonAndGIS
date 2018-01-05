# -*- coding: utf-8 -*-
import geocoder
import csv


def _get_lng_lat(_address):
    g = geocoder.google(_address)
    rlt = g.json
    if 'lng' in rlt:
        return rlt["lng"], rlt["lat"]
    else:
        return 0.0, 0.0


def get_position(_address):
    lng, lat = _get_lng_lat(_address)
    if lng == 0.0 and lat == 0.0:
        return None, None
    else:
        return lng, lat


if __name__ == "__main__":
    input_path = "rent.csv"
    output_path = "rent_o.csv"

    csv_file = open(output_path, "w", newline='')
    fieldnames = ['detail', 'address', 'price', 'url', 'lng', 'lat']
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

    address_dict = {}

    with open(input_path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            address = row['address']
            lng = lat = None

            if address not in address_dict:
                lng, lat = get_position('北京' + row['address'])
            else:
                lng = address_dict[address]['lng']
                lat = address_dict[address]['lat']

            if lng is None or lat is None:
                continue
            else:
                address_dict[address] = {'lng': lng, 'lat': lat}
                row['lng'] = lng
                row['lat'] = lat
                csv_writer.writerow(row)
