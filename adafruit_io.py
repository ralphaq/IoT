import Adafruit_IO
aio = Adafruit_IO.Client("user", "aio_key")

aio.send("feed_name", "payload_data")

data = aio.receive("feedname").value
