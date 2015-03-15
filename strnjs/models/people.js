/**
 * Created by pierregm on 3/15/15.
 */

'use strict';

var mongoose = require('mongoose');


var peopleSchema = new mongoose.Schema({
  name: {type: String, required: true},
  realname: {type: String, required: true},
  aliases: Array,
  homebase: {type: String, required: false}
},
{
  colelction: 'people'
});
