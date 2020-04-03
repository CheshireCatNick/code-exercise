/**
 * @param {number} maxSize
 */
var CustomStack = function(maxSize) {
    this.maxSize = maxSize;
    this.data = [];
};

/** 
 * @param {number} x
 * @return {void}
 */
CustomStack.prototype.push = function(x) {
    if (this.data.length === this.maxSize) return;
    this.data.push(x);
};

/**
 * @return {number}
 */
CustomStack.prototype.pop = function() {
    const l = this.data.length;
    if (l === 0) return -1;
    const val = this.data[l - 1];
    this.data.splice(l - 1, 1);
    return val;
};

/** 
 * @param {number} k 
 * @param {number} val
 * @return {void}
 */
CustomStack.prototype.increment = function(k, val) {
    end = Math.min(this.data.length, k);
    for (let i = 0; i < end; i++) {
        this.data[i] += val;
    }
};

 var obj = new CustomStack(3)
 obj.push(1)
 obj.push(2)
 console.log(obj.pop());
 console.log(obj);
 obj.push(2)
 obj.push(3)
 obj.push(4)
 console.log(obj);

 obj.increment(5,100);
 console.log(obj);

 obj.increment(2,100);
 console.log(obj);

 console.log(obj.pop());
 console.log(obj.pop());
 console.log(obj.pop());
 console.log(obj.pop());
