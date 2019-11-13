var x = 0;
var prev_number = 1;
var range_number = 100000;
while (x < range_number) {
    if (x % 3 == 0) {
        console.log(x % 5 == 0 ? 'Maria Health' : 'Maria')
    } else if (x % 5 == 0) {
        console.log('Health');
    } else {
        console.log(x);
    }
    x = (x + prev_number);
    prev_number = (x - prev_number);
}