const API_KEY = "a2c903cc-b31e-4547-9299-b6d07b7631ab"
const a = 1111111111111;

function encryptApiKey() {
    var t = API_KEY
      , e = t.split("")
      , n = e.splice(0, 8);
    return t = e.concat(n).join("")
}

function encryptTime(t) {
    var e = (1 * t + a).toString().split("")
      , n = parseInt(10 * Math.random(), 10)
      , r = parseInt(10 * Math.random(), 10)
      , o = parseInt(10 * Math.random(), 10);
    return e.concat([n, r, o]).join("")
}

// py_mini_racer 不支持 NodeJs代码，需要改用 PyExecJS 库 
// btoa = function (str) {
//   return new Buffer(str).toString('base64');
// };

function comb (t, e) {
    var n = "".concat(t, "|").concat(e);
    return btoa(n)
}

function getApiKey() {
    var t = (new Date).getTime()
      , e = encryptApiKey();
    return t = encryptTime(t), comb(e, t)
}

console.log(getApiKey())