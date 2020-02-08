/**
 * @param {number[]} arr
 * @return {number}
 */
var minJumps = function(arr) {
    // index => [can go index];
    if (arr.length <= 1) return 0;
    const nArr = [];
    for (let i = 0; i < arr.length; i++) {
        let j = i + 1;
        while (j < arr.length && arr[i] === arr[j]) j++;
        nArr.push(arr[i]);
        if (j < arr.length && j !== i + 1) nArr.push(arr[j - 1]);
        i = j - 1;
    }
    arr = nArr;
    //console.log(arr);
    const map = [];
    for (let i = 0; i < arr.length; i++) {
        let canGo;
        if (i === 0) canGo = [1];
        else if (i === arr.length - 1) canGo = [arr.length - 2];
        else canGo = [i - 1, i + 1];
        map.push(canGo);
    }
    const done = [];
    for (let i = 0; i < arr.length; i++) done.push(false);
    for (let i = 0; i < arr.length; i++) {
        if (done[i]) continue;
        const dst = [i];
        done[i] = true;
        for (let j = i + 2; j < arr.length; j++) {
            if (arr[i] === arr[j]) {
                dst.push(j);
                done[j] = true;
            }
        }
        for (let i of dst) {
            map[i] = map[i].concat(dst);
        }
    }
    //for (i = 0; i < arr.length; i++) console.log(map[i]);
    // bfs
    const passed = [];
    for (let i = 0; i < arr.length; i++) passed.push(false);
    const queue = [{i: 0, s: 0}];
    while (queue.length > 0) {
        const now = queue.shift();
        passed[now.i] = true;
        for (let next of map[now.i]) {
            if (passed[next]) continue;
            if (next === arr.length - 1) {
                return now.s + 1;
            }
            queue.push({i: next, s: now.s + 1});
        }
    }
};

console.log(minJumps([100, -23, -23, 404, 100, 23, 23, 23, 3, 404]));
console.log(minJumps([7]));
console.log(minJumps([7, 6, 9, 6, 9, 6, 9, 7]));
console.log(minJumps([6, 1, 9]));
console.log(minJumps([11, 22, 7, 7, 7, 7, 7, 7, 7, 22, 13]));
console.log(minJumps([7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 11]));