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
    console.log('Form-Data:', form_data);
    // TODO: Error handing w/ Axios
    // TODO: Need to make a request to the live link, not local host

    // TODO: How to save t
    axios.post('http://127.0.0.1:3000/', {form_data: form_data }).then((all_events) => {
        console.log(all_events.data[0].Page_1); //Returned Json array of values for Page_1

    }).catch((err) => console.log(err));

    // data: '{"form_data":{"location":"San Francisco","num_of_pages":"1","category":"any_category","event-type":"appearance","time-frame":"today"}}' }

    // TODO: Redirect to User's Dashboard
    // TODO: Look @ Ikey's Authentication middleware in MMYBO project NOTE: Devloper's using the API also need to be authenticated
    res.redirect('/');
})


app.listen(port, () => {
    console.log(`Listening on port ${port}`)
})
