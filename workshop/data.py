# -*- coding: utf-8 -*-

from pymongo import MongoClient

from bson.json_util import dumps

import people
reload(people)
from people import people

import bands
reload(bands)
from bands import bands

import releases
reload(releases)
from releases import releases

client = MongoClient()

db = client.strn_test_20150308


def get_entry_by_name(collection, name):
    entry = collection.find({'$or': [{'name': name},
                                    {'realname': name}]})
    if entry.count() == 0:
        raise Exception('No artist matches %s in collection %s' % (name,
                                                                collection.name))
    if entry.count() > 1:
        raise Exception('Multiple artists match %s in collection %s' %
                        (name, collection))
    entry = dict(entry[0])
    return {
        u'_id': entry['_id'],
        u'name': entry['name']
    }

def get_person_by_name(name):
    return get_entry_by_name(db.people, name)

def get_band_by_name(name):
    return get_entry_by_name(db.bands, name)


if 1:
    db.drop_collection('people')
    for person in people:
        if person.get('realname') is None:
            person['realname'] = person['name']
        db.people.insert(person)
    people_collection = db.people
    people_json = dumps(people_collection.find(),
                        indent=2, sort_keys=True)
    with open('people.json', 'w') as f:
        f.write(people_json)

if 1:
    db.drop_collection('bands')
    bands_collection = db.bands
    for band in bands:
        current_members = []
        for m in band.get('current_members', []):
            try:
                person = get_person_by_name(m)
            except Exception, err_msg:
                print u"\terror while processing current members: %s" % \
                      err_msg
                continue
            member = {
                u'name': person['name'],
                u'_id': person['_id']
            }
            current_members.append(member)
        band['current_members'] = current_members
        previous_members = []
        for m in band.get('previous_members', []):
            try:
                person = get_person_by_name(m)
            except Exception, err_msg:
                print u"\terror while processing current members: %s" % \
                      err_msg
                continue
            member = {
                u'name': person['name'],
                u'_id': person['_id']
            }
            previous_members.append(member)
        band['previous_members'] = previous_members

    db.bands.insert(bands)
    bands_json = dumps(db.bands.find(),
                       indent=2, sort_keys=True)
    with open('bands.json', 'w') as f:
        f.write(bands_json)




releases_collection = db.releases
db.drop_collection('releases')
for release in releases:
    print "Release %s" % release['title']
    artist = release.get('artist')
    if artist is not None:
        try:
            artist = get_band_by_name(artist)
        except Exception, err_msg:
            print u"\t error while processing artist: %s" % err_msg
            continue
        release['artist'] = artist
        db.bands.update({u'_id': artist['_id']},
                        {'$set': {'strn': True}})
    tracklist = []
    for (i, track) in enumerate(release['tracklist']):
        if track.get('position') is None:
            track['position'] = i
        artists = []
        for a in track.get('artists', []):
            try:
                artist = get_band_by_name(a)
            except Exception, err_msg:
                print u"\t error while processing track artist: %s" \
                      % err_msg
                continue
            artists.append(artist)
            db.bands.update({u'_id': artist['_id']},
                            {'$set': {'strn': True}})
        track['artists'] = artists
        #
        extra_artists = []
        for extra in track.get('extra_artists', []):
            try:
                artist = get_person_by_name(extra['name'])
            except Exception, err_msg:
                try:
                    artist = get_band_by_name(extra['name'])
                except Exception, err_msg:
                    print u"\t error while processing extra artist: %s" \
                          % err_msg
                    continue
            artist['role'] = extra.get('role', '')
            print "\t\t", extra, artist
            extra_artists.append(artist)
        if extra_artists:
            track['extra_artists'] = extra_artists
        tracklist.append(track)
    release['tracklist'] = tracklist
    extra_artists = []
    for artist in release.get('extra_artists', []):
        role = artist.pop('role', '')
        try:
            artist = get_person_by_name(artist.get('name'))
        except Exception, err_msg:
            print u"\t error while processing release extra artist: %s" \
                  % err_msg
            continue
        artist = dict(artist)
        extra_artists.append({
            u'name': artist['name'],
            u'_id': artist['_id'],
            u'role': role
        })
    release['extra_artists'] = extra_artists
    db.releases.insert(release)
releases_json = dumps(db.releases.find(),
                      indent=2, sort_keys=True)
with open('releases.json', 'w') as f:
    f.write(releases_json)

