import boto3
import gzip

client = boto3.client(
    's3',
    aws_access_key_id='XXXXXXXXXXXXXXXXXXXX',
    aws_secret_access_key='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
)

def main():
    # your code here
    client.download_file('commoncrawl', 'crawl-data/CC-MAIN-2022-05/wet.paths.gz', 'file.gz')
    
    with gzip.open('file.gz', 'rb') as f:
        file_content = f.read()

        first_link = str((file_content.split(b"\n")[0]))
        first_link = first_link[2:-1]
        print(first_link)

    client.download_file('commoncrawl', first_link, 'fileFromLink.gz')

    with gzip.open('fileFromLink.gz', 'rb') as f2:
        lines = f2.read()
        for line in lines:
            print(line)

    pass


if __name__ == '__main__':
    main()
