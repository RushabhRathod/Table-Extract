const MongoClient = require('mongodb').MongoClient;
const fs = require('fs');   
const Binary = require('mongodb').Binary;

const url = 'mongodb://localhost:27017';
const dbName = 'table-extract';
const pdfDir = '/home/rushabh/advanced-database-topics/database/pdfs';

run = async () => {
        
    var client = await MongoClient.connect(url, {useUnifiedTopology: true}).catch((err) => {
        console.log("Connection error");
    });
    
    if(!client) {
        console.log("Error");
        exit();
    } else {
        console.log("Succes");
    }
    
    var db = client.db(dbName);
    var collection = await db.collection("pdfs");

    fs.readdirSync(pdfDir).forEach((file, i) => {
        var data = {};
        data.file_data = Binary(file);
        collection.insertOne(data, (err, res) => {
            console.log(file + " stored");
        });
    });
}
run();