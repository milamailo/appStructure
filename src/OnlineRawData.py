import urllib.request
import zlib

def onlineRequest(url):
    """
    Fetches the content from the given URL. Handles gzip compressed content and tries to decode
    it with UTF-8 first, falling back to ISO-8859-1 if UTF-8 decoding fails.

    :param url: The URL to fetch content from.
    :return: The decoded content as a string, or None if an error occurs.
    """
    try:
        response = urllib.request.urlopen(url)
        raw_data = response.read()

        # Check if content is gzip compressed
        if response.info().get('Content-Encoding') == 'gzip':
            raw_data = zlib.decompress(raw_data, zlib.MAX_WBITS | 16)

        # Try to decode with UTF-8 first
        try:
            decoded_data = raw_data.decode('utf-8')
        except UnicodeDecodeError:
            # If UTF-8 fails, try ISO-8859-1
            decoded_data = raw_data.decode('iso-8859-1')

        return decoded_data

    except urllib.error.URLError as e:
        print(f'URL error: {e.reason}')
    except Exception as e:
        print(f'An error occurred: {e}')
        return None