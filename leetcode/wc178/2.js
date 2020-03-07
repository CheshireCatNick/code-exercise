/**
 * @param {string[]} votes
 * @return {string}
 */
var rankTeams = function(votes) {
    const A = 'A'.charCodeAt(0);
    const state = {};
    for (let vote of votes) {
        for (let i = 0; i < vote.length; i++) {
            team = vote[i];
            if (state[team] === undefined) {
                state[team] = new Array(vote.length).fill(0);
            }
            state[team][i]++;
        }
    }
    //console.log(state);
    const teams = [];
    for (let team in state) teams.push(team);
    teams.sort((a, b) => {
        for (let i = 0; i < teams.length; i++) {
            if (state[a][i] > state[b][i]) return -1;
            else if (state[a][i] < state[b][i]) return 1;
        }
        if (a.charCodeAt(0) > b.charCodeAt(0)) return 1;
        else if (a.charCodeAt(0) < b.charCodeAt(0)) return -1;
        return 0;
    });
    let rank = '';
    teams.forEach(team => rank += team);
    return rank;
};

console.log(rankTeams(["ABC","ACB","ABC","ACB","ACB"]));
console.log(rankTeams(["WXYZ","XYZW"]));
console.log(rankTeams(["ZMNAGUEDSJYLBOPHRQICWFXTVK"]));
console.log(rankTeams(["BCA","CAB","CBA","ABC","ACB","BAC"]));
console.log(rankTeams(["M","M","M","M"]));