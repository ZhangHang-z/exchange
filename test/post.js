var querystring = require('querystring');
var http = require('http');

var postData = querystring.stringify({
    username: 'zhg',
    password: '77567wwwwww'
});


var options = {
    hostname: '127.0.0.1',
    port: 8888,
    path: '/',
    method: 'GET',
    headers: {
        'Content-Type': 'appliction/x-www-form-urlencoded',
        'Content-Length': postData.length
    }
};

var req = http.request(options, (res) => {
    console.log(`STATUS: ${res.status}`);
    console.log(`HEADERS: ${res.headers}`);
    res.setEncoding('utf-8');
    res.on('data', (chunk) => {
        console.log(`BODY: ${chunk}`);
    });
    res.on('end', () => {
        console.log('ending...');
    });
});

req.on('error', (err) => {
    console.log(err);
});

req.write(postData);
req.end();