const Singleton = function() {
    let instance = undefined;
    function createInstance() {
        instance = { s: "this is an instance" };
    }
    return {
        New: () => {
            if (instance === undefined) {
                createInstance();
            }
            return instance;
        }
    }
}();
const NotSingleton = function() {
    let instance = undefined;
    function createInstance() {
        instance = { s: "this is an instance" };
    }
    return {
        New: () => {
            createInstance();
            return instance;
        }
    }
}();

const a = NotSingleton.New()
const b = NotSingleton.New()
console.log(a === b)

const c = Singleton.New()
const d = Singleton.New()
console.log(c === d)