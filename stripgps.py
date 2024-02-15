import argparse
import piexif

def remove_exif_data(filename):
    print(f"Inspecting {filename}")
    exif_dict = piexif.load(filename)
    tags_found = False
    for ifd in ("Exif", "GPS"):
        for tag in exif_dict.get(ifd, {}):
            tags_found = True
            print("    ", piexif.TAGS[ifd].get(tag, {}).get("name"), exif_dict[ifd][tag])

    if tags_found: 
        print(f"Stripping GPS and Exif data from {filename}")
        # Remove GPS and Exif data if present
        exif_dict.pop("GPS", None)
        exif_dict.pop("Exif", None)

        # Save the modified image without EXIF data
        exif_bytes = piexif.dump(exif_dict)
        piexif.insert(exif_bytes, filename)
    else:
        print(f"No GPS/Exif data found in {filename}")
    print("************************************")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Remove EXIF data from JPEG files.')
    parser.add_argument('filenames', nargs='+', help='JPEG files to process')
    args = parser.parse_args()

    for filename in args.filenames:
        remove_exif_data(filename)
