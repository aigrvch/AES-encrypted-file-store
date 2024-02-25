import os

CONTENT_PATH = os.getcwd() + '/Content'
META_PATH = os.getcwd() + '/Meta'
KEY_PATH = META_PATH + '/key'
MAX_INACTIVE_TIME = 5 * 60
PORT = 8000
ENCODING = 'utf-8'
NONCE_SIZE = 12
TAG_SIZE = 16
CHUNK_SIZE = 128 * 1024
DECRYPT_CHUNK_SIZE = NONCE_SIZE + CHUNK_SIZE + TAG_SIZE
SLASH_REPLACER = '-'
ENCRYPTED_FILE_PREFIX = '_'
