// const {mongoose} = require('./db/mongoose');

const express = require('express')
const app = express()
const exphbs = require('express-handlebars');
const bodyParser = require('body-parser');
const request = require('request');
const axios = require('axios');

// const fs = require('fs');
// const request = require('request')

const port = process.env.PORT || 5000;


app.engine('handlebars', exphbs({defaultLayout: 'main'}));
app.use(require('method-override')('_method'));
app.use(express.static('public'));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.set('view engine', 'handlebars');

app.get('/', (req, res) => {
    res.render('home')
})

app.get('/form-submit', (req, res) => {
    const form_data = req.query

    // TODO: Error handing w/ Axios
    axios.post('http://127.0.0.1:5000/', {form_data: form_data });

    // TODO: Redirect to User's Dashboard
    // TODO: Look @ Ikey's Authentication middleware in MMYBO project NOTE: (MAY NOT WORK FOR ALL ROUTES) because we are trying to integrate a developer API
    res.redirect('/');
})


app.listen(port, () => {
    console.log(`Listening on port ${port}`)
})
