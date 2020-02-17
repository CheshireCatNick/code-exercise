var TweetCounts = function() {
    this.tweets = {};
};

/** 
 * @param {string} tweetName 
 * @param {number} time
 * @return {void}
 */
TweetCounts.prototype.recordTweet = function(tweetName, time) {
    if (this.tweets[tweetName] === undefined) this.tweets[tweetName] = [time];
    else this.tweets[tweetName].push(time);
};

/** 
 * @param {string} freq 
 * @param {string} tweetName 
 * @param {number} startTime 
 * @param {number} endTime
 * @return {number[]}
 */
TweetCounts.prototype.getTweetCountsPerFrequency = function(freq, tweetName, startTime, endTime) {
    const all = this.tweets[tweetName];
    let inTime = all.filter(t => t >= startTime && t <= endTime);
    const fMap = {
        'minute': 60,
        'hour': 3600,
        'day': 86400
    };
    const f = fMap[freq];
    inTime = inTime.map(time => Math.floor(time / f));
    const ans = [];
    for (let t = startTime; t <= endTime; t += f) {
        ans.push(0);
    }
    for (let interval of inTime) {
        ans[interval]++;
    }
    return ans;
};

/*
//Your TweetCounts object will be instantiated and called as such:
var obj = new TweetCounts()
obj.recordTweet('test', 60);
obj.recordTweet('test', 120);
obj.recordTweet('test', 130);
obj.recordTweet('test', 190);
obj.recordTweet('test', 201);
obj.recordTweet('other', 32);
console.log(obj.tweets);
var param_2 = obj.getTweetCountsPerFrequency('hour', 'test', 0, 200000);
console.log(param_2);
*/
const tweetCounts = new TweetCounts();
tweetCounts.recordTweet("tweet3", 0);
tweetCounts.recordTweet("tweet3", 60);
tweetCounts.recordTweet("tweet3", 10);                             // All tweets correspond to "tweet3" with recorded times at 0, 10 and 60.
console.log(tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 59)); // return [2]. The frequency is per minute (60 seconds), so there is one interval of time: 1) [0, 60> - > 2 tweets.
console.log(tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 60)); // return [2, 1]. The frequency is per minute (60 seconds), so there are two intervals of time: 1) [0, 60> - > 2 tweets, and 2) [60,61> - > 1 tweet.
tweetCounts.recordTweet("tweet3", 120);                            // All tweets correspond to "tweet3" with recorded times at 0, 10, 60 and 120.
console.log(tweetCounts.getTweetCountsPerFrequency("hour", "tweet3", 0, 210));  // return [4]. The frequency is per hour (3600 seconds), so there is one interval of time: 1) [0, 211> - > 4 tweets.
