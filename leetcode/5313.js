/**
 * @param {number} hour
 * @param {number} minutes
 * @return {number}
 */

var angleClock = function(hour, minutes) {
    if (hour == 12) hour = 0;
    const short = 360 * hour / 12 + 30 * minutes / 60;
    const long = 360 * minutes / 60;
    const abs = n => (n >= 0) ? n : -n;
    const min = (a, b) => (a < b) ? a : b;
    const a = abs(short - long);
    return min(a, 360 - a);    
};

console.log(angleClock(12, 30));
console.log(angleClock(3, 30));
console.log(angleClock(3, 15));
console.log(angleClock(4, 50));
console.log(angleClock(12, 0));