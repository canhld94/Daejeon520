# About this dataset
We crawl Google Streetview Images within 40km2 of the city to create this dataset. There are total  32,880 panorama images are collected, the distance among neigbor panoramas is varied but on average less than 10m. We split those panorama images into two sets: 500 for query set and the rest for database. 
For each crawled panorama image, we generate 8 perspective images with the resolution of 640x640. Here we only provide the perspective images (259,040 database images and 4000 queries)

<img src="/imgs/map.jpg" align="center" width="640" />

# About this repo
- *daejeon520.xlsx*: excel file with three tab:
    - Database: Panorama ID, Latitude and Longtitude
    - Query: Panorama ID, Lattitude and Longtitude
    - Map: Map of all Panorama (both database and query); [you can search for Daejeon on Google Map to verify the map][daejeon].

- *annotation.xlsx*: annotation of the queries. In visual place recognition, we use GPS as the groundtruth location for queries. For each image in the query set, correct locations of the image are all street-view points with the distance to the image’s GPS location less than D meters with D is from 10 to 50. 

# Download links
- *daejeon520.tar.gz* (link comming soon): includes all perspective database images. The format of image names is "PanoramaID_X" with X is from 0 to 7 (corresponding to yaws 0,45,...).

- *daejeon520_query.tar.gz* (link comming soon): includes all perspective query images. The format of image names is "PanoramaID_X" with X is from 0 to 7 (corresponding to yaws 0,45,...).



[daejeon]: https://www.google.com/maps/place/Daejeon/@36.3450802,127.3651532,14z/data=!4m5!3m4!1s0x356548d7ba4a6601:0xd196d69d988ad3b5!8m2!3d36.3504119!4d127.3845475

[map]: /imgs/map.jpg
