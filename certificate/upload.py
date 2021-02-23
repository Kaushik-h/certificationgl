from google.cloud import storage

def pdf_upload(file, filename):
	storage_client = storage.Client()
	bucket = storage_client.bucket('certificates')
	blob = bucket.blob(filename)
	blob.upload_from_filename(file)