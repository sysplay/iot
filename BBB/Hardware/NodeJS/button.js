var b = require('bonescript');
b.pinMode('P9_14', b.INPUT);//GPIO 50 correspond to P9_14. More details at http://beagleboard.org/Support/bone101/#headers

setInterval(check, 1000);

function check(){
    b.digitalRead('P9_14', checkButton);
}

function checkButton(err, value) {
    console.log(value);
    if(value == 1) {
        console.log("you are pressing button");
    }
    else{
        console.log("you are not pressing button");
    }
}
