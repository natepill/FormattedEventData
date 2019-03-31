const mongoose = require('mongoose');
const Schema = mongoose.Schema;

// TODO: Add Tags: tags: [{type: String, required: false}]

const Card = new Schema({
    date: {type: String, required: false},
    location: {type: String, required: false},
    price: {type: String, required: false},
    time: {type: String, required: false},
    title: {type: String, required: false},
    numberOfPages: {type: Number, required: false},
    category: {type: String, required: false},
    eventType: {type: String, required: false},
    timeFrame: {type: String, required: false},


}, {timestamps: true});
