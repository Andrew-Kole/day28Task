import os
import typing
import requests


API_KEY: typing.Final = os.environ["NASAAPIKEY"]


#b'{"date":"2023-04-30","explanation":"Although its colors may be subtle,
# Saturn\'s moon Helene is an enigma in any light. The moon was imaged in unprecedented detail in
# 2012 as the robotic Cassini spacecraft orbiting Saturn swooped to within a single Earth diameter of
# the diminutive moon. Although conventional craters and hills appear, the above image also shows
# terrain that appears unusually smooth and streaked. Planetary astronomers are inspecting these
# detailed images of Helene to glean clues about the origin and evolution of the 30-km across
# floating iceberg. Helene is also unusual because it circles Saturn just ahead of the large moon
# Dione, making it one of only four known Saturnian moons to occupy a gravitational well known as
# a stable Lagrange point.","hdurl":"https://apod.nasa.gov/apod/image/2304/helene2_cassini_1024.jpg",
# "media_type":"image","service_version":"v1","title":"Saturn\'s Moon Helene in Color",
# "url":"https://apod.nasa.gov/apod/image/2304/helene2_cassini_1024.jpg"}\n'


#get json from NASA api
def get_info():
    r = requests.get("https://api.nasa.gov/planetary/apod", params={"api_key": API_KEY})
    r.raise_for_status()
    content = r.json()
    return content


"""def get_img():
    img_url = get_info()["url"]
    r_img = requests.get(img_url)
    r_img.raise_for_status()
    img = r_img.content
    with open("image.jpg", "wb") as file:
        file.write(img)
"""

