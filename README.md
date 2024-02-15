# photoprivacyshield
Let's say you want to publish your photos to a web site. Let's say you don't want to reveal the precise location of where the photo was taken. Before you publish, you need to consider stripping the GPS location data from the photos. You can use on-line tools for this and that may be fine if you trust those sites and if you only have one or two photos. But if you have hundreds or thousands of photos, it could be very time consuming. 

In which case, you could use a tool like this to take care of it for you.

No warranty. Be careful - this script will modify files. It's wise to back up your jpeg files first just in case stuff happens.

### How To Use

    photoprivacyshield git:(main) ✗ python3 stripgps.py -h
    usage: stripgps.py [-h] filenames [filenames ...]
    
    Remove EXIF data from JPEG files.
    
    positional arguments:
      filenames   JPEG files to process
    
    options:
      -h, --help  show this help message and exit

### Sample Usage

Let's strip the GPS location data from the file Fireplace_squareon_after.jpg:

    photoprivacyshield git:(main) ✗ python3 stripgps.py Fireplace_squareon_after.jpg
    Inspecting Fireplace_squareon_after.jpg
         ExposureTime (1, 60)
         FNumber (11, 5)
         ExposureProgram 2
         ISOSpeedRatings 250
         ExifVersion b'0232'
         DateTimeOriginal b'2024:02:03 08:29:15'
         DateTimeDigitized b'2024:02:03 08:29:15'
         OffsetTime b'-05:00'
         OffsetTimeOriginal b'-05:00'
         OffsetTimeDigitized b'-05:00'
         ComponentsConfiguration b'\x01\x02\x03\x00'
         ShutterSpeedValue (447643, 75788)
         ApertureValue (177537, 78038)
         BrightnessValue (27549, 11096)
         ExposureBiasValue (0, 1)
         MeteringMode 5
         Flash 16
         FocalLength (111, 50)
         SubjectArea (2009, 1512, 2322, 1328)
         MakerNote b'Apple iOS\\x00\x00\x00....\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n'
         SubSecTimeOriginal b'309'
         SubSecTimeDigitized b'309'
         FlashpixVersion b'0100'
         ColorSpace 65535
         PixelXDimension 4032
         PixelYDimension 3024
         SensingMethod 2
         SceneType b'\x01'
         ExposureMode 0
         WhiteBalance 0
         DigitalZoomRatio (168, 125)
         FocalLengthIn35mmFilm 18
         SceneCaptureType 0
         LensSpecification ((1551800, 699009), (9, 1), (1244236, 699009), (14, 5))
         LensMake b'Apple'
         LensModel b'iPhone 14 Pro Max back triple camera 2.22mm f/2.2'
         GPSLatitudeRef b'N'
         GPSLatitude #####################################
         GPSLongitudeRef b'W'
         GPSLongitude #####################################
         GPSAltitudeRef 0
         GPSAltitude #####################################
         GPSTimeStamp ((13, 1), (29, 1), (14, 1))
         GPSSpeedRef b'K'
         GPSSpeed (0, 1)
         GPSImgDirectionRef b'T'
         GPSImgDirection (596800, 1703)
         GPSDestBearingRef b'T'
         GPSDestBearing (596800, 1703)
         GPSDateStamp b'2024:02:03'
         GPSHPositioningError (69179, 14550)
    Stripping GPS and Exif data from Fireplace_squareon_after.jpg
    ************************************

After completion, the file has been modified with the GPS data stripped. We can prove that by running it through again:

    photoprivacyshield git:(main) ✗ python3 stripgps.py Fireplace_squareon_after.jpg
    Inspecting Fireplace_squareon_after.jpg
    No GPS/Exif data found in Fireplace_squareon_after.jpg
    ************************************
