var b = require('bonescript');
b.analogRead('P9_39', printAIN0);

function printAIN0(err, value) {
    console.log('value = ' + value);
    console.log('err = ' + err);
}                    
