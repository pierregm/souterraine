* Create a `discogs` virtualenv w/ pymongo
* Install `discogs-xml2db` from [https://github.com/philipmat/discogs-xml2db]
* Download the monthly dumps from [http://www.discogs.com/data/]
* Unzip the `.xml.gz` files.
* Transform the `xml` to `json` with the following commands in `ipython`
```python
run discogsparser.py -i -o mongo -p "file:///tmp/discogs/" ../discogs_20150201_artists.xml
run discogsparser.py -i -o mongo -p "file:///tmp/discogs/" ../discogs_20150201_labels.xml
run discogsparser.py -i -o mongo -p "file:///tmp/discogs/" ../discogs_20150201_releases.xml
```
* Use the mongo command to connect to the database and create the indexes you need, the ids at a minimum
```
$ mongo discogs
> db.artists.ensureIndex({id:1}, {background:true,unique:true})
> db.artists.ensureIndex({l_name:1}, {background:true})
> db.releases.ensureIndex({id:1}, {background:true,unique:true})
> db.releases.ensureIndex({l_title:1, l_artist:1}, {background:true, unique:true})
```

Get the tables schema
---------------------
``javascript
var schemaArtists = db.artists.findOne();
for (var key in schemaArtists){ print (key); }

_id
profile
urls
namevariations
l_name
name
aliases
members
images
updated_on
groups
id
data_quality
realname
