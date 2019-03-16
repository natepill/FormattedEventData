const mongoose = require('mongoose');
const Schema = mongoose.Schema;

// TODO: Add Tags: tags: [{type: String, required: false}]

const Card = new Schema({
    location: {type: String, required: false},
    numberOfPages: {type: Number, required: false},
    category: {type: String, required: false},
    eventType: {type: String, required: false},
    timeFrame: {type: String, required: false},


}, {timestamps: true});
