import collections
from pdf2image.pdf2image import convert_from_bytes
from pdf2image import convert_from_path
import pymongo
import bson
from bson.codec_options import CodecOptions
 
from os import listdir
from os.path import isfile, join
from google.cloud import storage

# client = pymongo.MongoClient("localhost", 27017)
# db = client['table-extract']
# pdfs = db['pdfs']
# data = pdfs.find({})

# # for d in data:
# #     print(d['file_data'])
# #     for k, v in d.items():
# #         print("\t'" + k + "'")
# #     a = a + 1
# decoded_doc = ""
# for d in data:
#     decoded_doc = bson.BSON(d['file_data']).decode()
#     print(decoded_doc)


# Store Pdf with convert_from_path function
# images = convert_from_bytes(decoded_doc)

mypath = '/home/rushabh/advanced-database-topics/database/pdfs/'
onlyfiles = [mypath + f  for f in listdir(mypath) if isfile(join(mypath, f)) ]

for file in onlyfiles:
    print(file)
    print(file.rsplit('/')[-1])

    images = convert_from_path(file)

    for i in range(len(images)):   
        # Save pages as images in the pdf
        images[i].save('./img/' + file.rsplit('/')[-1] + str(i) +'.jpg', 'JPEG')

# def upload_blob(bucket_name, source_file_name, destination_blob_name):
#     """Uploads a file to the bucket."""
#     # bucket_name = "images-data-table-extract"
#     # source_file_name = "/home/rushabh/advanced-database-topics/database/pdfs/Advanced java.pdf"
#     # destination_blob_name = "Advanced java.pdf"

#     storage_client = storage.Client()
#     bucket = storage_client.bucket(bucket_name)
#     blob = bucket.blob(destination_blob_name)

#     blob.upload_from_filename(source_file_name)

#     print("File {} uploaded to {}.".format(source_file_name, destination_blob_name))

# upload_blob("images-data-table-extract", "/home/rushabh/advanced-database-topics/database/pdfs/Advanced java.pdf", "Advanced java.pdf" )

