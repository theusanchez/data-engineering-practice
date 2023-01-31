import os
import json

rootdir = '/app/data'

def main():
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            extension = (file.split('.')[1])
            if extension == 'json':
                link = subdir.replace('\\', '/')
                link = link + '/' + file
                with open(link) as json_file:
                    with open(file[0:-4] + 'csv', 'w') as fileToWrite:
                        json_content = json_file.read()
                        data = json.loads(json_content)
                        data['geolocationType'] = data['geolocation']['type']
                        data['geolocationCoordinates'] = data['geolocation']['coordinates']
                        data.pop('geolocation')
                        fileToWrite.write(str(data))
                        fileToWrite.close()

    pass


if __name__ == '__main__':
    main()
