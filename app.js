// const {mongoose} = require('./db/mongoose');

const express = require('express')
const app = express()
const exphbs = require('express-handlebars');
const bodyParser = require('body-parser');


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


app.listen(port, () => {
    console.log(`Listening on port ${port}`)
})
