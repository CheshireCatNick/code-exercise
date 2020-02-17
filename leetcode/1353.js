/**
 * @param {number[][]} events
 * @return {number}
 */
var maxEvents = function(events) {
    events.sort((a, b) => {
        if (a[0] > b[0]) return 1;
        if (a[0] < b[0]) return -1;
        // a[0] == b[0]
        if (a[1] > b[1]) return 1;
        if (a[1] < b[1]) return -1;
        return 0;
    });
    console.log(events);
    let attendNum = 0;
    let time = 0;
    for (let event of events) {
        if (time <= event[0]) {
            time = event[0];
        }
        if (time >= event[0] && time <= event[1]) {
            attendNum++;
        }
        time++;
    }
    return attendNum;
};

console.log(maxEvents([[1,2],[2,3],[3,4]]));
console.log(maxEvents([[1,2],[2,3],[3,4],[1,2]]));
console.log(maxEvents([[1,4],[4,4],[2,2],[3,4],[1,1]]));
console.log(maxEvents([[1,100000]]));
console.log(maxEvents([[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]));
console.log(maxEvents([[1,5],[1,5],[1,5],[2,3],[2,3]]));