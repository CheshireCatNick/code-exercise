
var ProductOfNumbers = function() {
    this.list = [];
    this.lastZ = -1;
};

/** 
 * @param {number} num
 * @return {void}
 */
ProductOfNumbers.prototype.add = function(num) {
    if (num === 0) {
        this.list.push(1);
        this.lastZ = this.list.length - 1;
        return;
    }
    if (this.list.length === 0) {
        //console.log(num);
        this.list.push(num);
    }
    else {
        const last = this.list[this.list.length - 1];
        //console.log(last);
        this.list.push(num * last);
    }
};

/** 
 * @param {number} k
 * @return {number}
 */
ProductOfNumbers.prototype.getProduct = function(k) {
    const l = this.list.length;
    if (this.lastZ >= l - k) return 0;
    const last = this.list[l - 1];
    const d = (l - k - 1 < 0) ? 1 : this.list[l - k - 1];
    return last / d;
};

 
//Your ProductOfNumbers object will be instantiated and called as such:
var obj = new ProductOfNumbers();
obj.add(3);
obj.add(0);
obj.add(2);
obj.add(5);
obj.add(4);
console.log(obj.getProduct(2));
console.log(obj.getProduct(3));
console.log(obj.getProduct(4));
obj.add(8);
console.log(obj.getProduct(2));
