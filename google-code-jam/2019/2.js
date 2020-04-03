const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let state = 'testCase';
let totalTestCase;
let testCase = 1;
let n, path;

rl.on('line', (line) => {
    switch (state) {
    case 'testCase':
        totalTestCase = parseInt(line);
        state = 'readN';
        break;
    case 'readN':
        n = parseInt(line);
        state = 'readPath';
        break;
    case 'readPath':
        path = line;
        solve(n, path);
        testCase++;
        if (testCase === totalTestCase + 1) rl.close();
        state = 'readN';
        break;
    }
});

// return position with a move
function move(pos, dir) {
    const rPos = { x: pos.x, y: pos.y };
    switch (dir) {
    case 'E':
        rPos.x += 1;
        break;
    case 'S':
        rPos.y += 1;
        break;
    }
    return rPos;
}
function has(s, char) {
    return s.indexOf(char) !== -1;
}
function print(stack) {
    console.log('stack: ');
    stack.forEach(l => console.log(l));
}
function dfs(n, walls) {
    /*
    for (let x = 0; x < n; x++) {
        for (let y = 0; y < n; y++) {
            console.log(walls[x][y]);
        }
    }*/
    // status 'S': trying dir S
    // optimization: block tried path
    const isBlock = [];
    for (let x = 0; x < n; x++) {
        isBlock.push([]);
        for (let y = 0; y < n; y++) {
            isBlock[x].push(false);
        }
    }
    let stack = [{ pos: { x: 0, y: 0 }, status: 'S' }];
    while (stack.length > 0) {
        //print(stack);
        const last = stack[stack.length - 1];
        if (last.status === 'A') {
            //console.log('pop');
            // pop
            //console.log('last', last);
            isBlock[last.pos.x][last.pos.y] = true;
            stack = stack.slice(0, stack.length - 1);
            //console.log(stack.length);
            if (stack[stack.length - 1].status === 'S') {
                stack[stack.length - 1].status = 'E';
            }
            else {
                stack[stack.length - 1].status = 'A';
            }
            continue;
        }
        // next
        let nextPos;
        if (last.status === 'S') {
            // try S
            nextPos = move(last.pos, 'S');
            if (has(walls[last.pos.x][last.pos.y], 'S') ||
                isBlock[nextPos.x][nextPos.y]) {
                // S is blocked
                stack[stack.length - 1].status = 'E';
                continue;
            }
        }
        else if (last.status === 'E') {
            // try E
            nextPos = move(last.pos, 'E');
            if (has(walls[last.pos.x][last.pos.y], 'E') ||
                isBlock[nextPos.x][nextPos.y]) {
                // E is blocked
                stack[stack.length - 1].status = 'A';
                continue;
            }
            //console.log(last.pos, last.status);
        }
        if (nextPos.x === n - 1 && nextPos.y === n - 1) {
            // find a path
            let path = '';
            stack.forEach((node) => path += node.status);
            return path;
        }
        //console.log('here');
        stack.push({ pos: nextPos, status: 'S' });
    }
    return 'path not found';
}
function solve(n, path) {
    // construct walls: [x][y] -> char
    // 'A': all direction, 'S': south is blocked, 'E': east is blocked
    const walls = [];
    for (let x = 0; x < n; x++) {
        walls.push([]);
        for (let y = 0; y < n; y++) {
            walls[x].push('A');
        }
    }
    // boundaries
    for (let y = 0; y < n; y++) {
        walls[n - 1][y] = 'E';
    }
    for (let x = 0; x < n; x++) {
        walls[x][n - 1] = 'S';
    }
    let pos = { x: 0, y: 0 };
    for (let step of path) {
        walls[pos.x][pos.y] += step;
        pos = move(pos, step);
    }
    console.log(`Case #${testCase}: ${dfs(n, walls)}`);
}

