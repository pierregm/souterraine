/**
 * Created by pierregm on 3/15/15.
 */

'use strict';

var mongoose = require('mongoose');

var bandSchema = new mongoose.Schema({
  name: {type: String, required:true},
  current_members: Array,
  previous_members: Array,
  bio: Buffer,
  pix: String
},
{
  collection: 'bands'
});
