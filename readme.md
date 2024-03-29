# About this dataset

We crawl Google Streetview Images within 40km2 of the city to create this dataset. There are total  32,880 panorama images are collected, the distance among neighbor panoramas is varied but on average less than 10m. We split those panorama images into two sets: 500 for query set and the rest for database. For each crawled panorama image, we generate 8 perspective images with the resolution of 640x640 each (corresponding to 8 yaw directions 0, 45,…, 315). Here we only provide the perspective images (259,040 database images and 4000 queries).

This dataset is originally used in my master thesis [City-Scale Visual Place Recognition with Deep Local Features Based on Multi-Scale Ordered VLAD Pooling Scheme][thesis]

**Map of all panorama collected:** ([Daejeon on Google Map][daejeon])  

<img src="/imgs/map.jpg" align="center" width="500" />

**Sample images:**  

<img src="/imgs/samples.jpg" align="center" width="720" />

**Compare to some other dataset:**  

*[Pitts250k][netvlad]*  

<img src="/imgs/map_pitts.jpg" align="center" width="500" />

*[Tokyo247][tokyo247]*  

<img src="/imgs/map_247.jpg" align="center" width="500" />

## Files in this repo

- *database.csv*: csv file that describe the database (PanoramaID, Latitude, Longtutide)
- *query.csv*: csv file that describe the query (PanoramaID, Latitude, Longtutide)
- *annotation*: annotation of the queries. In visual place recognition, we use GPS as the groundtruth location for queries. For each image in the query set, correct locations of the image are all street-view points with the distance to the image’s GPS location less than D meters. This folder includes 6 files (corresponding to D = 10m, 20m, 25m, 30m, 40m, and 50m). Each files has 500 rows with the first column is the query panorama id and the following are correct panorama ids in the database.

## Download

- *daejeon520.tar.gz* (17GB): includes all perspective database images. The format of image names is "PanoramaID_X" with X is from 0 to 7 (corresponding to yaws 0,45,...).
- *daejeon520_query.tar.gz* (261MB): includes all perspective query images. The format of image names is "PanoramaID_X" with X is from 0 to 7 (corresponding to yaws 0,45,...).

[Google Drive Link](https://drive.google.com/drive/folders/1MjZcgqC6isgoLkJFPZSfWGpokjJ5wZxq?usp=sharing) 


[thesis]: https://arxiv.org/abs/2009.09255

[daejeon]: https://www.google.com/maps/place/Daejeon/@36.3450802,127.3651532,14z/data=!4m5!3m4!1s0x356548d7ba4a6601:0xd196d69d988ad3b5!8m2!3d36.3504119!4d127.3845475

[map]: /imgs/map.jpg

[map_pitts]: /imgs/map_pitts.jpg

[netvlad]: https://www.di.ens.fr/willow/research/netvlad/

[tokyo247]: http://www.ok.ctrl.titech.ac.jp/~torii/project/247/
