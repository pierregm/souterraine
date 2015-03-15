/**
 * Created by pierregm on 3/15/15.
 */

'use strict';

var mongoose = require('mongoose');

var releaseSchema = new mongoose.Schema({
  title: {type: String, required: true},
  artist: {
    name: String,
    name_id: ObjectId
  },
  extra_artists: [{
    name: String,
    name_id: ObjectId,
    role: String
  }],
  released: Date,
  labels: [{catno: String, name: String}],
  cover: String
  notes: Buffer,
  tracklist: [{
    position: Number,
    title: String,
    duration: String,
    artists: [{
      name_id: ObjectId,
      name: String,
      role: String
    }],
    extra_artists: [{
      name_id: ObjectId,
      name: String,
      role: String
    }]
  }]
},{
  collection: 'releases'
});
